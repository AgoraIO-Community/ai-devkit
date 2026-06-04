# ElevenLabs Voiceover Generation

> **When to Read This:** Load this document when you are generating or updating
> presentation voiceovers, changing `presentation.md` audio tags, or debugging
> TTS output quality.

Reference for generating presentation voiceovers using the ElevenLabs TTS API.

## API

All endpoints use the `/v1/` path. Model generation is selected via `model_id`.

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps
```

Authentication: `xi-api-key` header. Store the key in `TTS_KEY` env var — never hardcode it.

## Models

| Model | `model_id` | Notes |
|-------|-----------|-------|
| Eleven v3 | `eleven_v3` | Latest. 70+ languages. Supports audio tags. Use this. |
| Eleven Flash v2.5 | `eleven_flash_v2_5` | Ultra-low latency (~75ms). For real-time/agents. |
| Eleven Multilingual v2 | `eleven_multilingual_v2` | Legacy default. 28 languages. No audio tags. |

## Voice IDs

| Voice | ID | Use |
|-------|-----|-----|
| Primary (EN) | `XnKbmWxx8uWjruHkpXmf` | English presentation voiceover |
| Chinese alt | `BrbEfHMQu0fyclQR7lfh` | Chinese voiceover alternative |

## Voice Settings

```json
{
  "stability": 0.7,
  "similarity_boost": 0.8,
  "speed": 0.95
}
```

- **stability** — Higher = more consistent, calmer delivery. Use 0.65-0.8 for presentations.
- **similarity_boost** — How closely to match the voice. 0.75-0.85 is good.
- **speed** — Range 0.7 (slow) to 1.2 (fast). Default 1.0. Use 0.93-0.97 for natural presentation pacing.
- **style** — Expressiveness. Only used on v2 models. Not needed for v3 (use audio tags instead).

## Audio Tags (eleven_v3 only)

Audio tags control delivery inline. They replace SSML `<break>` tags from older models.

### Pauses

```
[pause]              — Standard pause (~0.5-1s)
[short pause]        — Brief beat (~0.3s)
[long pause]         — Extended pause (~1.5s)
[continues after a beat]
```

### Pacing

```
[deliberate]         — Slow, measured delivery
[slows down]         — Gradual deceleration
[rushed]             — Speed up delivery
[rapid-fire]         — Fast staccato
```

### Tone and Emotion

```
[thoughtful]         — Reflective, considered
[excited]            — Energetic opener
[sigh]               — Audible sigh
[emphatic]           — Strong emphasis on next phrase
[flatly]             — Deadpan delivery
```

### Rhythm

```
[stammers]           — Hesitant delivery
[drawn out]          — Elongated words
[breathes]           — Audible breath
```

## Examples

### Presentation slide with pacing

```
AI DevKit is an operating model for AI-centric software engineering.
[short pause] AI writes specs, tests, code, and docs. [pause]
Humans approve the spec and approve the release.
```

Note: the title slide greeting uses `[excited]` for an energetic opener. Each subsequent slide transition also uses `[excited]` for a fresh energy reset.

### Making a key point land

```
[deliberate] The key discipline here: decide in the spec, not in the code.
[pause]
If you let the AI defer decisions to implementation, [short pause]
it makes them implicitly, often inconsistently,
and you only find out when you're reading the code.
```

### Rhetorical question

```
[thoughtful] Why prompts instead of skills or slash commands?
[short pause]
Skills are tool-specific. A Claude Code skill doesn't work in Cursor.
A Cursor command doesn't work in Codex.
```

### Emotional delivery

```
"It was a VERY long day [sigh] ... nobody listens anymore."
```

## Script Conventions

When writing `presentation.md` for TTS generation:

1. Put audio tags at natural speech boundaries — start of slides, after questions, before key points
2. Use `[pause]` between major ideas within a slide
3. Use `[short pause]` after rhetorical questions or list items
4. Use `[excited]` at the opening slide greeting and at subsequent slide transitions to set fresh energy
5. Use `[deliberate]` before the single most important sentence per slide
6. CAPS for emphasis words (e.g. "VERY") — the model respects this
7. Keep speed at 0.93-0.97 for presentation voiceover — natural pace, not sluggish
8. Never use abbreviations in voiceover text (write "test-driven development" not "TDD", "continuous integration" not "CI")
9. Keep technical terms consistent with slide visuals (e.g. "Verify AI" not "Verifier AI")

## Presentation Pipeline

### Slide Structure

`presentation.md` has 8 slides (Slide 1 -- Slide 8) that generate audio via ElevenLabs TTS. `player.html` has 10 display slides:

| Display Slide | Content | Audio |
|---------------|---------|-------|
| 1 (title) | Title card | Greeting from Slide 1 audio plays during first 3s (`TITLE_AUDIO`) |
| 2--9 (content) | SVG diagrams + transcript | Slides 1--8 audio maps to display slides 2--9 |
| 10 (closing) | Laptop photo (`images/closing.png`) | No dedicated audio -- appears when "Goodbye for now" subtitle starts |

The title slide greeting uses the `[excited]` tag ("Hello and welcome").

### Recorder Timing Constants (`record.mjs`)

| Constant | Value | Description |
|----------|-------|-------------|
| `TITLE_HOLD` | 2s | Silent hold on title slide before audio starts |
| `TITLE_AUDIO` | 3s | Audio plays while title slide stays visible (greeting overlap) |
| `CLOSING_HOLD` | 4s | Hold on closing slide after audio ends |
| `SUB_LINGER` | 0.8s | Subtitle text stays visible past its audio end time |

Frame capture sequence: `TITLE_HOLD` silent frames, then audio-driven frames (title stays during first `TITLE_AUDIO` seconds, then display slides 2--9 track `combinedTiming`), then `CLOSING_HOLD` frames on slide 10.

### Files

| Path | Purpose |
|------|---------|
| `presentation.md` | Voiceover script -- one `## Slide N` section per slide (8 slides) with audio tags |
| `presentation/player.html` | HTML slide deck with 10 display slides, SVG diagrams, transcript, subtitle rendering, playback |
| `presentation/generate.py` | TTS generation -- calls ElevenLabs API, produces MP3s + timing + SRT |
| `presentation/record.mjs` | Playwright-based video recorder -- captures frames + composes MP4 with ffmpeg |
| `presentation/audio/` | Per-slide MP3s (`slide-01.mp3` ... `slide-08.mp3`) + concatenated `full.mp3` |
| `presentation/images/` | Static assets -- `closing.png` (laptop photo shown on closing slide 10) |
| `presentation/timing/` | Per-slide timing JSON + `combined.json` |
| `presentation/subs/en.srt` | English subtitles (auto-generated from timing) |
| `presentation/subs/zh.srt` | Chinese subtitles (manually translated from en.srt) |
| `presentation/runs/` | Recorded MP4 videos (gitignored) |
| `.env` | `TTS_KEY` -- ElevenLabs API key (gitignored) |

### Regenerating Audio

The API key lives in `.env` at repo root. Source it before running.

```bash
# Regenerate all slides
source .env && export TTS_KEY && python3 presentation/generate.py

# Regenerate a single slide (1-indexed)
source .env && export TTS_KEY && python3 presentation/generate.py 1

# Regenerate only SRT + combined timing (no API calls)
source .env && export TTS_KEY && python3 presentation/generate.py srt
```

The script parses `presentation.md`, calls the API per slide, saves individual MP3s + timing JSON, concatenates into `audio/full.mp3`, and generates `subs/en.srt`.

### Translating Chinese Subtitles

After regenerating `en.srt`, translate to `zh.srt` manually. Rules:
- Timestamps must match `en.srt` exactly
- Keep technical terms in English: AI DevKit, Lead AI, Verify AI, Progressive Disclosure, Git, Pull Request, Playwright, Terraform, curl, claude, codex, GitHub, markdown, LLM, Level zero/one/two
- No abbreviations (same rule as voiceover)

### Recording Video

Requires Node 22+, Playwright, and ffmpeg.

```bash
# Start HTTP server (if not already running)
python3 -m http.server 8090 -d presentation &

# Record
nvm use 22 && node presentation/record.mjs
```

Output: `presentation/runs/ai-devkit-overview-YYYY-MM-DD_HHMM.mp4`

The recorder captures frames from `player.html` at 10fps: 2s silent title hold, then audio-driven frames (title stays visible for the first 3s of audio while the greeting plays, then content slides 2--9 track timing data, and slide 10 appears when "Goodbye for now" starts), then 4s closing slide hold. Frames are composed into a 30fps MP4 with the audio track using ffmpeg (audio is delayed by `TITLE_HOLD` via `adelay` filter).

### Subtitle Layout

The subtitle panel in `player.html` uses a fixed `height: 110px` with `min-height` on the text elements to prevent the slide area from shifting vertically when subtitles appear and disappear.
