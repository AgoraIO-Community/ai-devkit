#!/usr/bin/env python3
"""Generate audio + timing for AI DevKit presentation."""

import json
import os
import re
import struct
import sys
import urllib.request

API_KEY = os.environ.get("TTS_KEY")
if not API_KEY:
    raise SystemExit("Set TTS_KEY environment variable (ElevenLabs API key)")
VOICE_ID = "XnKbmWxx8uWjruHkpXmf"
MODEL_ID = "eleven_v3"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
PRESENTATION_MD = os.path.join(ROOT_DIR, "presentation.md")
AUDIO_DIR = os.path.join(SCRIPT_DIR, "audio")
TIMING_DIR = os.path.join(SCRIPT_DIR, "timing")
SUBS_DIR = os.path.join(SCRIPT_DIR, "subs")


def parse_slides(path):
    """Parse presentation.md into slides: [{title, text}]."""
    with open(path) as f:
        content = f.read()

    slides = []
    parts = re.split(r"^## ", content, flags=re.MULTILINE)
    for part in parts[1:]:  # skip preamble before first ##
        lines = part.strip().split("\n", 1)
        title = lines[0].strip()
        text = lines[1].strip() if len(lines) > 1 else ""
        slides.append({"title": title, "text": text})
    return slides


def generate_audio_with_timestamps(text, output_audio, output_timing):
    """Call ElevenLabs API, save audio and timing."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"
    payload = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8,
            "speed": 0.9,
        },
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())

    # Decode base64 audio
    import base64
    audio_bytes = base64.b64decode(data["audio_base64"])
    with open(output_audio, "wb") as f:
        f.write(audio_bytes)

    # Save alignment/timing
    alignment = data.get("alignment", {})
    characters = alignment.get("characters", [])
    char_start_times = alignment.get("character_start_times_seconds", [])
    char_end_times = alignment.get("character_end_times_seconds", [])

    # Reconstruct words from characters
    words = []
    current_word = ""
    word_start = None
    word_end = None

    for i, char in enumerate(characters):
        if char == " ":
            if current_word:
                words.append({
                    "word": current_word,
                    "start": word_start,
                    "end": word_end,
                })
                current_word = ""
                word_start = None
        else:
            if word_start is None:
                word_start = char_start_times[i]
            word_end = char_end_times[i]
            current_word += char

    if current_word:
        words.append({
            "word": current_word,
            "start": word_start,
            "end": word_end,
        })

    # Strip audio tags (e.g. [pause], [excited], [short pause]) from word list
    # Tags may span multiple word entries: [short -> pause] or be single: [pause]
    cleaned = []
    in_tag = False
    for w in words:
        if w["word"].startswith("[") and w["word"].endswith("]"):
            continue  # single-word tag like [pause]
        if w["word"].startswith("["):
            in_tag = True
            continue
        if in_tag:
            if w["word"].endswith("]"):
                in_tag = False
            continue
        cleaned.append(w)
    words = cleaned

    timing = {
        "words": words,
        "duration": char_end_times[-1] if char_end_times else 0,
    }

    with open(output_timing, "w") as f:
        json.dump(timing, f, indent=2)

    return timing


def get_audio_duration_mp3(path):
    """Rough MP3 duration from file size and assumed bitrate."""
    # Better: parse actual frames. For now use timing data instead.
    return None


def generate_srt(all_timings, output_path, max_words=12, max_duration=5.0):
    """Generate SRT subtitle file from timing data.

    Groups words into subtitle lines, breaking at sentence boundaries
    (periods, question marks, exclamation marks, em dashes followed by
    a pause) or when max_words/max_duration is reached.
    """
    srt_entries = []
    idx = 1

    for slide_timing in all_timings:
        offset = slide_timing["offset"]
        words = slide_timing["timing"]["words"]

        group = []
        for w in words:
            group.append(w)

            # Check if we should break here
            ends_sentence = w["word"].rstrip().endswith((".", "?", "!"))
            at_max_words = len(group) >= max_words
            at_max_duration = (
                len(group) > 1
                and (w["end"] - group[0]["start"]) >= max_duration
            )
            # Break at comma/semicolon if group is already 6+ words
            at_clause = (
                len(group) >= 6
                and w["word"].rstrip().endswith((",", ";", ":"))
            )

            if ends_sentence or at_max_words or at_max_duration or at_clause:
                start = offset + group[0]["start"]
                end = offset + group[-1]["end"]
                text = " ".join(g["word"] for g in group)
                # Clean up stray whitespace
                text = " ".join(text.split())

                srt_entries.append({
                    "idx": idx,
                    "start": start,
                    "end": end,
                    "text": text,
                })
                idx += 1
                group = []

        # Flush remaining words
        if group:
            start = offset + group[0]["start"]
            end = offset + group[-1]["end"]
            text = " ".join(g["word"] for g in group)
            text = " ".join(text.split())
            srt_entries.append({
                "idx": idx,
                "start": start,
                "end": end,
                "text": text,
            })
            idx += 1

    with open(output_path, "w") as f:
        for entry in srt_entries:
            # Strip audio tags like [pause], [short pause], [deliberate] etc.
            text = re.sub(r"\[.*?\]\s*", "", entry["text"]).strip()
            if not text:
                continue
            f.write(f"{entry['idx']}\n")
            f.write(f"{format_srt_time(entry['start'])} --> {format_srt_time(entry['end'])}\n")
            f.write(f"{text}\n\n")


def format_srt_time(seconds):
    """Format seconds as SRT timestamp: HH:MM:SS,mmm."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def concatenate_mp3(files, output):
    """Concatenate MP3 files by raw byte appending."""
    with open(output, "wb") as out:
        for f in files:
            with open(f, "rb") as inp:
                out.write(inp.read())


def main():
    slides = parse_slides(PRESENTATION_MD)
    print(f"Found {len(slides)} slides")

    # Check which slides to generate (allow partial runs)
    slide_arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    srt_only = slide_arg == "srt"

    if srt_only or slide_arg == "all":
        to_generate = list(range(len(slides)))
    else:
        to_generate = [int(slide_arg) - 1]  # 1-indexed arg

    all_timings = []
    audio_files = []
    cumulative_offset = 0.0

    for i in range(len(slides)):
        slide = slides[i]
        audio_path = os.path.join(AUDIO_DIR, f"slide-{i+1:02d}.mp3")
        timing_path = os.path.join(TIMING_DIR, f"slide-{i+1:02d}.json")

        if srt_only or i not in to_generate:
            # Load existing timing
            if os.path.exists(timing_path):
                with open(timing_path) as f:
                    timing = json.load(f)
            else:
                print(f"  Skipping slide {i+1} (no existing timing)")
                continue
        else:
            print(f"Generating slide {i+1}: {slide['title']}")
            timing = generate_audio_with_timestamps(
                slide["text"], audio_path, timing_path
            )
            print(f"  Duration: {timing['duration']:.1f}s, Words: {len(timing['words'])}")

        all_timings.append({
            "slide": i + 1,
            "title": slide["title"],
            "offset": cumulative_offset,
            "timing": timing,
        })
        audio_files.append(audio_path)
        cumulative_offset += timing["duration"]  # no gap — v3 audio tags handle pacing

    # Concatenate audio
    if audio_files:
        full_audio = os.path.join(AUDIO_DIR, "full.mp3")
        concatenate_mp3(audio_files, full_audio)
        print(f"\nFull audio: {full_audio} ({cumulative_offset:.1f}s total)")

    # Generate English SRT
    if all_timings:
        en_srt = os.path.join(SUBS_DIR, "en.srt")
        generate_srt(all_timings, en_srt)
        print(f"English subtitles: {en_srt}")

    # Save combined timing for the video renderer
    combined_timing = os.path.join(TIMING_DIR, "combined.json")
    with open(combined_timing, "w") as f:
        json.dump(all_timings, f, indent=2)
    print(f"Combined timing: {combined_timing}")

    print("\nDone. Next steps:")
    print("  1. Review audio quality in audio/slide-01.mp3")
    print("  2. Generate Chinese subtitles")
    print("  3. Build the HTML player or render video frames")


if __name__ == "__main__":
    main()
