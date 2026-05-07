Title: Architecture

Description: Understanding Voicebox's technical architecture

Source: https://docs.voicebox.sh/developer/architecture

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

Understanding Voicebox's technical architecture

## [System Overview](https://docs.voicebox.sh/developer/architecture#system-overview)
[System Overview](https://docs.voicebox.sh/developer/architecture#system-overview)
Voicebox uses a client-server architecture with a React frontend and Python backend. The desktop app is built with Tauri and contains two main layers:
Frontend Layer: A React application that handles the UI components, state management with Zustand, and data fetching with React Query (TanStack Query).
Backend Layer: A Python FastAPI server that hosts the REST API, runs a pluggable registry of TTS and STT engines, manages the SQLite database, and handles audio processing.
These two layers communicate via HTTP on localhost:17493, with the frontend making API requests to the backend. In production the backend is compiled with PyInstaller and launched as a Tauri sidecar; in development it's run manually via uvicorn.

```
localhost:17493
```


```
uvicorn
```

## [Frontend Architecture](https://docs.voicebox.sh/developer/architecture#frontend-architecture)
[Frontend Architecture](https://docs.voicebox.sh/developer/architecture#frontend-architecture)

### [Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack)
[Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack)
- Framework: React 18 with TypeScript
- State Management: Zustand stores
- Data Fetching: React Query (TanStack Query)
- Styling: Tailwind CSS
- Audio: WaveSurfer.js
- Desktop: Tauri (Rust)

### [Component Structure](https://docs.voicebox.sh/developer/architecture#component-structure)
[Component Structure](https://docs.voicebox.sh/developer/architecture#component-structure)

[Backend Architecture](https://docs.voicebox.sh/developer/architecture#backend-architecture)

### [Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack-1)
[Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack-1)
- Framework: FastAPI (Python 3.11+)
- TTS Engines: Qwen3-TTS, Qwen CustomVoice, LuxTTS, Chatterbox, Chatterbox Turbo, TADA, Kokoro
- Transcription: Whisper (PyTorch or MLX-Whisper)
- Inference Backends: MLX (Apple Silicon), PyTorch (CUDA / ROCm / XPU / DirectML / CPU)
- Database: SQLite via SQLAlchemy
- Audio: librosa, soundfile, Pedalboard

### [Layout](https://docs.voicebox.sh/developer/architecture#layout)
[Layout](https://docs.voicebox.sh/developer/architecture#layout)

### [Request Flow](https://docs.voicebox.sh/developer/architecture#request-flow)
[Request Flow](https://docs.voicebox.sh/developer/architecture#request-flow)
An HTTP request enters a route handler, which validates input and delegates to a service function. The service calls into the appropriate engine backend via the registry, which runs the actual inference. Audio post-processing runs through utils (trim, resample, effects).
Route handlers are intentionally thin — they validate input, delegate to a service function, and format the response. All business logic lives in services/.

```
services/
```

### [Multi-Engine Registry](https://docs.voicebox.sh/developer/architecture#multi-engine-registry)
[Multi-Engine Registry](https://docs.voicebox.sh/developer/architecture#multi-engine-registry)
The backend is designed so that adding a new TTS engine only requires touching the backends/ directory and the central registry. There is no per-engine branching in routes or services.

```
backends/
```

- TTSBackend Protocol (backends/__init__.py) — defines the contract every engine implements: load_model, create_voice_prompt, combine_voice_prompts, generate, unload_model, is_loaded, _get_model_path.
- ModelConfig dataclass — central metadata record for each model variant: model_name, display_name, engine, hf_repo_id, size_mb, needs_trim, languages, supports_instruct, etc.
- TTS_ENGINES dict — maps engine name ("qwen", "kokoro", etc.) to display name.
- get_tts_backend_for_engine(engine) — thread-safe factory that lazily instantiates and caches the backend for an engine using double-checked locking.

```
TTSBackend
```


```
backends/__init__.py
```


```
load_model
```


```
create_voice_prompt
```


```
combine_voice_prompts
```


```
generate
```


```
unload_model
```


```
is_loaded
```


```
_get_model_path
```


```
ModelConfig
```


```
model_name
```


```
display_name
```


```
engine
```


```
hf_repo_id
```


```
size_mb
```


```
needs_trim
```


```
languages
```


```
supports_instruct
```


```
TTS_ENGINES
```


```
"qwen"
```


```
"kokoro"
```


```
get_tts_backend_for_engine(engine)
```

Shipped engines:

```
qwen
```


```
qwen_custom_voice
```


```
luxtts
```


```
chatterbox
```


```
chatterbox_turbo
```


```
tada
```


```
kokoro
```

See [TTS Engines](https://docs.voicebox.sh/developer/tts-engines) for the full contract and integration phases, and [PROJECT_STATUS.md](https://github.com/jamiepine/voicebox/blob/main/docs/PROJECT_STATUS.md) for candidates under evaluation.

### [Key Modules](https://docs.voicebox.sh/developer/architecture#key-modules)
[Key Modules](https://docs.voicebox.sh/developer/architecture#key-modules)
- app.py — FastAPI app factory, CORS, lifecycle events
- main.py — Entry point (imports app, runs uvicorn)
- server.py — Tauri sidecar launcher, parent-pid watchdog, frozen-build environment setup
- services/generation.py — Single function handling all generation modes (generate, retry, regenerate)
- services/task_queue.py — Serial generation queue for GPU inference
- backends/__init__.py — Protocol definitions, ModelConfig registry, and engine factory
- backends/base.py — Shared utilities across all engine implementations (device selection, progress tracking, output trimming)

```
app.py
```


```
main.py
```


```
server.py
```


```
services/generation.py
```


```
services/task_queue.py
```


```
backends/__init__.py
```


```
ModelConfig
```


```
backends/base.py
```

### [Inference Backend Selection](https://docs.voicebox.sh/developer/architecture#inference-backend-selection)
[Inference Backend Selection](https://docs.voicebox.sh/developer/architecture#inference-backend-selection)
The server detects the best inference backend at startup and uses it for all engines that support it:
See [GPU Acceleration](https://docs.voicebox.sh/overview/gpu-acceleration) for platform-specific notes and manual overrides.

[Data Model](https://docs.voicebox.sh/developer/architecture#data-model)
Core tables (see backend/database/models.py):

```
backend/database/models.py
```

- profiles — Voice profiles with voice_type discriminator (cloned | preset | designed), preset_engine, preset_voice_id, and default_engine.
- profile_samples — Reference audio clips + transcripts for cloned profiles. Empty for preset profiles.
- generations — Generated audio with text, engine, model, language, seed, and duration.
- generation_versions — Processed variants of a generation with different effects chains applied.
- audio_channels + channel_device_mappings + profile_channel_mappings — Multi-output routing.

```
profiles
```


```
voice_type
```


```
cloned
```


```
preset
```


```
designed
```


```
preset_engine
```


```
preset_voice_id
```


```
default_engine
```


```
profile_samples
```


```
generations
```


```
generation_versions
```


```
audio_channels
```


```
channel_device_mappings
```


```
profile_channel_mappings
```

See [Voice Profiles](https://docs.voicebox.sh/developer/voice-profiles) and [Effects Pipeline](https://docs.voicebox.sh/developer/effects-pipeline) for details.

[Desktop App (Tauri)](https://docs.voicebox.sh/developer/architecture#desktop-app-tauri)

### [Rust Backend](https://docs.voicebox.sh/developer/architecture#rust-backend)
[Rust Backend](https://docs.voicebox.sh/developer/architecture#rust-backend)

### [Responsibilities](https://docs.voicebox.sh/developer/architecture#responsibilities)
[Responsibilities](https://docs.voicebox.sh/developer/architecture#responsibilities)
- Launch Python backend as sidecar process
- Native file dialogs
- System tray integration
- Auto-updates (Tauri updater + custom CUDA backend swap)
- Parent-PID watchdog so the backend exits if the app crashes

[Build Process](https://docs.voicebox.sh/developer/architecture#build-process)

### [Development](https://docs.voicebox.sh/developer/architecture#development)
[Development](https://docs.voicebox.sh/developer/architecture#development)

```
just dev # Starts backend + Tauri app just dev-web # Starts backend + web app (no Tauri) just dev-backend # Backend only just dev-frontend # Tauri app only (backend must be running)
```


```
just dev # Starts backend + Tauri app just dev-web # Starts backend + web app (no Tauri) just dev-backend # Backend only just dev-frontend # Tauri app only (backend must be running)
```

### [Production](https://docs.voicebox.sh/developer/architecture#production)
[Production](https://docs.voicebox.sh/developer/architecture#production)

```
just build # CPU server binary + Tauri installer just build-local # CPU + CUDA binaries + Tauri installer (Windows) just build-server # Server binary only just build-tauri # Tauri app only
```


```
just build # CPU server binary + Tauri installer just build-local # CPU + CUDA binaries + Tauri installer (Windows) just build-server # Server binary only just build-tauri # Tauri app only
```

See [Building](https://docs.voicebox.sh/developer/building) for what PyInstaller does and how the CUDA binary is split and packaged separately.

[Data Flow](https://docs.voicebox.sh/developer/architecture#data-flow)

[Generation Flow](https://docs.voicebox.sh/developer/architecture#generation-flow)
1. User Input — text entered in a React component, engine + profile selected
2. State Update — Zustand generation form store records the request
3. API Request — React Query mutation hits POST /generate
4. Route — routes/generate.py validates input, dispatches to services/generation.py
5. Voice Prompt — the service creates or retrieves a cached voice prompt via the engine's backend
6. Queue — services/task_queue.py serializes generation to avoid GPU contention
7. Inference — the engine backend runs generate() and returns audio + sample rate
8. Post-process — optional trim (for engines that need it), effects chain applied per generation version
9. Storage — audio written to the generations directory, metadata saved to SQLite
10. Response — backend returns the generation record; frontend updates React Query cache and plays audio

```
POST /generate
```


```
routes/generate.py
```


```
services/generation.py
```


```
services/task_queue.py
```


```
generate()
```

[Performance Considerations](https://docs.voicebox.sh/developer/architecture#performance-considerations)

### [Frontend](https://docs.voicebox.sh/developer/architecture#frontend)
[Frontend](https://docs.voicebox.sh/developer/architecture#frontend)
- Code splitting — lazy-load routes
- Memoization — React.memo for heavy components
- Virtual scrolling — for large lists
- Debouncing — search and input handling

```
React.memo
```

### [Backend](https://docs.voicebox.sh/developer/architecture#backend)
[Backend](https://docs.voicebox.sh/developer/architecture#backend)
- Async I/O — all I/O is async; inference runs in asyncio.to_thread
- Serial task queue — avoids multiple engines fighting for the GPU
- Voice prompt caching — engine-specific, keyed by audio hash + reference text
- Model pinning — only one model per engine loaded at a time; switching unloads the previous one
- Per-engine backend cache — engines are only instantiated once per process

```
asyncio.to_thread
```

[Security](https://docs.voicebox.sh/developer/architecture#security)

### [Current](https://docs.voicebox.sh/developer/architecture#current)
[Current](https://docs.voicebox.sh/developer/architecture#current)
- Local-only by default (bound to 127.0.0.1:17493)
- No authentication (localhost trust)
- File system sandboxing via Tauri

```
127.0.0.1:17493
```

### [Planned](https://docs.voicebox.sh/developer/architecture#planned)
[Planned](https://docs.voicebox.sh/developer/architecture#planned)
- API key authentication for remote mode
- User accounts
- Rate limiting
- HTTPS support

[Deployment Modes](https://docs.voicebox.sh/developer/architecture#deployment-modes)

### [Local Mode](https://docs.voicebox.sh/developer/architecture#local-mode)
[Local Mode](https://docs.voicebox.sh/developer/architecture#local-mode)
- Backend runs as sidecar
- All data stays on device
- No network required

### [Remote Mode](https://docs.voicebox.sh/developer/architecture#remote-mode)
[Remote Mode](https://docs.voicebox.sh/developer/architecture#remote-mode)
- Backend on a separate machine (Docker or bare host)
- Frontend (desktop or web) connects over HTTP
- See [Remote Mode](https://docs.voicebox.sh/overview/remote-mode) and [Docker](https://docs.voicebox.sh/overview/docker)
[Remote Mode](https://docs.voicebox.sh/overview/remote-mode)
[Docker](https://docs.voicebox.sh/overview/docker)

[Next Steps](https://docs.voicebox.sh/developer/architecture#next-steps)
[Development SetupSet up your dev environment](https://docs.voicebox.sh/developer/setup)

### Development Setup
Set up your dev environment
[TTS EnginesHow to add a new engine](https://docs.voicebox.sh/developer/tts-engines)

### TTS Engines
How to add a new engine
[ContributingContribute to Voicebox](https://docs.voicebox.sh/developer/contributing)

### Contributing
Contribute to Voicebox
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/developer/architecture.mdx)
[Development SetupSet up your local development environment for Voicebox](https://docs.voicebox.sh/developer/setup)
Development Setup
Set up your local development environment for Voicebox
[ContributingHow to contribute to Voicebox](https://docs.voicebox.sh/developer/contributing)
Contributing
How to contribute to Voicebox

### On this page
[System Overview](https://docs.voicebox.sh/developer/architecture#system-overview)
[Frontend Architecture](https://docs.voicebox.sh/developer/architecture#frontend-architecture)
[Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack)
[Component Structure](https://docs.voicebox.sh/developer/architecture#component-structure)
[Backend Architecture](https://docs.voicebox.sh/developer/architecture#backend-architecture)
[Tech Stack](https://docs.voicebox.sh/developer/architecture#tech-stack-1)
[Layout](https://docs.voicebox.sh/developer/architecture#layout)
[Request Flow](https://docs.voicebox.sh/developer/architecture#request-flow)
[Multi-Engine Registry](https://docs.voicebox.sh/developer/architecture#multi-engine-registry)
[Key Modules](https://docs.voicebox.sh/developer/architecture#key-modules)
[Inference Backend Selection](https://docs.voicebox.sh/developer/architecture#inference-backend-selection)
[Data Model](https://docs.voicebox.sh/developer/architecture#data-model)
[Desktop App (Tauri)](https://docs.voicebox.sh/developer/architecture#desktop-app-tauri)
[Rust Backend](https://docs.voicebox.sh/developer/architecture#rust-backend)
[Responsibilities](https://docs.voicebox.sh/developer/architecture#responsibilities)
[Build Process](https://docs.voicebox.sh/developer/architecture#build-process)
[Development](https://docs.voicebox.sh/developer/architecture#development)
[Production](https://docs.voicebox.sh/developer/architecture#production)
[Data Flow](https://docs.voicebox.sh/developer/architecture#data-flow)
[Generation Flow](https://docs.voicebox.sh/developer/architecture#generation-flow)
[Performance Considerations](https://docs.voicebox.sh/developer/architecture#performance-considerations)
[Frontend](https://docs.voicebox.sh/developer/architecture#frontend)
[Backend](https://docs.voicebox.sh/developer/architecture#backend)
[Security](https://docs.voicebox.sh/developer/architecture#security)
[Current](https://docs.voicebox.sh/developer/architecture#current)
[Planned](https://docs.voicebox.sh/developer/architecture#planned)
[Deployment Modes](https://docs.voicebox.sh/developer/architecture#deployment-modes)
[Local Mode](https://docs.voicebox.sh/developer/architecture#local-mode)
[Remote Mode](https://docs.voicebox.sh/developer/architecture#remote-mode)
[Next Steps](https://docs.voicebox.sh/developer/architecture#next-steps)

