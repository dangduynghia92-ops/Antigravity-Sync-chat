Title: Introduction

Description: Voicebox is the open-source, local-first AI voice studio — a free alternative to ElevenLabs and WisprFlow, running entirely on your machine.

Source: https://docs.voicebox.sh/overview/introduction

---

[Voicebox](https://docs.voicebox.sh/)
[Voicebox](https://docs.voicebox.sh/)
[Introduction](https://docs.voicebox.sh/overview/introduction)
[Installation](https://docs.voicebox.sh/overview/installation)
[Docker Deployment](https://docs.voicebox.sh/overview/docker)
[Quick Start](https://docs.voicebox.sh/overview/quick-start)
[GPU Acceleration](https://docs.voicebox.sh/overview/gpu-acceleration)
[Dictation](https://docs.voicebox.sh/overview/dictation)
[Captures](https://docs.voicebox.sh/overview/captures)
[Voice Cloning](https://docs.voicebox.sh/overview/voice-cloning)
[Preset Voices](https://docs.voicebox.sh/overview/preset-voices)
[Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities)
[MCP Server](https://docs.voicebox.sh/overview/mcp-server)
[Stories Editor](https://docs.voicebox.sh/overview/stories-editor)
[Recording & Transcription](https://docs.voicebox.sh/overview/recording-transcription)
[Generation History](https://docs.voicebox.sh/overview/generation-history)
[Remote Mode](https://docs.voicebox.sh/overview/remote-mode)
[Creating Voice Profiles](https://docs.voicebox.sh/overview/creating-voice-profiles)
[Generating Speech](https://docs.voicebox.sh/overview/generating-speech)
[Building Stories](https://docs.voicebox.sh/overview/building-stories)
[Troubleshooting](https://docs.voicebox.sh/overview/troubleshooting)
[Development Setup](https://docs.voicebox.sh/developer/setup)
[Architecture](https://docs.voicebox.sh/developer/architecture)
[Contributing](https://docs.voicebox.sh/developer/contributing)
[Building](https://docs.voicebox.sh/developer/building)
[Auto-Updater](https://docs.voicebox.sh/developer/autoupdater)
[Voice Profiles](https://docs.voicebox.sh/developer/voice-profiles)
[TTS Generation](https://docs.voicebox.sh/developer/tts-generation)
[TTS Engines](https://docs.voicebox.sh/developer/tts-engines)
[Effects Pipeline](https://docs.voicebox.sh/developer/effects-pipeline)
[Generation History](https://docs.voicebox.sh/developer/history)
[Stories & Timeline](https://docs.voicebox.sh/developer/stories)
[Transcription](https://docs.voicebox.sh/developer/transcription)
[Audio Channels](https://docs.voicebox.sh/developer/audio-channels)
[Model Management](https://docs.voicebox.sh/developer/model-management)

Voicebox is the open-source, local-first AI voice studio — a free alternative to ElevenLabs and WisprFlow, running entirely on your machine.

## [What is Voicebox?](https://docs.voicebox.sh/overview/introduction#what-is-voicebox)
[What is Voicebox?](https://docs.voicebox.sh/overview/introduction#what-is-voicebox)
Voicebox is the open-source, local-first AI voice studio. It closes the voice I/O loop in both directions on one machine, with no cloud and no accounts:
- Humans talk — hold a chord anywhere on your machine and your
dictation lands as clean text in whatever text field you had focused
- Agents talk back — any MCP-aware agent can call Voicebox to speak in
one of your cloned voices
- Voices speak for themselves — voice profiles can carry a personality
that composes fresh lines or rewrites text before it's spoken
It's the free, local alternative to both ElevenLabs (voice cloning and TTS) and WisprFlow (voice dictation for agents and power users) — covering both sides of the same loop in one app, with a single model directory and LLM shared between input and output.

## [What's in the app](https://docs.voicebox.sh/overview/introduction#whats-in-the-app)
[What's in the app](https://docs.voicebox.sh/overview/introduction#whats-in-the-app)
- [Dictation](https://docs.voicebox.sh/overview/dictation) — global hotkey, push-to-talk and toggle modes, auto-paste
into the focused field on macOS and Windows (see Dictation)
- [Captures](https://docs.voicebox.sh/overview/captures) tab — paired audio + transcript archive, retranscribe,
refine, play-as-voice, promote-to-sample (see Captures)
- Voice cloning — 5 cloning engines covering 23 languages. Zero-shot
cloning from a reference sample (see [Voice Cloning](https://docs.voicebox.sh/overview/voice-cloning))
- Preset voices — 50+ curated voices via Kokoro and Qwen CustomVoice
for when you don't want to clone (see [Preset Voices](https://docs.voicebox.sh/overview/preset-voices))
- Voice personalities — optional free-form personality on any profile
plus a compose button and persona-rewrite toggle powered by a local LLM (see
[Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities))
- Post-processing effects — pitch shift, reverb, delay, chorus,
compression, filters (Spotify's Pedalboard)
- Expressive speech — paralinguistic tags like [laugh] and [sigh]
via Chatterbox Turbo; natural-language delivery control via Qwen CustomVoice
- Unlimited length — auto-chunking with crossfade for long scripts
- Stories editor — multi-track timeline for conversations and podcasts
- API-first — REST + WebSocket API; MCP server for agent integrations
- Runs everywhere — macOS (MLX/Metal), Windows (CUDA / DirectML), Linux
(ROCm / CPU), Intel Arc, Docker
[Dictation](https://docs.voicebox.sh/overview/dictation)
[Captures](https://docs.voicebox.sh/overview/captures)
[Voice Cloning](https://docs.voicebox.sh/overview/voice-cloning)
[Preset Voices](https://docs.voicebox.sh/overview/preset-voices)
[Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities)

```
[laugh]
```


```
[sigh]
```

## [TTS Engines](https://docs.voicebox.sh/overview/introduction#tts-engines)
[TTS Engines](https://docs.voicebox.sh/overview/introduction#tts-engines)
Seven engines with different strengths, switchable per-generation:

## [STT and local LLM](https://docs.voicebox.sh/overview/introduction#stt-and-local-llm)
[STT and local LLM](https://docs.voicebox.sh/overview/introduction#stt-and-local-llm)
Voicebox also runs a full speech recognition and local LLM stack, shared between dictation, the Captures tab, and per-profile personality modes:
No cloud fallback, no bring-your-own-API-key. Local is the product.

## [GPU Support](https://docs.voicebox.sh/overview/introduction#gpu-support)
[GPU Support](https://docs.voicebox.sh/overview/introduction#gpu-support)

## [Use Cases](https://docs.voicebox.sh/overview/introduction#use-cases)
[Use Cases](https://docs.voicebox.sh/overview/introduction#use-cases)
- Dictation for humans and agents — speak instead of type, in any app
- Agent voice output — any MCP-aware agent can speak in a cloned voice
- Game development — generate dynamic dialogue for characters
- Content creation — podcasts, video voiceovers, audiobooks
- Accessibility — speech-to-text for any field, TTS with a voice you own
- Voice assistants — custom voice interfaces without a cloud bill
- Production pipelines — automate voice workflows via the REST API

[Tech Stack](https://docs.voicebox.sh/overview/introduction#tech-stack)
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/introduction.mdx)
[InstallationDownload and install Voicebox on macOS, Windows, or Linux](https://docs.voicebox.sh/overview/installation)
Installation
Download and install Voicebox on macOS, Windows, or Linux

[What is Voicebox?](https://docs.voicebox.sh/overview/introduction#what-is-voicebox)
[What's in the app](https://docs.voicebox.sh/overview/introduction#whats-in-the-app)
[TTS Engines](https://docs.voicebox.sh/overview/introduction#tts-engines)
[STT and local LLM](https://docs.voicebox.sh/overview/introduction#stt-and-local-llm)
[GPU Support](https://docs.voicebox.sh/overview/introduction#gpu-support)
[Use Cases](https://docs.voicebox.sh/overview/introduction#use-cases)
[Tech Stack](https://docs.voicebox.sh/overview/introduction#tech-stack)

