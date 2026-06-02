#!/usr/bin/env python3
"""Generate English and Chinese audio samples for voice comparison.

Usage:
  TTS_KEY=sk_... python generate_samples.py

Generates two ~2 min clips using voice XnKbmWxx8uWjruHkpXmf:
  audio/sample-en.mp3  — English narration (slides 2+3)
  audio/sample-zh.mp3  — Chinese narration (same content)
"""

import base64
import json
import os
import urllib.request

API_KEY = os.environ.get("TTS_KEY")
if not API_KEY:
    raise SystemExit("Set TTS_KEY environment variable (ElevenLabs API key)")
VOICE_A = "XnKbmWxx8uWjruHkpXmf"  # Voice A
VOICE_B = "BrbEfHMQu0fyclQR7lfh"  # Voice B (Chinese alternative)
MODEL_ID = "eleven_multilingual_v2"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(SCRIPT_DIR, "audio")

# Slides 2 and 3 transcript text (~2 min when spoken)
EN_TEXT = (
    "AI DevKit is an operating model for AI-centric software engineering. "
    "AI writes specs, tests, code, and docs. Humans approve the spec and "
    "approve the release. It works with your existing stack — git, repos, "
    "pull requests, CI — and reshapes it around AI execution, while keeping "
    "the human checkpoints that matter. There are four pillars: spec planning, "
    "test-driven implementation, Progressive Disclosure docs, and the AI dev "
    "environment. "
    "Work comes in as a story, epic, bug, or feature. It flows through three "
    "phases: Plan, Implementation, and Release. The Lead AI executes the "
    "workflow. The Verifier AI independently checks key transitions — it's a "
    "second AI from a different training lineage. Why two AIs? A single AI is "
    "confidently wrong in ways invisible to itself. Asking the same model to "
    "review its own output rarely catches the error. Two independent lineages "
    "catch different mistakes. The Plan phase produces a spec. The "
    "Implementation phase produces working code, tests, and updated docs. "
    "That deliverable passes through Release — a CI gate plus human approval."
)

ZH_TEXT = (
    "AI DevKit 是一种以 AI 为中心的软件工程运营模式。"
    "AI 负责编写规格说明、测试、代码和文档。人类负责审批规格说明和发布。"
    "它与你现有的技术栈兼容——git、代码仓库、Pull Request、CI——"
    "围绕 AI 执行进行重新组织，同时保留关键的人工检查点。"
    "它有四大支柱：规格规划、测试驱动实现、渐进式披露文档，以及 AI 开发环境。"
    "工作以用户故事、史诗、缺陷或功能需求的形式进入。"
    "它经过三个阶段：规划、实现和发布。"
    "主导 AI 执行整个工作流。验证 AI 独立检查关键转换——"
    "它是来自不同训练谱系的第二个 AI。"
    "为什么需要两个 AI？因为单一 AI 会以自己看不到的方式犯下自信满满的错误。"
    "让同一个模型审查自己的输出，几乎不会发现这些错误。"
    "两个独立的谱系能捕捉到不同的问题。"
    "规划阶段产出规格说明。实现阶段产出可运行的代码、测试和更新后的文档。"
    "这些交付物通过发布阶段——CI 门禁加上人工审批。"
)


def generate_audio(text, output_path, label, voice_id=VOICE_A):
    """Call ElevenLabs API and save audio."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8,
            "style": 0.15,
        },
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )

    print(f"Generating {label}...")
    with urllib.request.urlopen(req) as resp:
        audio_bytes = resp.read()

    with open(output_path, "wb") as f:
        f.write(audio_bytes)

    size_kb = len(audio_bytes) / 1024
    print(f"  Saved: {output_path} ({size_kb:.0f} KB)")


def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)

    generate_audio(EN_TEXT, os.path.join(AUDIO_DIR, "sample-en.mp3"), "English (voice A)", VOICE_A)
    generate_audio(ZH_TEXT, os.path.join(AUDIO_DIR, "sample-zh-a.mp3"), "Chinese voice A", VOICE_A)
    generate_audio(ZH_TEXT, os.path.join(AUDIO_DIR, "sample-zh-b.mp3"), "Chinese voice B", VOICE_B)

    print("\nDone! Three samples:")
    print(f"  1. English voice A: {os.path.join(AUDIO_DIR, 'sample-en.mp3')}")
    print(f"  2. Chinese voice A: {os.path.join(AUDIO_DIR, 'sample-zh-a.mp3')}")
    print(f"  3. Chinese voice B: {os.path.join(AUDIO_DIR, 'sample-zh-b.mp3')}")


if __name__ == "__main__":
    main()
