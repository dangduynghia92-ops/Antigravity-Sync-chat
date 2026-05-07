Title: Remote Mode

Description: Connect to a GPU server for faster generation

Source: https://docs.voicebox.sh/overview/remote-mode

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

Connect to a GPU server for faster generation

## [Overview](https://docs.voicebox.sh/overview/remote-mode#overview)
[Overview](https://docs.voicebox.sh/overview/remote-mode#overview)
Remote Mode allows you to run the Voicebox backend on a separate machine (like a GPU server) while using the desktop app on your local machine.

## [Use Cases](https://docs.voicebox.sh/overview/remote-mode#use-cases)
[Use Cases](https://docs.voicebox.sh/overview/remote-mode#use-cases)
- No local GPU - Use a cloud GPU or remote workstation
- Faster generation - Leverage powerful remote hardware
- Shared infrastructure - Multiple users connect to one server
- Laptop workflows - Keep your laptop cool and battery-efficient

## [Architecture](https://docs.voicebox.sh/overview/remote-mode#architecture)
[Architecture](https://docs.voicebox.sh/overview/remote-mode#architecture)
In Remote Mode, the Voicebox desktop app (running on your local machine) communicates with the backend server (running on a remote machine) via HTTP. The local app provides only the user interface, while the remote server handles all the heavy processing including the TTS models, API endpoints, and audio generation.

## [Setting Up Remote Mode](https://docs.voicebox.sh/overview/remote-mode#setting-up-remote-mode)
[Setting Up Remote Mode](https://docs.voicebox.sh/overview/remote-mode#setting-up-remote-mode)

### [On the Server](https://docs.voicebox.sh/overview/remote-mode#on-the-server)
[On the Server](https://docs.voicebox.sh/overview/remote-mode#on-the-server)

```
# Clone the repo git clone https://github.com/jamiepine/voicebox.git cd voicebox/backend # Install Python dependencies pip install -r requirements.txt # Engines with incompatible transitive pins — install with --no-deps pip install --no-deps chatterbox-tts pip install --no-deps hume-tada # Qwen3-TTS from source pip install git+https://github.com/QwenLM/Qwen3-TTS.git
```


```
# Clone the repo git clone https://github.com/jamiepine/voicebox.git cd voicebox/backend # Install Python dependencies pip install -r requirements.txt # Engines with incompatible transitive pins — install with --no-deps pip install --no-deps chatterbox-tts pip install --no-deps hume-tada # Qwen3-TTS from source pip install git+https://github.com/QwenLM/Qwen3-TTS.git
```

Or just run just setup from the repo root, which handles all of this.

```
just setup
```


```
# Allow external connections uvicorn main:app --host 0.0.0.0 --port 17493
```


```
# Allow external connections uvicorn main:app --host 0.0.0.0 --port 17493
```

This exposes the server to your network. Use a firewall or VPN for security.

```
# Ubuntu/Debian sudo ufw allow 17493 # Or use your cloud provider's firewall settings
```


```
# Ubuntu/Debian sudo ufw allow 17493 # Or use your cloud provider's firewall settings
```

### [On the Client](https://docs.voicebox.sh/overview/remote-mode#on-the-client)
[On the Client](https://docs.voicebox.sh/overview/remote-mode#on-the-client)
In Voicebox, go to Settings → Server
Toggle Use Remote Server

```
http://<server-ip>:17493
```


```
http://<server-ip>:17493
```

Replace <server-ip> with your server's IP address

```
<server-ip>
```

Click Test Connection to verify

[Cloud Deployment](https://docs.voicebox.sh/overview/remote-mode#cloud-deployment)

### [AWS EC2](https://docs.voicebox.sh/overview/remote-mode#aws-ec2)
[AWS EC2](https://docs.voicebox.sh/overview/remote-mode#aws-ec2)

```
# Launch a GPU instance (e.g., g4dn.xlarge) # Install dependencies # Start server with --host 0.0.0.0
```


```
# Launch a GPU instance (e.g., g4dn.xlarge) # Install dependencies # Start server with --host 0.0.0.0
```

### [Vast.ai](https://docs.voicebox.sh/overview/remote-mode#vastai)
[Vast.ai](https://docs.voicebox.sh/overview/remote-mode#vastai)

```
# Rent a GPU instance # SSH in and clone repo # Start server
```


```
# Rent a GPU instance # SSH in and clone repo # Start server
```

### [RunPod](https://docs.voicebox.sh/overview/remote-mode#runpod)
[RunPod](https://docs.voicebox.sh/overview/remote-mode#runpod)

```
# Deploy a pod with CUDA support # Install Voicebox backend # Expose port 17493
```


```
# Deploy a pod with CUDA support # Install Voicebox backend # Expose port 17493
```

## [Security Considerations](https://docs.voicebox.sh/overview/remote-mode#security-considerations)
[Security Considerations](https://docs.voicebox.sh/overview/remote-mode#security-considerations)
The API currently has no authentication. Only use on trusted networks or with a VPN.
Best Practices:
- Use a VPN (WireGuard, Tailscale) instead of exposing to the internet
- Run behind a reverse proxy with authentication (nginx + basic auth)
- Use HTTPS with SSL certificates
- Firewall rules to limit access to specific IPs

## [Performance](https://docs.voicebox.sh/overview/remote-mode#performance)
[Performance](https://docs.voicebox.sh/overview/remote-mode#performance)
Expected performance on various GPUs:
A GPU with 8GB+ VRAM is recommended for best performance.

## [Troubleshooting](https://docs.voicebox.sh/overview/remote-mode#troubleshooting)
[Troubleshooting](https://docs.voicebox.sh/overview/remote-mode#troubleshooting)
See the [Troubleshooting Guide](https://docs.voicebox.sh/overview/troubleshooting) for common issues.
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/remote-mode.mdx)
[Generation HistoryTrack and manage all your generated audio](https://docs.voicebox.sh/overview/generation-history)
Generation History
Track and manage all your generated audio
[Creating Voice ProfilesHow to create voice profiles, both cloning-based and preset-based](https://docs.voicebox.sh/overview/creating-voice-profiles)
Creating Voice Profiles
How to create voice profiles, both cloning-based and preset-based

[Overview](https://docs.voicebox.sh/overview/remote-mode#overview)
[Use Cases](https://docs.voicebox.sh/overview/remote-mode#use-cases)
[Architecture](https://docs.voicebox.sh/overview/remote-mode#architecture)
[Setting Up Remote Mode](https://docs.voicebox.sh/overview/remote-mode#setting-up-remote-mode)
[On the Server](https://docs.voicebox.sh/overview/remote-mode#on-the-server)
[On the Client](https://docs.voicebox.sh/overview/remote-mode#on-the-client)
[Cloud Deployment](https://docs.voicebox.sh/overview/remote-mode#cloud-deployment)
[AWS EC2](https://docs.voicebox.sh/overview/remote-mode#aws-ec2)
[Vast.ai](https://docs.voicebox.sh/overview/remote-mode#vastai)
[RunPod](https://docs.voicebox.sh/overview/remote-mode#runpod)
[Security Considerations](https://docs.voicebox.sh/overview/remote-mode#security-considerations)
[Performance](https://docs.voicebox.sh/overview/remote-mode#performance)
[Troubleshooting](https://docs.voicebox.sh/overview/remote-mode#troubleshooting)

