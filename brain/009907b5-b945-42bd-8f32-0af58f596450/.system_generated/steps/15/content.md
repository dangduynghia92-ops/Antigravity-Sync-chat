Title: Installation

Description: Download and install Voicebox on macOS, Windows, or Linux

Source: https://docs.voicebox.sh/overview/installation

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

Download and install Voicebox on macOS, Windows, or Linux

[Download](https://docs.voicebox.sh/overview/installation#download)
Voicebox is available for macOS and Windows, with Linux builds coming soon.

### macOS
Download for Apple Silicon or Intel Macs

### Windows
Download MSI installer or Setup executable

### [macOS](https://docs.voicebox.sh/overview/installation#macos)
[macOS](https://docs.voicebox.sh/overview/installation#macos)
Download: [voicebox_aarch64.app.tar.gz](https://github.com/jamiepine/voicebox/releases/latest/download/voicebox_aarch64.app.tar.gz)

```
# Extract the archive tar -xzf voicebox_aarch64.app.tar.gz # Move to Applications mv Voicebox.app /Applications/
```


```
# Extract the archive tar -xzf voicebox_aarch64.app.tar.gz # Move to Applications mv Voicebox.app /Applications/
```

Download: [voicebox_x64.app.tar.gz](https://github.com/jamiepine/voicebox/releases/latest/download/voicebox_x64.app.tar.gz)

```
# Extract the archive tar -xzf voicebox_x64.app.tar.gz # Move to Applications mv Voicebox.app /Applications/
```


```
# Extract the archive tar -xzf voicebox_x64.app.tar.gz # Move to Applications mv Voicebox.app /Applications/
```

### [Windows](https://docs.voicebox.sh/overview/installation#windows)
[Windows](https://docs.voicebox.sh/overview/installation#windows)
Download: [voicebox_x64_en-US.msi](https://github.com/jamiepine/voicebox/releases/latest/download/voicebox_x64_en-US.msi)
Double-click the MSI file and follow the installation wizard.
Download: [voicebox_x64-setup.exe](https://github.com/jamiepine/voicebox/releases/latest/download/voicebox_x64-setup.exe)
Run the executable and follow the installation wizard.

### [Linux](https://docs.voicebox.sh/overview/installation#linux)
[Linux](https://docs.voicebox.sh/overview/installation#linux)
Linux builds are coming soon. Currently blocked by GitHub runner disk space limitations.

## [First Launch](https://docs.voicebox.sh/overview/installation#first-launch)
[First Launch](https://docs.voicebox.sh/overview/installation#first-launch)
When you launch Voicebox for the first time:
1. 
Model Download — The TTS engine you generate with first will download its model automatically. Sizes range from ~350 MB (Kokoro) to ~8 GB (TADA 3B). Most users start with Qwen 1.7B (~3.5 GB).

2. 
Data Directory — Voice profiles and generated audio are stored in:

macOS: ~/Library/Application Support/sh.voicebox.app/
Windows: %APPDATA%/sh.voicebox.app/
Linux: ~/.config/sh.voicebox.app/


3. macOS: ~/Library/Application Support/sh.voicebox.app/
4. Windows: %APPDATA%/sh.voicebox.app/
5. Linux: ~/.config/sh.voicebox.app/
6. 
Backend Server — The bundled Python server starts automatically

Model Download — The TTS engine you generate with first will download its model automatically. Sizes range from ~350 MB (Kokoro) to ~8 GB (TADA 3B). Most users start with Qwen 1.7B (~3.5 GB).
Data Directory — Voice profiles and generated audio are stored in:
- macOS: ~/Library/Application Support/sh.voicebox.app/
- Windows: %APPDATA%/sh.voicebox.app/
- Linux: ~/.config/sh.voicebox.app/

```
~/Library/Application Support/sh.voicebox.app/
```


```
%APPDATA%/sh.voicebox.app/
```


```
~/.config/sh.voicebox.app/
```

Backend Server — The bundled Python server starts automatically
First generation will be slower due to model downloads. Subsequent runs use cached models.

## [System Requirements](https://docs.voicebox.sh/overview/installation#system-requirements)
[System Requirements](https://docs.voicebox.sh/overview/installation#system-requirements)

### [Minimum](https://docs.voicebox.sh/overview/installation#minimum)
[Minimum](https://docs.voicebox.sh/overview/installation#minimum)
- OS: macOS 11+, Windows 10+, or Linux
- RAM: 8GB
- Storage: 5GB free space (for models and data)
- CPU: Modern multi-core processor

### [Recommended](https://docs.voicebox.sh/overview/installation#recommended)
[Recommended](https://docs.voicebox.sh/overview/installation#recommended)
- RAM: 16GB+
- GPU: CUDA-capable NVIDIA GPU (for faster generation)
- Storage: 10GB+ free space
CPU inference is supported but significantly slower than GPU. A CUDA-capable GPU is highly recommended for real-time workflows.

## [Verification](https://docs.voicebox.sh/overview/installation#verification)
[Verification](https://docs.voicebox.sh/overview/installation#verification)
After installation, verify everything works:
1. Launch Voicebox
2. Check the server status indicator in the bottom-left corner (should be green)
3. Navigate to Profiles and create a test profile
4. Generate a short audio clip to verify the TTS engine works
If you see a green status indicator and can generate audio, you're all set!

## [Next Steps](https://docs.voicebox.sh/overview/installation#next-steps)
[Next Steps](https://docs.voicebox.sh/overview/installation#next-steps)
[Quick Start GuideCreate your first voice profile and generate speech](https://docs.voicebox.sh/overview/quick-start)

### Quick Start Guide
Create your first voice profile and generate speech
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/installation.mdx)
[IntroductionVoicebox is the open-source, local-first AI voice studio — a free alternative to ElevenLabs and WisprFlow, running entirely on your machine.](https://docs.voicebox.sh/overview/introduction)
Introduction
Voicebox is the open-source, local-first AI voice studio — a free alternative to ElevenLabs and WisprFlow, running entirely on your machine.
[Docker DeploymentRun Voicebox as a headless server with a web UI using Docker](https://docs.voicebox.sh/overview/docker)
Docker Deployment
Run Voicebox as a headless server with a web UI using Docker

### On this page
[Download](https://docs.voicebox.sh/overview/installation#download)
[macOS](https://docs.voicebox.sh/overview/installation#macos)
[Windows](https://docs.voicebox.sh/overview/installation#windows)
[Linux](https://docs.voicebox.sh/overview/installation#linux)
[First Launch](https://docs.voicebox.sh/overview/installation#first-launch)
[System Requirements](https://docs.voicebox.sh/overview/installation#system-requirements)
[Minimum](https://docs.voicebox.sh/overview/installation#minimum)
[Recommended](https://docs.voicebox.sh/overview/installation#recommended)
[Verification](https://docs.voicebox.sh/overview/installation#verification)
[Next Steps](https://docs.voicebox.sh/overview/installation#next-steps)

