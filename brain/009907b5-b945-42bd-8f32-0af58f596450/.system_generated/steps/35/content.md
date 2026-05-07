Title: TTS Engines

Description: How to add new text-to-speech engines to Voicebox

Source: https://docs.voicebox.sh/developer/tts-engines

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

How to add new text-to-speech engines to Voicebox
For humans: This doc is optimized for AI agents to implement new TTS engines autonomously. It's structured as a phased workflow with explicit gates and a checklist so an agent can do the full integration — dependency research, backend, frontend, bundling — and hand you a draft release or prod build to test locally. It's also a useful reference if you're doing it yourself.
Adding an engine touches ~10 files across 4 layers. The backend protocol work is straightforward — the real time sink is dependency hell, upstream library bugs, and PyInstaller bundling.
Do not start writing code until you complete Phase 0. The v0.2.3 release was three patch releases of PyInstaller fixes because dependency research was skipped. Every issue — inspect.getsource() failures, missing native data files, metadata lookups, dtype mismatches — was discoverable by reading the model library's source code before integration began.

```
inspect.getsource()
```

## [Architecture Overview](https://docs.voicebox.sh/developer/tts-engines#architecture-overview)
[Architecture Overview](https://docs.voicebox.sh/developer/tts-engines#architecture-overview)
The backend is split into layers:

```
routes/
```


```
services/
```


```
backends/
```


```
your_engine_backend.py
```


```
utils/
```

New engines only need to touch backends/ and models.py on the backend side — the route and service layers use a model config registry that handles dispatch automatically.

```
backends/
```


```
models.py
```

## [Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research)
[Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research)
This phase is mandatory. Clone the model library and its key dependencies into a temporary directory and inspect them before writing any integration code. The goal is to produce a dependency audit that identifies every PyInstaller-incompatible pattern, every native data file, and every upstream bug you'll need to work around.

[0.1 Clone and Inspect the Model Library](https://docs.voicebox.sh/developer/tts-engines#01-clone-and-inspect-the-model-library)

```
# Create a throwaway workspace mkdir /tmp/engine-research && cd /tmp/engine-research # Clone the model library git clone https://github.com/org/model-library.git cd model-library
```


```
# Create a throwaway workspace mkdir /tmp/engine-research && cd /tmp/engine-research # Clone the model library git clone https://github.com/org/model-library.git cd model-library
```

Read these files first, in order:
1. 
setup.py / setup.cfg / pyproject.toml — Check pinned dependency versions. If the library pins torch==2.6.0 or numpy<1.26, you'll need --no-deps installation and manual sub-dependency listing (this is what happened with chatterbox-tts).

2. 
__init__.py and the main model class — Trace the import chain. Look for:

from_pretrained() — does it call huggingface_hub internally? Does it pass token=True (which crashes without a stored HF token)?
from_local() — does it exist? You may need manual snapshot_download() + from_local() to bypass download bugs.
Device handling — does it default to CUDA? Does it support MPS? Many libraries crash on MPS with unsupported operators.


3. from_pretrained() — does it call huggingface_hub internally? Does it pass token=True (which crashes without a stored HF token)?
4. from_local() — does it exist? You may need manual snapshot_download() + from_local() to bypass download bugs.
5. Device handling — does it default to CUDA? Does it support MPS? Many libraries crash on MPS with unsupported operators.
6. 
All import statements — Recursively trace what the library imports. You're looking for:

inspect.getsource() anywhere in the chain (search all .py files)
typeguard / @typechecked decorators (these call inspect.getsource() at import time)
importlib.metadata.version() or pkg_resources.get_distribution() (need --copy-metadata)
lazy_loader (needs --collect-all to bundle .pyi stubs)


7. inspect.getsource() anywhere in the chain (search all .py files)
8. typeguard / @typechecked decorators (these call inspect.getsource() at import time)
9. importlib.metadata.version() or pkg_resources.get_distribution() (need --copy-metadata)
10. lazy_loader (needs --collect-all to bundle .pyi stubs)
setup.py / setup.cfg / pyproject.toml — Check pinned dependency versions. If the library pins torch==2.6.0 or numpy<1.26, you'll need --no-deps installation and manual sub-dependency listing (this is what happened with chatterbox-tts).

```
setup.py
```


```
setup.cfg
```


```
pyproject.toml
```


```
torch==2.6.0
```


```
numpy<1.26
```


```
--no-deps
```


```
chatterbox-tts
```

__init__.py and the main model class — Trace the import chain. Look for:

```
__init__.py
```

- from_pretrained() — does it call huggingface_hub internally? Does it pass token=True (which crashes without a stored HF token)?
- from_local() — does it exist? You may need manual snapshot_download() + from_local() to bypass download bugs.
- Device handling — does it default to CUDA? Does it support MPS? Many libraries crash on MPS with unsupported operators.

```
from_pretrained()
```


```
huggingface_hub
```


```
token=True
```


```
from_local()
```


```
snapshot_download()
```


```
from_local()
```

All import statements — Recursively trace what the library imports. You're looking for:

```
import
```

- inspect.getsource() anywhere in the chain (search all .py files)
- typeguard / @typechecked decorators (these call inspect.getsource() at import time)
- importlib.metadata.version() or pkg_resources.get_distribution() (need --copy-metadata)
- lazy_loader (needs --collect-all to bundle .pyi stubs)

```
inspect.getsource()
```


```
.py
```


```
typeguard
```


```
@typechecked
```


```
inspect.getsource()
```


```
importlib.metadata.version()
```


```
pkg_resources.get_distribution()
```


```
--copy-metadata
```


```
lazy_loader
```


```
--collect-all
```


```
.pyi
```

[0.2 Scan for PyInstaller-Incompatible Patterns](https://docs.voicebox.sh/developer/tts-engines#02-scan-for-pyinstaller-incompatible-patterns)
Run these searches against the cloned library and its transitive dependencies:

```
# inspect.getsource — will crash in frozen binary without --collect-all grep -r "inspect.getsource\|getsource(" . # typeguard / @typechecked — calls inspect.getsource at import time grep -r "@typechecked\|from typeguard" . # importlib.metadata — needs --copy-metadata grep -r "importlib.metadata\|pkg_resources.get_distribution\|pkg_resources.require" . # Data files loaded at runtime — need --collect-all or --collect-data grep -r "Path(__file__).parent\|os.path.dirname(__file__)\|resources_path\|pkg_resources.resource_filename" . # Native library paths — may need env var override in frozen builds grep -r "/usr/share\|/usr/lib\|/usr/local\|espeak\|phonemize" . # torch.load without map_location — will crash on CPU-only builds grep -r "torch.load(" . | grep -v "map_location" # HuggingFace token bugs grep -r 'token=True\|token=os.getenv' . # Float64/Float32 assumptions — librosa returns float64, many models assume float32 grep -r "torch.from_numpy\|\.double()\|float64" . # @torch.jit.script — calls inspect.getsource(), crashes in frozen builds grep -r "@torch.jit.script\|torch.jit.script" . # torchaudio.load — requires torchcodec in torchaudio 2.10+, use soundfile.read() instead grep -r "torchaudio.load\|torchaudio.save" . # Gated HuggingFace repos — models that hardcode gated repos as tokenizer/config sources grep -r "from_pretrained\|tokenizer_name\|AutoTokenizer" . | grep -i "llama\|meta-llama\|gated"
```


```
# inspect.getsource — will crash in frozen binary without --collect-all grep -r "inspect.getsource\|getsource(" . # typeguard / @typechecked — calls inspect.getsource at import time grep -r "@typechecked\|from typeguard" . # importlib.metadata — needs --copy-metadata grep -r "importlib.metadata\|pkg_resources.get_distribution\|pkg_resources.require" . # Data files loaded at runtime — need --collect-all or --collect-data grep -r "Path(__file__).parent\|os.path.dirname(__file__)\|resources_path\|pkg_resources.resource_filename" . # Native library paths — may need env var override in frozen builds grep -r "/usr/share\|/usr/lib\|/usr/local\|espeak\|phonemize" . # torch.load without map_location — will crash on CPU-only builds grep -r "torch.load(" . | grep -v "map_location" # HuggingFace token bugs grep -r 'token=True\|token=os.getenv' . # Float64/Float32 assumptions — librosa returns float64, many models assume float32 grep -r "torch.from_numpy\|\.double()\|float64" . # @torch.jit.script — calls inspect.getsource(), crashes in frozen builds grep -r "@torch.jit.script\|torch.jit.script" . # torchaudio.load — requires torchcodec in torchaudio 2.10+, use soundfile.read() instead grep -r "torchaudio.load\|torchaudio.save" . # Gated HuggingFace repos — models that hardcode gated repos as tokenizer/config sources grep -r "from_pretrained\|tokenizer_name\|AutoTokenizer" . | grep -i "llama\|meta-llama\|gated"
```

### [0.3 Install and Trace in a Throwaway Venv](https://docs.voicebox.sh/developer/tts-engines#03-install-and-trace-in-a-throwaway-venv)
[0.3 Install and Trace in a Throwaway Venv](https://docs.voicebox.sh/developer/tts-engines#03-install-and-trace-in-a-throwaway-venv)

```
# Create isolated venv python -m venv /tmp/engine-venv source /tmp/engine-venv/bin/activate # Install the package (try normally first) pip install model-package # Check if it conflicts with our stack pip install model-package torch==2.10 transformers==4.57.3 numpy>=1.26 # If this fails, you need --no-deps: pip install --no-deps model-package # Get the full dependency tree pip show model-package # Check Requires: field pip show -f model-package # List all installed files (look for data files) # Check for non-PyPI dependencies pip install model-package 2>&1 | grep -i "no matching distribution"
```


```
# Create isolated venv python -m venv /tmp/engine-venv source /tmp/engine-venv/bin/activate # Install the package (try normally first) pip install model-package # Check if it conflicts with our stack pip install model-package torch==2.10 transformers==4.57.3 numpy>=1.26 # If this fails, you need --no-deps: pip install --no-deps model-package # Get the full dependency tree pip show model-package # Check Requires: field pip show -f model-package # List all installed files (look for data files) # Check for non-PyPI dependencies pip install model-package 2>&1 | grep -i "no matching distribution"
```

### [0.4 Test Model Loading on CPU](https://docs.voicebox.sh/developer/tts-engines#04-test-model-loading-on-cpu)
[0.4 Test Model Loading on CPU](https://docs.voicebox.sh/developer/tts-engines#04-test-model-loading-on-cpu)
Before writing any integration code, verify the model works on CPU in a plain Python script:

```
import torch # Force CPU to catch map_location bugs early model = ModelClass.from_pretrained("org/model", device="cpu") # Test with a float32 audio array (not float64) import numpy as np audio = np.random.randn(16000).astype(np.float32) output = model.generate("Hello world", audio) print(f"Output shape: {output.shape}, dtype: {output.dtype}, sample rate: {model.sample_rate}")
```


```
import torch # Force CPU to catch map_location bugs early model = ModelClass.from_pretrained("org/model", device="cpu") # Test with a float32 audio array (not float64) import numpy as np audio = np.random.randn(16000).astype(np.float32) output = model.generate("Hello world", audio) print(f"Output shape: {output.shape}, dtype: {output.dtype}, sample rate: {model.sample_rate}")
```

If this crashes, you've found a bug you'll need to monkey-patch. Common ones:
- RuntimeError: expected scalar type Float but found Double → needs float32 cast
- RuntimeError: map_location → needs torch.load patch
- RuntimeError: Unsupported operator aten::... → needs MPS skip

```
RuntimeError: expected scalar type Float but found Double
```


```
RuntimeError: map_location
```


```
torch.load
```


```
RuntimeError: Unsupported operator aten::...
```

### [0.5 Produce a Dependency Audit](https://docs.voicebox.sh/developer/tts-engines#05-produce-a-dependency-audit)
[0.5 Produce a Dependency Audit](https://docs.voicebox.sh/developer/tts-engines#05-produce-a-dependency-audit)
Before proceeding to Phase 1, write down:
1. PyPI vs non-PyPI deps — which packages need --find-links, git+https://, or --no-deps?
2. PyInstaller directives needed — which packages need --collect-all, --copy-metadata, --hidden-import?
3. Runtime data files — which packages ship data files (YAML, pretrained weights, phoneme tables, shader libraries) that must be bundled?
4. Native library paths — which packages look for data at system paths that won't exist in a frozen binary?
5. Monkey-patches needed — torch.load map_location, float64→float32 casts, MPS skip, HF token bypass, etc.
6. Sample rate — what does the engine output? (24kHz, 44.1kHz, 48kHz)
7. Model download method — from_pretrained() with library-managed download, or manual snapshot_download() + from_local()?

```
--find-links
```


```
git+https://
```


```
--no-deps
```


```
--collect-all
```


```
--copy-metadata
```


```
--hidden-import
```


```
torch.load
```


```
from_pretrained()
```


```
snapshot_download()
```


```
from_local()
```

This audit becomes your implementation plan for Phases 1, 4, and 5.

[Phase 1: Backend Implementation](https://docs.voicebox.sh/developer/tts-engines#phase-1-backend-implementation)

### [1.1 Create the Backend File](https://docs.voicebox.sh/developer/tts-engines#11-create-the-backend-file)
[1.1 Create the Backend File](https://docs.voicebox.sh/developer/tts-engines#11-create-the-backend-file)
Create backend/backends/<engine>_backend.py (~200-300 lines) implementing the TTSBackend protocol:

```
backend/backends/<engine>_backend.py
```


```
TTSBackend
```


```
class YourBackend: """Must satisfy the TTSBackend protocol.""" async def load_model(self, model_size: str = "default") -> None: ... async def create_voice_prompt(self, audio_path: str, reference_text: str, use_cache: bool = True) -> tuple[dict, bool]: ... async def combine_voice_prompts(self, audio_paths: list[str], ref_texts: list[str]) -> tuple[np.ndarray, str]: ... async def generate(self, text: str, voice_prompt: dict, language: str = "en", seed: int | None = None, instruct: str | None = None) -> tuple[np.ndarray, int]: ... def unload_model(self) -> None: ... def is_loaded(self) -> bool: ... def _get_model_path(self, model_size: str) -> str: ...
```


```
class YourBackend: """Must satisfy the TTSBackend protocol.""" async def load_model(self, model_size: str = "default") -> None: ... async def create_voice_prompt(self, audio_path: str, reference_text: str, use_cache: bool = True) -> tuple[dict, bool]: ... async def combine_voice_prompts(self, audio_paths: list[str], ref_texts: list[str]) -> tuple[np.ndarray, str]: ... async def generate(self, text: str, voice_prompt: dict, language: str = "en", seed: int | None = None, instruct: str | None = None) -> tuple[np.ndarray, int]: ... def unload_model(self) -> None: ... def is_loaded(self) -> bool: ... def _get_model_path(self, model_size: str) -> str: ...
```

Key decisions per engine:

```
snapshot_download
```


```
token=True
```

### [1.2 Voice Prompt Patterns](https://docs.voicebox.sh/developer/tts-engines#12-voice-prompt-patterns)
[1.2 Voice Prompt Patterns](https://docs.voicebox.sh/developer/tts-engines#12-voice-prompt-patterns)
Pattern A: Pre-computed tensors (Qwen, LuxTTS)

```
encoded = model.encode_prompt(audio_path) return encoded, False # (prompt_dict, was_cached)
```


```
encoded = model.encode_prompt(audio_path) return encoded, False # (prompt_dict, was_cached)
```

Pattern B: Deferred file paths (Chatterbox, MLX)

```
return {"ref_audio": audio_path, "ref_text": reference_text}, False
```


```
return {"ref_audio": audio_path, "ref_text": reference_text}, False
```

Pattern C: Hybrid (possible for new engines)

```
embedding = model.extract_speaker(audio_path) return {"embedding": embedding, "ref_audio": audio_path}, False
```


```
embedding = model.extract_speaker(audio_path) return {"embedding": embedding, "ref_audio": audio_path}, False
```

If caching, prefix your cache keys:

```
cache_key = "yourengine_" + get_cache_key(audio_path, reference_text)
```


```
cache_key = "yourengine_" + get_cache_key(audio_path, reference_text)
```

### [1.3 Register the Engine](https://docs.voicebox.sh/developer/tts-engines#13-register-the-engine)
[1.3 Register the Engine](https://docs.voicebox.sh/developer/tts-engines#13-register-the-engine)
In backend/backends/__init__.py:

```
backend/backends/__init__.py
```

Add a ModelConfig entry:

```
ModelConfig
```


```
ModelConfig( model_name="your-engine", display_name="Your Engine", engine="your_engine", hf_repo_id="org/model-repo", size_mb=3200, needs_trim=False, # set True if output needs trim_tts_output() languages=["en", "fr", "de"], ),
```


```
ModelConfig( model_name="your-engine", display_name="Your Engine", engine="your_engine", hf_repo_id="org/model-repo", size_mb=3200, needs_trim=False, # set True if output needs trim_tts_output() languages=["en", "fr", "de"], ),
```

Add to TTS_ENGINES dict:

```
TTS_ENGINES
```


```
TTS_ENGINES = { ... "your_engine": "Your Engine", }
```


```
TTS_ENGINES = { ... "your_engine": "Your Engine", }
```

Add factory branch:

```
elif engine == "your_engine": from .your_backend import YourBackend backend = YourBackend()
```


```
elif engine == "your_engine": from .your_backend import YourBackend backend = YourBackend()
```

### [1.4 Update Request Models](https://docs.voicebox.sh/developer/tts-engines#14-update-request-models)
[1.4 Update Request Models](https://docs.voicebox.sh/developer/tts-engines#14-update-request-models)
In backend/models.py:

```
backend/models.py
```

- Add engine name to GenerationRequest.engine regex pattern
- Add any new language codes to the language regex

```
GenerationRequest.engine
```

[Phase 2: Route and Service Integration](https://docs.voicebox.sh/developer/tts-engines#phase-2-route-and-service-integration)
With the model config registry, route and service layers have zero per-engine dispatch points. All endpoints use registry helpers like get_model_config(), load_engine_model(), engine_needs_trim(), check_model_loaded(), etc.

```
get_model_config()
```


```
load_engine_model()
```


```
engine_needs_trim()
```


```
check_model_loaded()
```

You don't need to touch any route or service files unless your engine needs custom behavior in the generate pipeline.

[Post-Processing](https://docs.voicebox.sh/developer/tts-engines#post-processing)
If your model produces trailing silence, set needs_trim=True on your ModelConfig. The generation service applies trim_tts_output() automatically.

```
needs_trim=True
```


```
ModelConfig
```


```
trim_tts_output()
```

[Phase 3: Frontend Integration](https://docs.voicebox.sh/developer/tts-engines#phase-3-frontend-integration)

### [3.1 TypeScript Types](https://docs.voicebox.sh/developer/tts-engines#31-typescript-types)
[3.1 TypeScript Types](https://docs.voicebox.sh/developer/tts-engines#31-typescript-types)
In app/src/lib/api/types.ts:

```
app/src/lib/api/types.ts
```

- Add to the engine union type on GenerationRequest

```
engine
```


```
GenerationRequest
```

### [3.2 Language Maps](https://docs.voicebox.sh/developer/tts-engines#32-language-maps)
[3.2 Language Maps](https://docs.voicebox.sh/developer/tts-engines#32-language-maps)
In app/src/lib/constants/languages.ts:

```
app/src/lib/constants/languages.ts
```

- Add entry to ENGINE_LANGUAGES record
- Add any new language codes to ALL_LANGUAGES if needed

```
ENGINE_LANGUAGES
```


```
ALL_LANGUAGES
```

### [3.3 Engine/Model Selector](https://docs.voicebox.sh/developer/tts-engines#33-enginemodel-selector)
[3.3 Engine/Model Selector](https://docs.voicebox.sh/developer/tts-engines#33-enginemodel-selector)
In app/src/components/Generation/EngineModelSelector.tsx:

```
app/src/components/Generation/EngineModelSelector.tsx
```

- Add entry to ENGINE_OPTIONS and ENGINE_DESCRIPTIONS
- Add to ENGLISH_ONLY_ENGINES if applicable

```
ENGINE_OPTIONS
```


```
ENGINE_DESCRIPTIONS
```


```
ENGLISH_ONLY_ENGINES
```

### [3.4 Form Hook](https://docs.voicebox.sh/developer/tts-engines#34-form-hook)
[3.4 Form Hook](https://docs.voicebox.sh/developer/tts-engines#34-form-hook)
In app/src/lib/hooks/useGenerationForm.ts:

```
app/src/lib/hooks/useGenerationForm.ts
```

- Add to Zod schema enum for engine
- Add engine-to-model-name mapping
- Update payload construction for engine-specific fields

```
engine
```

Watch out for model naming inconsistencies. The HuggingFace repo name, the model size label, and the API model name don't always follow predictable patterns. For example, TADA's 3B model is named tada-3b-ml (not tada-3b), because it's a multilingual variant. Always check the actual repo names and build the frontend model name mapping from those, not from assumptions like {engine}-{size}.

```
tada-3b-ml
```


```
tada-3b
```


```
{engine}-{size}
```

### [3.5 Model Management](https://docs.voicebox.sh/developer/tts-engines#35-model-management)
[3.5 Model Management](https://docs.voicebox.sh/developer/tts-engines#35-model-management)
In app/src/components/ServerSettings/ModelManagement.tsx:

```
app/src/components/ServerSettings/ModelManagement.tsx
```

- Add description to MODEL_DESCRIPTIONS record
- Add model name to voiceModels filter condition

```
MODEL_DESCRIPTIONS
```


```
voiceModels
```

[3.6 Non-Cloning Engines (Preset Voices)](https://docs.voicebox.sh/developer/tts-engines#36-non-cloning-engines-preset-voices)
If your engine uses pre-built voices instead of zero-shot cloning from reference audio (e.g. Kokoro), additional integration is needed:
Backend:
- In kokoro_backend.py (or your engine), define a VOICES list of (voice_id, display_name, gender, language) tuples
- create_voice_prompt() should return {"voice_type": "preset", "preset_engine": "<engine>", "preset_voice_id": "<id>"}
- generate() should read voice_prompt.get("preset_voice_id") to select the voice
- Add a seed_preset_profiles("<engine>") call in backend/routes/models.py after model download completes
- The seed_preset_profiles() function in backend/services/profiles.py creates DB profiles with voice_type="preset"

```
kokoro_backend.py
```


```
VOICES
```


```
(voice_id, display_name, gender, language)
```


```
create_voice_prompt()
```


```
{"voice_type": "preset", "preset_engine": "<engine>", "preset_voice_id": "<id>"}
```


```
generate()
```


```
voice_prompt.get("preset_voice_id")
```


```
seed_preset_profiles("<engine>")
```


```
backend/routes/models.py
```


```
seed_preset_profiles()
```


```
backend/services/profiles.py
```


```
voice_type="preset"
```

Frontend:
- The EngineModelSelector filters options based on selectedProfile.voice_type:

"cloned" profiles → only cloning engines shown (Kokoro hidden)
"preset" profiles → only the preset's engine shown


- "cloned" profiles → only cloning engines shown (Kokoro hidden)
- "preset" profiles → only the preset's engine shown
- Profile cards show the engine name as a badge for preset profiles
- When a preset profile is selected, the engine auto-switches

```
EngineModelSelector
```


```
selectedProfile.voice_type
```

- "cloned" profiles → only cloning engines shown (Kokoro hidden)
- "preset" profiles → only the preset's engine shown

```
"cloned"
```


```
"preset"
```

Profile schema fields for presets:
- voice_type: "preset" (vs "cloned" for traditional profiles)
- preset_engine: "<engine>" — which engine owns this voice
- preset_voice_id: "<id>" — the engine-specific voice identifier

```
voice_type: "preset"
```


```
"cloned"
```


```
preset_engine: "<engine>"
```


```
preset_voice_id: "<id>"
```

For future "designed" voices (text description instead of audio, e.g. Qwen CustomVoice):
- Use voice_type: "designed" with design_prompt field
- create_voice_prompt_for_profile() already returns the design prompt for this type

```
voice_type: "designed"
```


```
design_prompt
```


```
create_voice_prompt_for_profile()
```

[Phase 4: Dependencies](https://docs.voicebox.sh/developer/tts-engines#phase-4-dependencies)
Use the dependency audit from Phase 0 to drive this phase. You should already know what packages are needed, which conflict, and which require special installation.

### [4.1 Python Dependencies](https://docs.voicebox.sh/developer/tts-engines#41-python-dependencies)
[4.1 Python Dependencies](https://docs.voicebox.sh/developer/tts-engines#41-python-dependencies)
Add to backend/requirements.txt. There are three installation patterns, depending on what Phase 0 revealed:

```
backend/requirements.txt
```

Normal PyPI packages:

```
some-model-package>=1.0.0
```


```
some-model-package>=1.0.0
```

Pinned dependency conflicts (--no-deps) — If the model package pins old versions of torch/numpy/transformers, install with --no-deps and list sub-dependencies manually. This is the pattern used for chatterbox-tts:

```
--no-deps
```


```
--no-deps
```


```
chatterbox-tts
```


```
# In justfile / CI setup: pip install --no-deps chatterbox-tts # In requirements.txt — list each actual sub-dependency: conformer>=0.3.2 diffusers>=0.31.0 omegaconf>=2.3.0 resemble-perth>=0.0.2 s3tokenizer>=0.1.6
```


```
# In justfile / CI setup: pip install --no-deps chatterbox-tts # In requirements.txt — list each actual sub-dependency: conformer>=0.3.2 diffusers>=0.31.0 omegaconf>=2.3.0 resemble-perth>=0.0.2 s3tokenizer>=0.1.6
```

To identify sub-deps: pip show chatterbox-tts → Requires: field, then cross-reference against existing requirements.txt to avoid duplicates.

```
pip show chatterbox-tts
```


```
Requires:
```


```
requirements.txt
```

Non-PyPI packages — Some libraries only exist on GitHub or require custom indexes:

```
# Git-only packages (no PyPI release) linacodec @ git+https://github.com/ysharma3501/LinaCodec.git Zipvoice @ git+https://github.com/ysharma3501/LuxTTS.git # Custom package indexes (C extensions with platform-specific wheels) --find-links https://k2-fsa.github.io/icefall/piper_phonemize.html piper-phonemize>=1.2.0
```


```
# Git-only packages (no PyPI release) linacodec @ git+https://github.com/ysharma3501/LinaCodec.git Zipvoice @ git+https://github.com/ysharma3501/LuxTTS.git # Custom package indexes (C extensions with platform-specific wheels) --find-links https://k2-fsa.github.io/icefall/piper_phonemize.html piper-phonemize>=1.2.0
```

### [4.2 Dependency Conflict Resolution](https://docs.voicebox.sh/developer/tts-engines#42-dependency-conflict-resolution)
[4.2 Dependency Conflict Resolution](https://docs.voicebox.sh/developer/tts-engines#42-dependency-conflict-resolution)
Check for conflicts with the existing stack before adding anything:

```
# Our current stack pins (approximate): # Python 3.12+, torch>=2.10, transformers>=4.57, numpy>=1.26 # Test compatibility pip install model-package torch==2.10 transformers==4.57.3 numpy>=1.26 # If it fails, check what the package pins: pip show model-package | grep Requires # Look at setup.py/pyproject.toml for version constraints
```


```
# Our current stack pins (approximate): # Python 3.12+, torch>=2.10, transformers>=4.57, numpy>=1.26 # Test compatibility pip install model-package torch==2.10 transformers==4.57.3 numpy>=1.26 # If it fails, check what the package pins: pip show model-package | grep Requires # Look at setup.py/pyproject.toml for version constraints
```

Known incompatible patterns in the wild:
- torch==2.6.0 — many older packages pin this
- numpy<1.26 — conflicts with Python 3.12+
- transformers==4.46.3 — many packages pin old transformers
- onnxruntime pinned versions — often conflict with torch

```
torch==2.6.0
```


```
numpy<1.26
```


```
transformers==4.46.3
```


```
onnxruntime
```

### [4.3 Update Installation Scripts](https://docs.voicebox.sh/developer/tts-engines#43-update-installation-scripts)
[4.3 Update Installation Scripts](https://docs.voicebox.sh/developer/tts-engines#43-update-installation-scripts)
Dependencies must be added in multiple places:

```
backend/requirements.txt
```


```
justfile
```


```
--no-deps
```


```
setup-python
```


```
setup-python-release
```


```
.github/workflows/release.yml
```


```
--no-deps
```


```
Dockerfile
```

[Phase 5: PyInstaller Bundling (build_binary.py)](https://docs.voicebox.sh/developer/tts-engines#phase-5-pyinstaller-bundling-build_binarypy)

```
build_binary.py
```

This is where most of the pain lives. The v0.2.3 release was entirely dedicated to fixing bundling issues — every new engine that shipped in v0.2.1 (LuxTTS, Chatterbox, Chatterbox Turbo) worked in dev but failed in production builds. Don't skip this phase.

### [5.1 Register Your Engine in build_binary.py](https://docs.voicebox.sh/developer/tts-engines#51-register-your-engine-in-build_binarypy)
[5.1 Register Your Engine in build_binary.py](https://docs.voicebox.sh/developer/tts-engines#51-register-your-engine-in-build_binarypy)

```
build_binary.py
```

Every new engine needs entries in backend/build_binary.py. This file drives PyInstaller and is the single most common source of "works in dev, breaks in prod" bugs. You need to decide which PyInstaller directives your engine's dependencies require:

```
backend/build_binary.py
```


```
--hidden-import <module>
```


```
--collect-all <package>
```


```
.py
```


```
inspect.getsource()
```


```
inflect
```


```
typeguard
```


```
@typechecked
```


```
perth
```


```
.pth.tar
```


```
hparams.yaml
```


```
--collect-data <package>
```


```
--collect-submodules <package>
```


```
--copy-metadata <package>
```


```
importlib.metadata
```


```
importlib.metadata.version()
```


```
pkg_resources.get_distribution()
```


```
requests
```


```
transformers
```


```
huggingface-hub
```


```
tokenizers
```


```
safetensors
```


```
tqdm
```

Example: adding hidden imports and collect-all for a new engine:

```
# In build_binary.py, inside the args list: "--hidden-import", "backend.backends.your_engine_backend", "--hidden-import", "your_engine_package", "--hidden-import", "your_engine_package.inference", "--collect-all", "some_dependency_that_uses_inspect_getsource", "--copy-metadata", "some_dependency_that_checks_its_own_version",
```


```
# In build_binary.py, inside the args list: "--hidden-import", "backend.backends.your_engine_backend", "--hidden-import", "your_engine_package", "--hidden-import", "your_engine_package.inference", "--collect-all", "some_dependency_that_uses_inspect_getsource", "--copy-metadata", "some_dependency_that_checks_its_own_version",
```

### [5.2 Lessons from v0.2.3 — Real Failures and Their Fixes](https://docs.voicebox.sh/developer/tts-engines#52-lessons-from-v023--real-failures-and-their-fixes)
[5.2 Lessons from v0.2.3 — Real Failures and Their Fixes](https://docs.voicebox.sh/developer/tts-engines#52-lessons-from-v023--real-failures-and-their-fixes)
These are actual production failures from shipping new engines. Every one of these passed python -m uvicorn in dev:

```
python -m uvicorn
```


```
"could not get source code"
```


```
inflect
```


```
typeguard
```


```
@typechecked
```


```
inspect.getsource()
```


```
.py
```


```
--collect-all inflect
```


```
espeak-ng-data
```


```
piper_phonemize
```


```
/usr/share/espeak-ng-data/
```


```
--collect-all piper_phonemize
```


```
ESPEAK_DATA_PATH
```


```
inspect.getsource
```


```
linacodec
```


```
zipvoice
```


```
--collect-all linacodec
```


```
--collect-all zipvoice
```


```
FileNotFoundError
```


```
perth
```


```
hparams.yaml
```


```
.pth.tar
```


```
--collect-all perth
```


```
importlib.metadata
```


```
huggingface-hub
```


```
transformers
```


```
--copy-metadata
```


```
huggingface_hub
```


```
HFProgressTracker
```


```
inspect.getsource
```


```
Snake1d
```


```
@torch.jit.script
```


```
inspect.getsource()
```


```
.py
```


```
dac_shim.py
```


```
Snake1d
```


```
@torch.jit.script
```


```
dac.*
```


```
sys.modules
```


```
NameError: name 'obj' is not defined
```

[CPython bug](https://github.com/pyinstaller/pyinstaller/issues/7992)

```
resource_tracker
```


```
multiprocessing
```


```
freeze_support()
```


```
server.py
```

### [5.3 Runtime Frozen-Build Handling (server.py)](https://docs.voicebox.sh/developer/tts-engines#53-runtime-frozen-build-handling-serverpy)
[5.3 Runtime Frozen-Build Handling (server.py)](https://docs.voicebox.sh/developer/tts-engines#53-runtime-frozen-build-handling-serverpy)

```
server.py
```

Some fixes can't live in build_binary.py — they need runtime detection. The entry point backend/server.py handles these before any heavy imports:

```
build_binary.py
```


```
backend/server.py
```


```
# 1. freeze_support() — MUST be called before any multiprocessing use import multiprocessing multiprocessing.freeze_support() # 2. Native data paths — redirect C libraries to bundled data if getattr(sys, 'frozen', False): _meipass = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable)) _espeak_data = os.path.join(_meipass, 'piper_phonemize', 'espeak-ng-data') if os.path.isdir(_espeak_data): os.environ.setdefault('ESPEAK_DATA_PATH', _espeak_data) # 3. stdout/stderr safety — PyInstaller --noconsole on Windows sets these to None if not _is_writable(sys.stdout): sys.stdout = open(os.devnull, 'w')
```


```
# 1. freeze_support() — MUST be called before any multiprocessing use import multiprocessing multiprocessing.freeze_support() # 2. Native data paths — redirect C libraries to bundled data if getattr(sys, 'frozen', False): _meipass = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable)) _espeak_data = os.path.join(_meipass, 'piper_phonemize', 'espeak-ng-data') if os.path.isdir(_espeak_data): os.environ.setdefault('ESPEAK_DATA_PATH', _espeak_data) # 3. stdout/stderr safety — PyInstaller --noconsole on Windows sets these to None if not _is_writable(sys.stdout): sys.stdout = open(os.devnull, 'w')
```

If your engine's dependencies include native libraries that look for data at system paths (like espeak-ng does), you'll need to add a similar os.environ.setdefault() block here.

```
os.environ.setdefault()
```

### [5.4 CUDA vs CPU Build Branching](https://docs.voicebox.sh/developer/tts-engines#54-cuda-vs-cpu-build-branching)
[5.4 CUDA vs CPU Build Branching](https://docs.voicebox.sh/developer/tts-engines#54-cuda-vs-cpu-build-branching)
build_binary.py produces two different binaries:

```
build_binary.py
```

- voicebox-server (CPU) — excludes all nvidia.* packages to avoid bundling ~3 GB of CUDA DLLs
- voicebox-server-cuda — includes torch.cuda and torch.backends.cudnn

```
voicebox-server
```


```
nvidia.*
```


```
voicebox-server-cuda
```


```
torch.cuda
```


```
torch.backends.cudnn
```

On Windows, if the build environment has CUDA torch installed but you're building the CPU binary, the script temporarily swaps to CPU-only torch and restores CUDA torch afterward. This prevents PyInstaller from accidentally bundling CUDA libraries into the CPU build.
New engine imports go in the common section (not the CUDA or MLX conditional blocks) unless your engine has platform-specific dependencies.

### [5.5 MLX Conditional Inclusion](https://docs.voicebox.sh/developer/tts-engines#55-mlx-conditional-inclusion)
[5.5 MLX Conditional Inclusion](https://docs.voicebox.sh/developer/tts-engines#55-mlx-conditional-inclusion)
Apple Silicon builds conditionally include MLX hidden imports and --collect-all mlx / --collect-all mlx_audio. If your engine has an MLX-specific backend variant, add its imports inside the if is_apple_silicon() and not cuda: block.

```
--collect-all mlx
```


```
--collect-all mlx_audio
```


```
if is_apple_silicon() and not cuda:
```

### [5.6 Testing Frozen Builds](https://docs.voicebox.sh/developer/tts-engines#56-testing-frozen-builds)
[5.6 Testing Frozen Builds](https://docs.voicebox.sh/developer/tts-engines#56-testing-frozen-builds)
You can't skip this. Models that work in python -m uvicorn will break in the PyInstaller binary. The v0.2.3 release required three patch releases (v0.2.1 → v0.2.2 → v0.2.3) to get all engines working in production.

```
python -m uvicorn
```

1. Build: just build
2. Launch the binary directly (not via python -m)
3. Test the full chain: download → load → generate → progress tracking
4. Check stderr for the actual error (logs go to stderr for Tauri sidecar capture)
5. Fix, rebuild, repeat

```
just build
```


```
python -m
```

Common gotcha: testing only generation with a pre-cached model from your dev install. Always test with a clean model cache to verify downloads work too.

[Phase 6: Common Upstream Workarounds](https://docs.voicebox.sh/developer/tts-engines#phase-6-common-upstream-workarounds)

### [torch.load device mismatch](https://docs.voicebox.sh/developer/tts-engines#torchload-device-mismatch)
[torch.load device mismatch](https://docs.voicebox.sh/developer/tts-engines#torchload-device-mismatch)

```
_original_torch_load = torch.load def _patched_torch_load(*args, **kwargs): kwargs.setdefault("map_location", "cpu") return _original_torch_load(*args, **kwargs) torch.load = _patched_torch_load
```


```
_original_torch_load = torch.load def _patched_torch_load(*args, **kwargs): kwargs.setdefault("map_location", "cpu") return _original_torch_load(*args, **kwargs) torch.load = _patched_torch_load
```

### [Float64/Float32 dtype mismatch](https://docs.voicebox.sh/developer/tts-engines#float64float32-dtype-mismatch)
[Float64/Float32 dtype mismatch](https://docs.voicebox.sh/developer/tts-engines#float64float32-dtype-mismatch)

```
original_fn = SomeClass.some_method def patched_fn(self, *args, **kwargs): result = original_fn(self, *args, **kwargs) return result.float() SomeClass.some_method = patched_fn
```


```
original_fn = SomeClass.some_method def patched_fn(self, *args, **kwargs): result = original_fn(self, *args, **kwargs) return result.float() SomeClass.some_method = patched_fn
```

### [HuggingFace token bug](https://docs.voicebox.sh/developer/tts-engines#huggingface-token-bug)
[HuggingFace token bug](https://docs.voicebox.sh/developer/tts-engines#huggingface-token-bug)

```
from huggingface_hub import snapshot_download local_path = snapshot_download(repo_id=REPO, token=None) model = ModelClass.from_local(local_path, device=device)
```


```
from huggingface_hub import snapshot_download local_path = snapshot_download(repo_id=REPO, token=None) model = ModelClass.from_local(local_path, device=device)
```

### [MPS tensor issues](https://docs.voicebox.sh/developer/tts-engines#mps-tensor-issues)
[MPS tensor issues](https://docs.voicebox.sh/developer/tts-engines#mps-tensor-issues)
Skip MPS entirely if operators aren't supported:

```
def _get_device(self): if torch.cuda.is_available(): return "cuda" return "cpu" # Skip MPS
```


```
def _get_device(self): if torch.cuda.is_available(): return "cuda" return "cpu" # Skip MPS
```

### [Gated HuggingFace repos as hardcoded config sources](https://docs.voicebox.sh/developer/tts-engines#gated-huggingface-repos-as-hardcoded-config-sources)
[Gated HuggingFace repos as hardcoded config sources](https://docs.voicebox.sh/developer/tts-engines#gated-huggingface-repos-as-hardcoded-config-sources)
Some models hardcode a gated HuggingFace repo as their tokenizer or config source (e.g., TADA hardcodes "meta-llama/Llama-3.2-1B" in both its AlignerConfig and TadaConfig). This silently fails without HF authentication.

```
"meta-llama/Llama-3.2-1B"
```


```
AlignerConfig
```


```
TadaConfig
```

Fix: Download from an ungated mirror and patch the config objects directly:

```
# Download tokenizer from ungated mirror UNGATED_TOKENIZER = "unsloth/Llama-3.2-1B" tokenizer_path = snapshot_download(UNGATED_TOKENIZER, token=None) # Patch the model config to use the local path instead of the gated repo config = ModelConfig.from_pretrained(model_path) config.tokenizer_name = tokenizer_path model = ModelClass.from_pretrained(model_path, config=config)
```


```
# Download tokenizer from ungated mirror UNGATED_TOKENIZER = "unsloth/Llama-3.2-1B" tokenizer_path = snapshot_download(UNGATED_TOKENIZER, token=None) # Patch the model config to use the local path instead of the gated repo config = ModelConfig.from_pretrained(model_path) config.tokenizer_name = tokenizer_path model = ModelClass.from_pretrained(model_path, config=config)
```

Do NOT monkey-patch AutoTokenizer.from_pretrained — it's a classmethod, and replacing it corrupts the descriptor, which breaks other engines that use different tokenizers (e.g., Qwen uses a Qwen tokenizer via AutoTokenizer). Always patch at the config level, not the class method level.

```
AutoTokenizer.from_pretrained
```


```
AutoTokenizer
```

### [torchaudio.load() requires torchcodec in 2.10+](https://docs.voicebox.sh/developer/tts-engines#torchaudioload-requires-torchcodec-in-210)
[torchaudio.load() requires torchcodec in 2.10+](https://docs.voicebox.sh/developer/tts-engines#torchaudioload-requires-torchcodec-in-210)

```
torchaudio.load()
```


```
torchcodec
```

As of torchaudio>=2.10, torchaudio.load() requires the torchcodec package for audio I/O. If your engine or backend code uses torchaudio.load(), replace it with soundfile:

```
torchaudio>=2.10
```


```
torchaudio.load()
```


```
torchcodec
```


```
torchaudio.load()
```


```
soundfile
```


```
# Before (breaks without torchcodec): import torchaudio waveform, sr = torchaudio.load("audio.wav") # After: import soundfile as sf import torch data, sr = sf.read("audio.wav", dtype="float32") waveform = torch.from_numpy(data).unsqueeze(0)
```


```
# Before (breaks without torchcodec): import torchaudio waveform, sr = torchaudio.load("audio.wav") # After: import soundfile as sf import torch data, sr = sf.read("audio.wav", dtype="float32") waveform = torch.from_numpy(data).unsqueeze(0)
```

Note: torchaudio.functional.resample() and other pure-PyTorch math functions work fine without torchcodec — only the I/O functions are affected.

```
torchaudio.functional.resample()
```


```
torchcodec
```

### [@torch.jit.script breaks in frozen builds](https://docs.voicebox.sh/developer/tts-engines#torchjitscript-breaks-in-frozen-builds)
[@torch.jit.script breaks in frozen builds](https://docs.voicebox.sh/developer/tts-engines#torchjitscript-breaks-in-frozen-builds)

```
@torch.jit.script
```

torch.jit.script calls inspect.getsource() to parse the decorated function's source code. In a PyInstaller binary, .py source files aren't available, so this crashes at import time.

```
torch.jit.script
```


```
inspect.getsource()
```


```
.py
```

Fix: Remove or avoid @torch.jit.script decorators. If the decorated function comes from an upstream dependency, write a shim that reimplements the function without the decorator (see "Toxic dependency chains" below).

```
@torch.jit.script
```

[Toxic dependency chains — the shim pattern](https://docs.voicebox.sh/developer/tts-engines#toxic-dependency-chains--the-shim-pattern)
Sometimes a model library depends on a package with a massive, hostile transitive dependency tree, but only uses a tiny piece of it. When the dependency chain is unbuildable or would pull in dozens of unwanted packages, the right move is to write a lightweight shim.
Example: TADA depends on descript-audio-codec (DAC), which pulls in descript-audiotools -> onnx, tensorboard, protobuf, matplotlib, pystoi, etc. The onnx package fails to build from source on macOS. But TADA only uses Snake1d from DAC — a 7-line PyTorch module.

```
descript-audio-codec
```


```
descript-audiotools
```


```
onnx
```


```
tensorboard
```


```
protobuf
```


```
matplotlib
```


```
pystoi
```


```
onnx
```


```
Snake1d
```

Solution: Create a shim at backend/utils/dac_shim.py that registers fake modules in sys.modules:

```
backend/utils/dac_shim.py
```


```
sys.modules
```


```
import sys import types import torch from torch import nn def snake(x, alpha): """Snake activation — reimplemented without @torch.jit.script.""" return x + (1.0 / (alpha + 1e-9)) * torch.sin(alpha * x).pow(2) class Snake1d(nn.Module): def __init__(self, channels): super().__init__() self.alpha = nn.Parameter(torch.ones(1, channels, 1)) def forward(self, x): return snake(x, self.alpha) # Register fake dac.* modules so "from dac.nn.layers import Snake1d" works _nn = types.ModuleType("dac.nn") _layers = types.ModuleType("dac.nn.layers") _layers.Snake1d = Snake1d _nn.layers = _layers for name, mod in [("dac", types.ModuleType("dac")), ("dac.nn", _nn), ("dac.nn.layers", _layers)]: sys.modules[name] = mod
```


```
import sys import types import torch from torch import nn def snake(x, alpha): """Snake activation — reimplemented without @torch.jit.script.""" return x + (1.0 / (alpha + 1e-9)) * torch.sin(alpha * x).pow(2) class Snake1d(nn.Module): def __init__(self, channels): super().__init__() self.alpha = nn.Parameter(torch.ones(1, channels, 1)) def forward(self, x): return snake(x, self.alpha) # Register fake dac.* modules so "from dac.nn.layers import Snake1d" works _nn = types.ModuleType("dac.nn") _layers = types.ModuleType("dac.nn.layers") _layers.Snake1d = Snake1d _nn.layers = _layers for name, mod in [("dac", types.ModuleType("dac")), ("dac.nn", _nn), ("dac.nn.layers", _layers)]: sys.modules[name] = mod
```

Key rules for shims:
- Import the shim before importing the model library (so it finds the fake modules first)
- Do NOT use @torch.jit.script in the shim (see above)
- Only reimplement what the model actually uses — check the import chain carefully

```
@torch.jit.script
```

## [Candidate Engines](https://docs.voicebox.sh/developer/tts-engines#candidate-engines)
[Candidate Engines](https://docs.voicebox.sh/developer/tts-engines#candidate-engines)
The [docs/PROJECT_STATUS.md](https://github.com/jamiepine/voicebox/blob/main/docs/PROJECT_STATUS.md) file is the canonical, living list of candidates under evaluation — including why some have been backlogged (e.g. VoxCPM, which is effectively CUDA-only upstream).

```
docs/PROJECT_STATUS.md
```

At a glance, current top candidates:

```
mistralai/Voxtral-4B-TTS-2603
```

Backlogged:
- VoxCPM (2B, Apache 2.0) — CUDA ≥12 required upstream; MPS broken in issues #232/#248; CPU path rejected by maintainers (#256). Keep watching for a PR that relaxes the device requirement.
Update PROJECT_STATUS.md when you pick one up or mark one as shipped/backlogged.

```
PROJECT_STATUS.md
```

## [Implementation Checklist](https://docs.voicebox.sh/developer/tts-engines#implementation-checklist)
[Implementation Checklist](https://docs.voicebox.sh/developer/tts-engines#implementation-checklist)
Use this as a gate between phases. Do not proceed to the next phase until every item in the current phase is checked.

### [Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research-1)
[Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research-1)
-  Cloned model library source into a temp directory
-  Read setup.py / pyproject.toml — noted pinned dependency versions
-  Traced all imports from the model class through to leaf dependencies
-  Searched for inspect.getsource, @typechecked, typeguard in the full dependency tree
-  Searched for importlib.metadata, pkg_resources.get_distribution in the dependency tree
-  Searched for Path(__file__).parent, os.path.dirname(__file__), hardcoded system paths
-  Searched for torch.load calls missing map_location
-  Searched for torch.from_numpy without .float() cast
-  Searched for token=True or token=os.getenv("HF_TOKEN") in HuggingFace calls
-  Searched for @torch.jit.script / torch.jit.script (crashes in frozen builds)
-  Searched for torchaudio.load / torchaudio.save (requires torchcodec in 2.10+)
-  Searched for hardcoded gated HuggingFace repo names (e.g., meta-llama/*)
-  Evaluated whether any dependency is used minimally enough to shim instead of install
-  Tested model loading and generation on CPU in a throwaway venv
-  Tested with a clean HuggingFace cache (no pre-downloaded models)
-  Produced a written dependency audit documenting all findings

```
setup.py
```


```
pyproject.toml
```


```
inspect.getsource
```


```
@typechecked
```


```
typeguard
```


```
importlib.metadata
```


```
pkg_resources.get_distribution
```


```
Path(__file__).parent
```


```
os.path.dirname(__file__)
```


```
torch.load
```


```
map_location
```


```
torch.from_numpy
```


```
.float()
```


```
token=True
```


```
token=os.getenv("HF_TOKEN")
```


```
@torch.jit.script
```


```
torch.jit.script
```


```
torchaudio.load
```


```
torchaudio.save
```


```
torchcodec
```


```
meta-llama/*
```

### [Phase 1: Backend Implementation](https://docs.voicebox.sh/developer/tts-engines#phase-1-backend-implementation-1)
[Phase 1: Backend Implementation](https://docs.voicebox.sh/developer/tts-engines#phase-1-backend-implementation-1)
-  Created backend/backends/<engine>_backend.py implementing TTSBackend protocol
-  Chose voice prompt pattern (pre-computed tensors vs deferred file paths)
-  Implemented all monkey-patches identified in Phase 0
-  Used get_torch_device() from backends/base.py for device selection
-  Used model_load_progress() from backends/base.py for download/load tracking
-  Tested: model downloads correctly
-  Tested: model loads on CPU
-  Tested: generation produces valid audio
-  Tested: voice cloning from reference audio works
-  Registered ModelConfig in backends/__init__.py
-  Added to TTS_ENGINES dict
-  Added factory branch in get_tts_backend_for_engine()
-  Updated engine regex in backend/models.py

```
backend/backends/<engine>_backend.py
```


```
TTSBackend
```


```
get_torch_device()
```


```
backends/base.py
```


```
model_load_progress()
```


```
backends/base.py
```


```
ModelConfig
```


```
backends/__init__.py
```


```
TTS_ENGINES
```


```
get_tts_backend_for_engine()
```


```
backend/models.py
```

### [Phase 2–3: Route, Service, and Frontend](https://docs.voicebox.sh/developer/tts-engines#phase-23-route-service-and-frontend)
[Phase 2–3: Route, Service, and Frontend](https://docs.voicebox.sh/developer/tts-engines#phase-23-route-service-and-frontend)
-  Confirmed zero changes needed in routes/services (or documented why custom behavior is needed)
-  Added engine to TypeScript union type in app/src/lib/api/types.ts
-  Added language map entry in app/src/lib/constants/languages.ts
-  Added to ENGINE_OPTIONS and ENGINE_DESCRIPTIONS in EngineModelSelector.tsx
-  Added to Zod schema and model-name mapping in useGenerationForm.ts
-  Added description in ModelManagement.tsx

```
app/src/lib/api/types.ts
```


```
app/src/lib/constants/languages.ts
```


```
ENGINE_OPTIONS
```


```
ENGINE_DESCRIPTIONS
```


```
EngineModelSelector.tsx
```


```
useGenerationForm.ts
```


```
ModelManagement.tsx
```

### [Phase 4: Dependencies](https://docs.voicebox.sh/developer/tts-engines#phase-4-dependencies-1)
[Phase 4: Dependencies](https://docs.voicebox.sh/developer/tts-engines#phase-4-dependencies-1)
-  Added packages to backend/requirements.txt
-  If --no-deps needed: listed sub-dependencies explicitly
-  If git-only packages: added @ git+https://... entries
-  If custom index needed: added --find-links line
-  Updated justfile setup targets
-  Updated .github/workflows/release.yml build steps
-  Updated Dockerfile if applicable
-  Verified pip install succeeds in a clean venv with existing requirements

```
backend/requirements.txt
```


```
--no-deps
```


```
@ git+https://...
```


```
--find-links
```


```
justfile
```


```
.github/workflows/release.yml
```


```
Dockerfile
```


```
pip install
```

### [Phase 5: PyInstaller Bundling](https://docs.voicebox.sh/developer/tts-engines#phase-5-pyinstaller-bundling)
[Phase 5: PyInstaller Bundling](https://docs.voicebox.sh/developer/tts-engines#phase-5-pyinstaller-bundling)
-  Added --hidden-import entries in build_binary.py for:

 backend.backends.<engine>_backend
 The model package and its key submodules


-  backend.backends.<engine>_backend
-  The model package and its key submodules
-  Added --collect-all for any packages that:

 Use inspect.getsource() / @typechecked
 Ship pretrained model data files (.pth.tar, .yaml, etc.)
 Ship native data files (phoneme tables, shader libraries, etc.)


-  Use inspect.getsource() / @typechecked
-  Ship pretrained model data files (.pth.tar, .yaml, etc.)
-  Ship native data files (phoneme tables, shader libraries, etc.)
-  Added --copy-metadata for any packages that use importlib.metadata
-  If engine has native data paths: added os.environ.setdefault() in server.py
-  Built frozen binary with just build
-  Tested in frozen binary with clean model cache (not pre-cached from dev):

 Model download works with real-time progress
 Model loading works
 Generation produces valid audio
 No errors in stderr logs


-  Model download works with real-time progress
-  Model loading works
-  Generation produces valid audio
-  No errors in stderr logs

```
--hidden-import
```


```
build_binary.py
```

-  backend.backends.<engine>_backend
-  The model package and its key submodules

```
backend.backends.<engine>_backend
```


```
--collect-all
```

-  Use inspect.getsource() / @typechecked
-  Ship pretrained model data files (.pth.tar, .yaml, etc.)
-  Ship native data files (phoneme tables, shader libraries, etc.)

```
inspect.getsource()
```


```
@typechecked
```


```
.pth.tar
```


```
.yaml
```


```
--copy-metadata
```


```
importlib.metadata
```


```
os.environ.setdefault()
```


```
server.py
```


```
just build
```

-  Model download works with real-time progress
-  Model loading works
-  Generation produces valid audio
-  No errors in stderr logs

### [Phase 6: Final Verification](https://docs.voicebox.sh/developer/tts-engines#phase-6-final-verification)
[Phase 6: Final Verification](https://docs.voicebox.sh/developer/tts-engines#phase-6-final-verification)
-  Engine works in dev mode (just dev)
-  Engine works in frozen binary (just build → run binary directly)
-  Tested on target platform (macOS for MLX, Windows/Linux for CUDA)
-  No regressions in existing engines

```
just dev
```


```
just build
```

[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/developer/tts-engines.mdx)
[TTS GenerationHow text-to-speech generation works across Voicebox's multi-engine backend](https://docs.voicebox.sh/developer/tts-generation)
TTS Generation
How text-to-speech generation works across Voicebox's multi-engine backend
[Effects PipelineAudio post-processing effects and generation versioning](https://docs.voicebox.sh/developer/effects-pipeline)
Effects Pipeline
Audio post-processing effects and generation versioning

[Architecture Overview](https://docs.voicebox.sh/developer/tts-engines#architecture-overview)
[Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research)
[0.1 Clone and Inspect the Model Library](https://docs.voicebox.sh/developer/tts-engines#01-clone-and-inspect-the-model-library)
[0.2 Scan for PyInstaller-Incompatible Patterns](https://docs.voicebox.sh/developer/tts-engines#02-scan-for-pyinstaller-incompatible-patterns)
[0.3 Install and Trace in a Throwaway Venv](https://docs.voicebox.sh/developer/tts-engines#03-install-and-trace-in-a-throwaway-venv)
[0.4 Test Model Loading on CPU](https://docs.voicebox.sh/developer/tts-engines#04-test-model-loading-on-cpu)
[0.5 Produce a Dependency Audit](https://docs.voicebox.sh/developer/tts-engines#05-produce-a-dependency-audit)
[Phase 1: Backend Implementation](https://docs.voicebox.sh/developer/tts-engines#phase-1-backend-implementation)
[1.1 Create the Backend File](https://docs.voicebox.sh/developer/tts-engines#11-create-the-backend-file)
[1.2 Voice Prompt Patterns](https://docs.voicebox.sh/developer/tts-engines#12-voice-prompt-patterns)
[1.3 Register the Engine](https://docs.voicebox.sh/developer/tts-engines#13-register-the-engine)
[1.4 Update Request Models](https://docs.voicebox.sh/developer/tts-engines#14-update-request-models)
[Phase 2: Route and Service Integration](https://docs.voicebox.sh/developer/tts-engines#phase-2-route-and-service-integration)
[Post-Processing](https://docs.voicebox.sh/developer/tts-engines#post-processing)
[Phase 3: Frontend Integration](https://docs.voicebox.sh/developer/tts-engines#phase-3-frontend-integration)
[3.1 TypeScript Types](https://docs.voicebox.sh/developer/tts-engines#31-typescript-types)
[3.2 Language Maps](https://docs.voicebox.sh/developer/tts-engines#32-language-maps)
[3.3 Engine/Model Selector](https://docs.voicebox.sh/developer/tts-engines#33-enginemodel-selector)
[3.4 Form Hook](https://docs.voicebox.sh/developer/tts-engines#34-form-hook)
[3.5 Model Management](https://docs.voicebox.sh/developer/tts-engines#35-model-management)
[3.6 Non-Cloning Engines (Preset Voices)](https://docs.voicebox.sh/developer/tts-engines#36-non-cloning-engines-preset-voices)
[Phase 4: Dependencies](https://docs.voicebox.sh/developer/tts-engines#phase-4-dependencies)
[4.1 Python Dependencies](https://docs.voicebox.sh/developer/tts-engines#41-python-dependencies)
[4.2 Dependency Conflict Resolution](https://docs.voicebox.sh/developer/tts-engines#42-dependency-conflict-resolution)
[4.3 Update Installation Scripts](https://docs.voicebox.sh/developer/tts-engines#43-update-installation-scripts)
[Phase 5: PyInstaller Bundling (build_binary.py)](https://docs.voicebox.sh/developer/tts-engines#phase-5-pyinstaller-bundling-build_binarypy)

```
build_binary.py
```

[5.1 Register Your Engine in build_binary.py](https://docs.voicebox.sh/developer/tts-engines#51-register-your-engine-in-build_binarypy)

```
build_binary.py
```

[5.2 Lessons from v0.2.3 — Real Failures and Their Fixes](https://docs.voicebox.sh/developer/tts-engines#52-lessons-from-v023--real-failures-and-their-fixes)
[5.3 Runtime Frozen-Build Handling (server.py)](https://docs.voicebox.sh/developer/tts-engines#53-runtime-frozen-build-handling-serverpy)

```
server.py
```

[5.4 CUDA vs CPU Build Branching](https://docs.voicebox.sh/developer/tts-engines#54-cuda-vs-cpu-build-branching)
[5.5 MLX Conditional Inclusion](https://docs.voicebox.sh/developer/tts-engines#55-mlx-conditional-inclusion)
[5.6 Testing Frozen Builds](https://docs.voicebox.sh/developer/tts-engines#56-testing-frozen-builds)
[Phase 6: Common Upstream Workarounds](https://docs.voicebox.sh/developer/tts-engines#phase-6-common-upstream-workarounds)
[torch.load device mismatch](https://docs.voicebox.sh/developer/tts-engines#torchload-device-mismatch)
[Float64/Float32 dtype mismatch](https://docs.voicebox.sh/developer/tts-engines#float64float32-dtype-mismatch)
[HuggingFace token bug](https://docs.voicebox.sh/developer/tts-engines#huggingface-token-bug)
[MPS tensor issues](https://docs.voicebox.sh/developer/tts-engines#mps-tensor-issues)
[Gated HuggingFace repos as hardcoded config sources](https://docs.voicebox.sh/developer/tts-engines#gated-huggingface-repos-as-hardcoded-config-sources)
[torchaudio.load() requires torchcodec in 2.10+](https://docs.voicebox.sh/developer/tts-engines#torchaudioload-requires-torchcodec-in-210)

```
torchaudio.load()
```


```
torchcodec
```

[@torch.jit.script breaks in frozen builds](https://docs.voicebox.sh/developer/tts-engines#torchjitscript-breaks-in-frozen-builds)

```
@torch.jit.script
```

[Toxic dependency chains — the shim pattern](https://docs.voicebox.sh/developer/tts-engines#toxic-dependency-chains--the-shim-pattern)
[Candidate Engines](https://docs.voicebox.sh/developer/tts-engines#candidate-engines)
[Implementation Checklist](https://docs.voicebox.sh/developer/tts-engines#implementation-checklist)
[Phase 0: Dependency Research](https://docs.voicebox.sh/developer/tts-engines#phase-0-dependency-research-1)
[Phase 1: Backend Implementation](https://docs.voicebox.sh/developer/tts-engines#phase-1-backend-implementation-1)
[Phase 2–3: Route, Service, and Frontend](https://docs.voicebox.sh/developer/tts-engines#phase-23-route-service-and-frontend)
[Phase 4: Dependencies](https://docs.voicebox.sh/developer/tts-engines#phase-4-dependencies-1)
[Phase 5: PyInstaller Bundling](https://docs.voicebox.sh/developer/tts-engines#phase-5-pyinstaller-bundling)
[Phase 6: Final Verification](https://docs.voicebox.sh/developer/tts-engines#phase-6-final-verification)

