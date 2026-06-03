# ElevenLabs Voiceover Generation

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
  "speed": 0.9
}
```

- **stability** — Higher = more consistent, calmer delivery. Use 0.65-0.8 for presentations.
- **similarity_boost** — How closely to match the voice. 0.75-0.85 is good.
- **speed** — Range 0.7 (slow) to 1.2 (fast). Default 1.0. Use 0.85-0.92 for deliberate presentation pacing.
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
[excited] AI DevKit is an operating model for AI-centric software engineering.
[short pause] AI writes specs, tests, code, and docs. [pause]
Humans approve the spec and approve the release.
```

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
4. Use `[excited]` or `[thoughtful]` at slide openings to set tone
5. Use `[deliberate]` before the single most important sentence per slide
6. CAPS for emphasis words (e.g. "VERY") — the model respects this
7. Keep speed at 0.85-0.92 for presentation voiceover — prefer deliberate over rushed

## Generating

```bash
TTS_KEY=your_key python presentation/generate.py
```

The script parses `presentation.md`, calls the API per slide, saves individual MP3s + timing JSON, then concatenates into `audio/full.mp3` and generates `subs/en.srt`.
