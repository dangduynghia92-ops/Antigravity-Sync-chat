Title: GPU Acceleration

Description: How Voicebox uses your GPU — auto-detection, manual setup, troubleshooting

Source: https://docs.voicebox.sh/overview/gpu-acceleration

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

How Voicebox uses your GPU — auto-detection, manual setup, troubleshooting

## [Overview](https://docs.voicebox.sh/overview/gpu-acceleration#overview)
[Overview](https://docs.voicebox.sh/overview/gpu-acceleration#overview)
Voicebox auto-detects available accelerators on first launch and picks the fastest backend it can use. For most people this just works — open the app and you're already on the right backend.
This page is for the cases where it doesn't:
- You have a GPU but Voicebox is running on CPU
- You upgraded GPUs (especially to RTX 50-series / Blackwell) and generation broke
- You want to switch backends manually (e.g. force MLX over PyTorch on Apple Silicon)
- You see [UNSUPPORTED - see logs] next to your GPU in Settings

```
[UNSUPPORTED - see logs]
```

## [Backend Matrix](https://docs.voicebox.sh/overview/gpu-acceleration#backend-matrix)
[Backend Matrix](https://docs.voicebox.sh/overview/gpu-acceleration#backend-matrix)

```
HSA_OVERRIDE_GFX_VERSION
```

The detected backend is shown in Settings → GPU. Logs at startup also print the chosen backend and the device name.

## [Apple Silicon — MLX vs PyTorch](https://docs.voicebox.sh/overview/gpu-acceleration#apple-silicon--mlx-vs-pytorch)
[Apple Silicon — MLX vs PyTorch](https://docs.voicebox.sh/overview/gpu-acceleration#apple-silicon--mlx-vs-pytorch)
On M-series Macs, Voicebox ships an MLX-optimized backend that uses the Apple Neural Engine. It's 4-5x faster than the PyTorch (CPU/Metal) path for supported engines.

```
PYTORCH_ENABLE_MPS_FALLBACK=1
```

The Whisper Turbo + MLX combo dropped transcription latency from ~20s to ~2-3s on M-series chips (see CHANGELOG entry for v0.1.10).

## [Windows / Linux + NVIDIA — The CUDA Backend Swap](https://docs.voicebox.sh/overview/gpu-acceleration#windows--linux--nvidia--the-cuda-backend-swap)
[Windows / Linux + NVIDIA — The CUDA Backend Swap](https://docs.voicebox.sh/overview/gpu-acceleration#windows--linux--nvidia--the-cuda-backend-swap)
Voicebox doesn't bundle CUDA into the main installer (it would balloon downloads to multi-gigabyte territory for users who don't have an NVIDIA GPU). Instead, when you first need it, the app downloads a separate CUDA backend binary that contains the PyTorch + CUDA runtime.
If an NVIDIA GPU is detected, you'll see "Install CUDA backend" in the GPU panel
The app downloads two archives separately:
- Server core (~200-400 MB) — versioned with each Voicebox release
- CUDA libs (~4 GB) — the heavy PyTorch + CUDA DLLs, versioned independently
Voicebox restarts to swap in the CUDA backend
The split-archive design (added in v0.4) means most Voicebox upgrades only redownload the small server-core archive. The 4 GB libs archive is only refreshed when the underlying CUDA toolkit or torch major version changes.

[Auto-update](https://docs.voicebox.sh/overview/gpu-acceleration#auto-update)
When a new Voicebox release ships, the GPU panel checks if the bundled server-core matches the installed CUDA version. If only the core changed (typical), it pulls the new core in the background. If the libs version changed (rare — only happens on cu126 → cu128 type bumps), you'll be prompted to confirm the larger download.

## [RTX 50-series / Blackwell](https://docs.voicebox.sh/overview/gpu-acceleration#rtx-50-series--blackwell)
[RTX 50-series / Blackwell](https://docs.voicebox.sh/overview/gpu-acceleration#rtx-50-series--blackwell)
Voicebox 0.4 added explicit RTX 50-series support:
- CUDA toolkit upgraded to cu128 (previous releases used cu126 which lacks Blackwell kernels)
- Build pinned with TORCH_CUDA_ARCH_LIST=...12.0+PTX for forward-compatibility

```
TORCH_CUDA_ARCH_LIST=...12.0+PTX
```

If you're on an RTX 5070 / 5080 / 5090 and you see "no kernel image is available" errors:
1. Make sure you're on Voicebox ≥ 0.4.0 (Settings → About)
2. Reinstall the CUDA backend (Settings → GPU → Reinstall CUDA backend) — older installs may have stale cu126 libs
3. If errors persist, see the GPU compatibility warnings section below

## [Intel Arc (XPU)](https://docs.voicebox.sh/overview/gpu-acceleration#intel-arc-xpu)
[Intel Arc (XPU)](https://docs.voicebox.sh/overview/gpu-acceleration#intel-arc-xpu)
New in 0.4. Works with both Arc A-series (Alchemist: A380, A580, A750, A770) and B-series (Battlemage).

### [Setup](https://docs.voicebox.sh/overview/gpu-acceleration#setup)
[Setup](https://docs.voicebox.sh/overview/gpu-acceleration#setup)
Voicebox auto-detects Arc GPUs and routes through Intel's PyTorch XPU backend (powered by IPEX — Intel Extension for PyTorch). No extra installation step beyond the standard Voicebox install.
Verify it's working:
- Settings → GPU should show XPU followed by your Arc model name (e.g. XPU (Intel Arc A770))
- Startup logs print Backend: PYTORCH and GPU: XPU (Intel Arc ...)

```
XPU (Intel Arc A770)
```


```
Backend: PYTORCH
```


```
GPU: XPU (Intel Arc ...)
```

### [Engines on XPU](https://docs.voicebox.sh/overview/gpu-acceleration#engines-on-xpu)
[Engines on XPU](https://docs.voicebox.sh/overview/gpu-acceleration#engines-on-xpu)
All PyTorch-based engines work on XPU. Performance is generally between CPU and CUDA — expect ~2-3x speedup over CPU for the larger models.

## [DirectML](https://docs.voicebox.sh/overview/gpu-acceleration#directml)
[DirectML](https://docs.voicebox.sh/overview/gpu-acceleration#directml)
The fallback for Windows users with non-NVIDIA, non-Intel-Arc GPUs (older AMD discrete, integrated GPUs, etc.). Slower than CUDA and XPU but provides some acceleration over CPU.
Auto-selected when no other GPU backend is available.

## [AMD ROCm (Linux)](https://docs.voicebox.sh/overview/gpu-acceleration#amd-rocm-linux)
[AMD ROCm (Linux)](https://docs.voicebox.sh/overview/gpu-acceleration#amd-rocm-linux)
ROCm provides PyTorch GPU acceleration on AMD discrete GPUs. Voicebox auto-configures HSA_OVERRIDE_GFX_VERSION for common cards that need the override.

```
HSA_OVERRIDE_GFX_VERSION
```

[Verifying](https://docs.voicebox.sh/overview/gpu-acceleration#verifying)

```
# In a terminal echo $HSA_OVERRIDE_GFX_VERSION # Should show e.g. 10.3.0 for RX 6000 series
```


```
# In a terminal echo $HSA_OVERRIDE_GFX_VERSION # Should show e.g. 10.3.0 for RX 6000 series
```

If detection fails, set the variable manually before launching Voicebox:

```
export HSA_OVERRIDE_GFX_VERSION=10.3.0 voicebox
```


```
export HSA_OVERRIDE_GFX_VERSION=10.3.0 voicebox
```

Common values:
- 10.3.0 — RX 6000 series (RDNA 2)
- 11.0.0 — RX 7000 series (RDNA 3)
- 9.0.0 — Older Vega cards

```
10.3.0
```


```
11.0.0
```


```
9.0.0
```

[GPU Compatibility Warnings](https://docs.voicebox.sh/overview/gpu-acceleration#gpu-compatibility-warnings)
Voicebox 0.4 added a runtime check that compares your GPU's compute capability against the architectures the bundled PyTorch was compiled for. If they don't match, you'll see:
- A startup log line: WARNING: GPU COMPATIBILITY: <your GPU> is not supported by this PyTorch build...
- The GPU label in Settings shows [UNSUPPORTED - see logs]
- The /health API returns a populated gpu_compatibility_warning field

```
WARNING: GPU COMPATIBILITY: <your GPU> is not supported by this PyTorch build...
```


```
[UNSUPPORTED - see logs]
```


```
/health
```


```
gpu_compatibility_warning
```

[What to do](https://docs.voicebox.sh/overview/gpu-acceleration#what-to-do)
The most common trigger is a brand-new GPU architecture that pre-built PyTorch wheels don't yet cover natively. In order of preference:
1. Update Voicebox — newer releases ship newer PyTorch with broader arch support
2. Reinstall the CUDA backend — Settings → GPU → Reinstall CUDA backend
3. For bleeding-edge GPUs (newer than current Blackwell): install PyTorch nightly manually:
pip install torch --index-url https://download.pytorch.org/whl/nightly/cu128 --force-reinstall
Then point Voicebox at that environment via [Remote Mode](https://docs.voicebox.sh/overview/remote-mode) until stable PyTorch catches up.
4. Fall back to CPU temporarily — set VOICEBOX_FORCE_CPU=1 before launching

```
pip install torch --index-url https://download.pytorch.org/whl/nightly/cu128 --force-reinstall
```


```
pip install torch --index-url https://download.pytorch.org/whl/nightly/cu128 --force-reinstall
```

[Remote Mode](https://docs.voicebox.sh/overview/remote-mode)

```
VOICEBOX_FORCE_CPU=1
```

## [CPU-Only Fallback](https://docs.voicebox.sh/overview/gpu-acceleration#cpu-only-fallback)
[CPU-Only Fallback](https://docs.voicebox.sh/overview/gpu-acceleration#cpu-only-fallback)
When no GPU is available (or you've forced it off), Voicebox runs the PyTorch CPU backend. Expect:
- 5-50x slower generation depending on engine and text length
- Heavy CPU usage during generation
- Some engines work better than others on CPU:

Kokoro 82M — runs at realtime on modern CPUs
LuxTTS — exceeds 150x realtime on CPU
Chatterbox Turbo (350M) — usable but slow
Larger models (Qwen 1.7B, Chatterbox Multilingual, TADA 3B) — painful


- Kokoro 82M — runs at realtime on modern CPUs
- LuxTTS — exceeds 150x realtime on CPU
- Chatterbox Turbo (350M) — usable but slow
- Larger models (Qwen 1.7B, Chatterbox Multilingual, TADA 3B) — painful
- Kokoro 82M — runs at realtime on modern CPUs
- LuxTTS — exceeds 150x realtime on CPU
- Chatterbox Turbo (350M) — usable but slow
- Larger models (Qwen 1.7B, Chatterbox Multilingual, TADA 3B) — painful
For CPU-bound use cases, prefer the smaller, lighter engines.

## [Verifying Your Setup](https://docs.voicebox.sh/overview/gpu-acceleration#verifying-your-setup)
[Verifying Your Setup](https://docs.voicebox.sh/overview/gpu-acceleration#verifying-your-setup)
Three places to check that the right backend is being used:
Shows the detected backend, GPU model, and VRAM (when applicable). Look for the [UNSUPPORTED - see logs] suffix

```
[UNSUPPORTED - see logs]
```

The "Server logs" tab shows the startup banner with Backend: <type> and GPU: <name>

```
Backend: <type>
```


```
GPU: <name>
```

curl http://localhost:17493/health returns a JSON payload with backend_type, backend_variant, and gpu_compatibility_warning (when applicable)

```
curl http://localhost:17493/health
```


```
backend_type
```


```
backend_variant
```


```
gpu_compatibility_warning
```

## [Troubleshooting](https://docs.voicebox.sh/overview/gpu-acceleration#troubleshooting)
[Troubleshooting](https://docs.voicebox.sh/overview/gpu-acceleration#troubleshooting)
- On NVIDIA: install the CUDA backend (Settings → GPU)
- On Intel Arc: confirm IPEX detection in startup logs; restart the app after a driver update
- On AMD Linux: check HSA_OVERRIDE_GFX_VERSION is set

```
HSA_OVERRIDE_GFX_VERSION
```

Almost always means the bundled PyTorch doesn't have kernels for your GPU's compute capability.
1. Update to Voicebox ≥ 0.4.0 (Blackwell support added there)
2. Reinstall the CUDA backend
3. If still broken, install PyTorch nightly via Remote Mode
- Switch to a smaller model size (e.g. Qwen3 0.6B instead of 1.7B)
- Use Settings → Models to unload other engines you're not using
- Enable low_cpu_mem_usage is already on for CPU; for CUDA, the engine's device_map handles offload automatically
- Close other GPU applications

```
low_cpu_mem_usage
```


```
device_map
```

Some operations don't have a Metal implementation. Voicebox sets PYTORCH_ENABLE_MPS_FALLBACK=1 for engines that need it (notably Kokoro), but if you launch from a custom env, set it manually:

```
PYTORCH_ENABLE_MPS_FALLBACK=1
```


```
export PYTORCH_ENABLE_MPS_FALLBACK=1
```


```
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

- Check Settings → GPU shows your GPU (not CPU)
- Check VRAM usage — you may be paging to system memory
- Try a smaller model
- For NVIDIA: confirm cu128 is installed (Settings → GPU → version)

## [Next Steps](https://docs.voicebox.sh/overview/gpu-acceleration#next-steps)
[Next Steps](https://docs.voicebox.sh/overview/gpu-acceleration#next-steps)
[Remote ModeRun the backend on a different machine with a stronger GPU](https://docs.voicebox.sh/overview/remote-mode)

### Remote Mode
Run the backend on a different machine with a stronger GPU
[Model ManagementUnload models to free GPU memory](https://docs.voicebox.sh/developer/model-management)

### Model Management
Unload models to free GPU memory
[TroubleshootingGeneral troubleshooting beyond GPU](https://docs.voicebox.sh/overview/troubleshooting)

### Troubleshooting
General troubleshooting beyond GPU
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/gpu-acceleration.mdx)
[Quick StartGet started with Voicebox in 5 minutes](https://docs.voicebox.sh/overview/quick-start)
Quick Start
Get started with Voicebox in 5 minutes
[DictationHold a key anywhere on your machine, speak, release — the transcript lands in whatever text field you had focused.](https://docs.voicebox.sh/overview/dictation)
Dictation
Hold a key anywhere on your machine, speak, release — the transcript lands in whatever text field you had focused.

### On this page
[Overview](https://docs.voicebox.sh/overview/gpu-acceleration#overview)
[Backend Matrix](https://docs.voicebox.sh/overview/gpu-acceleration#backend-matrix)
[Apple Silicon — MLX vs PyTorch](https://docs.voicebox.sh/overview/gpu-acceleration#apple-silicon--mlx-vs-pytorch)
[Windows / Linux + NVIDIA — The CUDA Backend Swap](https://docs.voicebox.sh/overview/gpu-acceleration#windows--linux--nvidia--the-cuda-backend-swap)
[Auto-update](https://docs.voicebox.sh/overview/gpu-acceleration#auto-update)
[RTX 50-series / Blackwell](https://docs.voicebox.sh/overview/gpu-acceleration#rtx-50-series--blackwell)
[Intel Arc (XPU)](https://docs.voicebox.sh/overview/gpu-acceleration#intel-arc-xpu)
[Setup](https://docs.voicebox.sh/overview/gpu-acceleration#setup)
[Engines on XPU](https://docs.voicebox.sh/overview/gpu-acceleration#engines-on-xpu)
[DirectML](https://docs.voicebox.sh/overview/gpu-acceleration#directml)
[AMD ROCm (Linux)](https://docs.voicebox.sh/overview/gpu-acceleration#amd-rocm-linux)
[Verifying](https://docs.voicebox.sh/overview/gpu-acceleration#verifying)
[GPU Compatibility Warnings](https://docs.voicebox.sh/overview/gpu-acceleration#gpu-compatibility-warnings)
[What to do](https://docs.voicebox.sh/overview/gpu-acceleration#what-to-do)
[CPU-Only Fallback](https://docs.voicebox.sh/overview/gpu-acceleration#cpu-only-fallback)
[Verifying Your Setup](https://docs.voicebox.sh/overview/gpu-acceleration#verifying-your-setup)
[Troubleshooting](https://docs.voicebox.sh/overview/gpu-acceleration#troubleshooting)
[Next Steps](https://docs.voicebox.sh/overview/gpu-acceleration#next-steps)

