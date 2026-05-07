Title: MCP Server

Description: Let Claude Code, Cursor, Cline, or any MCP-aware agent speak in one of your cloned voices — locally, with no cloud.

Source: https://docs.voicebox.sh/overview/mcp-server

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

Let Claude Code, Cursor, Cline, or any MCP-aware agent speak in one of your cloned voices — locally, with no cloud.

## [Overview](https://docs.voicebox.sh/overview/mcp-server#overview)
[Overview](https://docs.voicebox.sh/overview/mcp-server#overview)
Voicebox ships a built-in Model Context Protocol server so local AI agents can call your Voicebox install directly: speak text in a voice profile, transcribe audio, and list captures or profiles. The server runs inside the same process as the rest of Voicebox and is mounted at /mcp over Streamable HTTP.

```
/mcp
```

Agent asks to speak → Voicebox plays audio on your speakers → an on-screen pill surfaces the voice name for the whole duration so you always see what's coming out of your machine.
MCP shipped in 0.5.0 alongside [Dictation](https://docs.voicebox.sh/overview/dictation) and [Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities). The design goal is "local voice layer for every agent on your machine" — the same app that captures your voice can generate a response in any voice profile you've cloned.

## [Quick install](https://docs.voicebox.sh/overview/mcp-server#quick-install)
[Quick install](https://docs.voicebox.sh/overview/mcp-server#quick-install)

### [Claude Code](https://docs.voicebox.sh/overview/mcp-server#claude-code)
[Claude Code](https://docs.voicebox.sh/overview/mcp-server#claude-code)

```
claude mcp add voicebox \ --transport http \ --url http://127.0.0.1:17493/mcp \ --header "X-Voicebox-Client-Id: claude-code"
```


```
claude mcp add voicebox \ --transport http \ --url http://127.0.0.1:17493/mcp \ --header "X-Voicebox-Client-Id: claude-code"
```

### [Cursor / Windsurf / VS Code MCP / any HTTP MCP client](https://docs.voicebox.sh/overview/mcp-server#cursor--windsurf--vs-code-mcp--any-http-mcp-client)
[Cursor / Windsurf / VS Code MCP / any HTTP MCP client](https://docs.voicebox.sh/overview/mcp-server#cursor--windsurf--vs-code-mcp--any-http-mcp-client)
Drop this into the client's MCP config (usually .mcp.json or a Settings UI):

```
.mcp.json
```


```
{ "mcpServers": { "voicebox": { "url": "http://127.0.0.1:17493/mcp", "headers": { "X-Voicebox-Client-Id": "cursor" } } } }
```


```
{ "mcpServers": { "voicebox": { "url": "http://127.0.0.1:17493/mcp", "headers": { "X-Voicebox-Client-Id": "cursor" } } } }
```

Change cursor to whatever name you want the binding to show up as in Voicebox → Settings → MCP. The value is just an identifier for the per-client voice binding — not a secret, not a credential.

```
cursor
```

### [Clients that only speak stdio](https://docs.voicebox.sh/overview/mcp-server#clients-that-only-speak-stdio)
[Clients that only speak stdio](https://docs.voicebox.sh/overview/mcp-server#clients-that-only-speak-stdio)
A stdio shim binary voicebox-mcp is bundled with the desktop app. Point the client at that binary's absolute path:

```
voicebox-mcp
```


```
{ "mcpServers": { "voicebox": { "command": "/Applications/Voicebox.app/Contents/MacOS/voicebox-mcp", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```


```
{ "mcpServers": { "voicebox": { "command": "/Applications/Voicebox.app/Contents/MacOS/voicebox-mcp", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```


```
{ "mcpServers": { "voicebox": { "command": "C:\\Program Files\\Voicebox\\voicebox-mcp.exe", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```


```
{ "mcpServers": { "voicebox": { "command": "C:\\Program Files\\Voicebox\\voicebox-mcp.exe", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```


```
{ "mcpServers": { "voicebox": { "command": "/opt/voicebox/voicebox-mcp", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```


```
{ "mcpServers": { "voicebox": { "command": "/opt/voicebox/voicebox-mcp", "env": { "VOICEBOX_CLIENT_ID": "claude-desktop" } } } }
```

The shim waits up to 30 seconds for the Voicebox backend to come up, then proxies JSON-RPC from stdio over Streamable HTTP. Voicebox must be running for the shim to connect.

[Tools](https://docs.voicebox.sh/overview/mcp-server#tools)

```
voicebox.speak
```


```
generation_id
```


```
voicebox.transcribe
```


```
voicebox.list_captures
```


```
voicebox.list_profiles
```

### [voicebox.speak](https://docs.voicebox.sh/overview/mcp-server#voiceboxspeak)
[voicebox.speak](https://docs.voicebox.sh/overview/mcp-server#voiceboxspeak)

```
voicebox.speak
```


```
voicebox.speak({ text: "Deploy complete.", profile?: "Morgan", // name or id; falls back to per-client binding, then default engine?: "qwen", // qwen | qwen_custom_voice | luxtts | chatterbox | chatterbox_turbo | tada | kokoro personality?: true, // rewrite via the profile's personality LLM before TTS; default comes from the per-client binding language?: "en", })
```


```
voicebox.speak({ text: "Deploy complete.", profile?: "Morgan", // name or id; falls back to per-client binding, then default engine?: "qwen", // qwen | qwen_custom_voice | luxtts | chatterbox | chatterbox_turbo | tada | kokoro personality?: true, // rewrite via the profile's personality LLM before TTS; default comes from the per-client binding language?: "en", })
```

Returns:

```
{ "generation_id": "…", "status": "generating", "profile": "Morgan", "source": "mcp", "poll_url": "/generate/<id>/status" }
```


```
{ "generation_id": "…", "status": "generating", "profile": "Morgan", "source": "mcp", "poll_url": "/generate/<id>/status" }
```

- Plain TTS — personality: false (or omitted + binding default is false). Text is spoken as-is.
- Persona mode — personality: true and the profile must have a personality prompt set.
The LLM rewrites the text in character before TTS. See [Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities).

```
personality: false
```


```
personality: true
```

[Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities)

### [voicebox.transcribe](https://docs.voicebox.sh/overview/mcp-server#voiceboxtranscribe)
[voicebox.transcribe](https://docs.voicebox.sh/overview/mcp-server#voiceboxtranscribe)

```
voicebox.transcribe
```


```
voicebox.transcribe({ audio_base64?: "<base64>", // exactly one of these two audio_path?: "/absolute/path/to/file.wav", language?: "en", model?: "turbo", // base | small | medium | large | turbo })
```


```
voicebox.transcribe({ audio_base64?: "<base64>", // exactly one of these two audio_path?: "/absolute/path/to/file.wav", language?: "en", model?: "turbo", // base | small | medium | large | turbo })
```

Returns { text, duration, language, model }. 200 MB ceiling on either path.

```
{ text, duration, language, model }
```

### [voicebox.list_captures](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_captures)
[voicebox.list_captures](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_captures)

```
voicebox.list_captures
```

{ limit?: 20, offset?: 0 } → { captures: [...], total }. limit is clamped to 1..=200.

```
{ limit?: 20, offset?: 0 }
```


```
{ captures: [...], total }
```


```
limit
```


```
1..=200
```

### [voicebox.list_profiles](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_profiles)
[voicebox.list_profiles](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_profiles)

```
voicebox.list_profiles
```

No args → { profiles: [{ id, name, voice_type, language, has_personality }] }.

```
{ profiles: [{ id, name, voice_type, language, has_personality }] }
```

## [Voice resolution](https://docs.voicebox.sh/overview/mcp-server#voice-resolution)
[Voice resolution](https://docs.voicebox.sh/overview/mcp-server#voice-resolution)
Every call to voicebox.speak (and POST /speak) resolves the voice profile in this order:

```
voicebox.speak
```


```
POST /speak
```

Passed as a name (case-insensitive) or id. If the name/id doesn't match, the call errors — the server doesn't silently fall back.
Looked up by the X-Voicebox-Client-Id header. Managed in Voicebox → Settings → MCP. Lets you pin Claude Code to Morgan, Cursor to Scarlett, etc.

```
X-Voicebox-Client-Id
```

capture_settings.default_playback_voice_id — same default voice the Captures tab's "Play as voice" action uses.

```
capture_settings.default_playback_voice_id
```

If none of the three produce a profile the tool returns a helpful error pointing at Settings.

## [Per-client bindings](https://docs.voicebox.sh/overview/mcp-server#per-client-bindings)
[Per-client bindings](https://docs.voicebox.sh/overview/mcp-server#per-client-bindings)
Voicebox → Settings → MCP shows one row per client_id Voicebox has heard from, plus the config snippets you can copy into each agent. Each row carries:

```
client_id
```


```
label
```


```
profile_id
```


```
profile
```


```
default_engine
```


```
default_personality
```


```
voicebox.speak
```


```
last_seen_at
```

last_seen_at is stamped automatically by middleware on every /mcp/* request — useful when you're not sure whether your config took.

```
last_seen_at
```


```
/mcp/*
```

## [The speaking pill](https://docs.voicebox.sh/overview/mcp-server#the-speaking-pill)
[The speaking pill](https://docs.voicebox.sh/overview/mcp-server#the-speaking-pill)
Every agent-initiated speak surfaces the floating pill the same way [Dictation](https://docs.voicebox.sh/overview/dictation) does, in a new Speaking state showing the profile name and an elapsed timer. The pill is intentionally unmissable — silent background TTS is a trust hazard, so Voicebox always shows what's being spoken and in what voice.

```
Speaking
```

Behind the scenes, the backend broadcasts speak-start and speak-end events on GET /events/speak, which DictateWindow subscribes to via SSE. The pill overrides the capture session when both would render — you can't hear two pills at once.

```
speak-start
```


```
speak-end
```


```
GET /events/speak
```


```
DictateWindow
```

## [Non-MCP REST surface](https://docs.voicebox.sh/overview/mcp-server#non-mcp-rest-surface)
[Non-MCP REST surface](https://docs.voicebox.sh/overview/mcp-server#non-mcp-rest-surface)
POST /speak is a thin wrapper on the same code path for callers that don't speak MCP — shell scripts, ACP, A2A, GitHub Actions, whatever.

```
POST /speak
```


```
curl -X POST http://127.0.0.1:17493/speak \ -H 'Content-Type: application/json' \ -H 'X-Voicebox-Client-Id: ci' \ -d '{"text":"Build complete.","profile":"Morgan"}'
```


```
curl -X POST http://127.0.0.1:17493/speak \ -H 'Content-Type: application/json' \ -H 'X-Voicebox-Client-Id: ci' \ -d '{"text":"Build complete.","profile":"Morgan"}'
```

Body fields match the MCP tool: text, optional profile, engine, personality, language. Returns a GenerationResponse — the same shape as POST /generate.

```
text
```


```
profile
```


```
engine
```


```
personality
```


```
language
```


```
GenerationResponse
```


```
POST /generate
```

## [Debugging](https://docs.voicebox.sh/overview/mcp-server#debugging)
[Debugging](https://docs.voicebox.sh/overview/mcp-server#debugging)
Use the MCP Inspector to poke tools directly without plumbing through an agent:

```
npx @modelcontextprotocol/inspector http://127.0.0.1:17493/mcp
```


```
npx @modelcontextprotocol/inspector http://127.0.0.1:17493/mcp
```

Start with voicebox.list_profiles to confirm wiring, then voicebox.speak for end-to-end — you should hear audio and see the generation land in the Captures tab.

```
voicebox.list_profiles
```


```
voicebox.speak
```

If an agent can't reach the server, the first thing to check is that Voicebox is running — the backend only listens while the desktop app is open. The stdio shim surfaces this as a JSON-RPC error on the client side after its 30-second health-wait window elapses.

## [Security](https://docs.voicebox.sh/overview/mcp-server#security)
[Security](https://docs.voicebox.sh/overview/mcp-server#security)
- Localhost only. The server binds to 127.0.0.1. If you ever point
Voicebox at a non-loopback interface (e.g. remote-mode over a trusted
network), add a bearer token — it's on the roadmap but not in 0.5.0.
- No auth today. Any process that can connect to your loopback can
call MCP. That's the same trust boundary as the rest of Voicebox's REST
API and is appropriate for a single-user local tool.
- audio_path reads are unrestricted against the same trust
boundary. If you're scripting against a shared host, prefer
audio_base64 so you don't have to think about path sandboxing.
- Voice cloning consent applies. See [Voice Cloning](https://docs.voicebox.sh/overview/voice-cloning#limitations)
— an agent being able to call voicebox.speak in someone's voice
doesn't change the ethics of whose voices you clone.

```
127.0.0.1
```


```
audio_path
```


```
audio_base64
```

[Voice Cloning](https://docs.voicebox.sh/overview/voice-cloning#limitations)

```
voicebox.speak
```

## [Implementation notes](https://docs.voicebox.sh/overview/mcp-server#implementation-notes)
[Implementation notes](https://docs.voicebox.sh/overview/mcp-server#implementation-notes)
- Transport: Streamable HTTP (Nov-2025 MCP spec, post-SSE). Claude
Code, Cursor, Windsurf, and VS Code MCP extensions all support it.
- Package naming: the backend package is backend/mcp_server/, not
mcp, to avoid shadowing the PyPI mcp package FastMCP imports
internally.
- Dependencies: fastmcp>=3.0,<4.0, sse-starlette>=2.0.
- Lifespan: mounting FastMCP requires the lifespan= kwarg on
FastAPI() — the startup/shutdown event decorators are incompatible
with FastMCP's Streamable HTTP session manager. The Voicebox app.py
composes both into one async context manager.

```
backend/mcp_server/
```


```
mcp
```


```
mcp
```


```
fastmcp>=3.0,<4.0
```


```
sse-starlette>=2.0
```


```
lifespan=
```


```
FastAPI()
```

For the full developer-facing tour of the code layout, see backend/mcp_server/README.md in the repo.

```
backend/mcp_server/README.md
```

## [Next steps](https://docs.voicebox.sh/overview/mcp-server#next-steps)
[Next steps](https://docs.voicebox.sh/overview/mcp-server#next-steps)
[Voice PersonalitiesPersona mode (personality: true) for agents that should
transform text in-character before speaking.](https://docs.voicebox.sh/overview/voice-personalities)

### Voice Personalities
Persona mode (personality: true) for agents that should transform text in-character before speaking.

```
personality: true
```

[DictationThe pill that surfaces agent speech is the same one that surfaces
your dictations — one mental model for both directions of the loop.](https://docs.voicebox.sh/overview/dictation)

### Dictation
The pill that surfaces agent speech is the same one that surfaces your dictations — one mental model for both directions of the loop.
[CapturesEvery agent-initiated speak lands in the Captures tab with its
generated audio — replay, download, repurpose.](https://docs.voicebox.sh/overview/captures)

### Captures
Every agent-initiated speak lands in the Captures tab with its generated audio — replay, download, repurpose.
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/mcp-server.mdx)
[Voice PersonalitiesAttach a personality to a voice profile, compose fresh in-character lines, and rewrite input text in their voice — all powered by a local LLM.](https://docs.voicebox.sh/overview/voice-personalities)
Voice Personalities
Attach a personality to a voice profile, compose fresh in-character lines, and rewrite input text in their voice — all powered by a local LLM.
[Stories EditorCreate multi-voice narratives with a timeline-based editor](https://docs.voicebox.sh/overview/stories-editor)
Stories Editor
Create multi-voice narratives with a timeline-based editor

### On this page
[Overview](https://docs.voicebox.sh/overview/mcp-server#overview)
[Quick install](https://docs.voicebox.sh/overview/mcp-server#quick-install)
[Claude Code](https://docs.voicebox.sh/overview/mcp-server#claude-code)
[Cursor / Windsurf / VS Code MCP / any HTTP MCP client](https://docs.voicebox.sh/overview/mcp-server#cursor--windsurf--vs-code-mcp--any-http-mcp-client)
[Clients that only speak stdio](https://docs.voicebox.sh/overview/mcp-server#clients-that-only-speak-stdio)
[Tools](https://docs.voicebox.sh/overview/mcp-server#tools)
[voicebox.speak](https://docs.voicebox.sh/overview/mcp-server#voiceboxspeak)

```
voicebox.speak
```

[voicebox.transcribe](https://docs.voicebox.sh/overview/mcp-server#voiceboxtranscribe)

```
voicebox.transcribe
```

[voicebox.list_captures](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_captures)

```
voicebox.list_captures
```

[voicebox.list_profiles](https://docs.voicebox.sh/overview/mcp-server#voiceboxlist_profiles)

```
voicebox.list_profiles
```

[Voice resolution](https://docs.voicebox.sh/overview/mcp-server#voice-resolution)
[Per-client bindings](https://docs.voicebox.sh/overview/mcp-server#per-client-bindings)
[The speaking pill](https://docs.voicebox.sh/overview/mcp-server#the-speaking-pill)
[Non-MCP REST surface](https://docs.voicebox.sh/overview/mcp-server#non-mcp-rest-surface)
[Debugging](https://docs.voicebox.sh/overview/mcp-server#debugging)
[Security](https://docs.voicebox.sh/overview/mcp-server#security)
[Implementation notes](https://docs.voicebox.sh/overview/mcp-server#implementation-notes)
[Next steps](https://docs.voicebox.sh/overview/mcp-server#next-steps)

