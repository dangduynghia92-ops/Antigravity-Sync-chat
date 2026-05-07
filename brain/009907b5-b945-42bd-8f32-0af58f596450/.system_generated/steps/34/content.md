Title: Voice Personalities

Description: Attach a personality to a voice profile, compose fresh in-character lines, and rewrite input text in their voice — all powered by a local LLM.

Source: https://docs.voicebox.sh/overview/voice-personalities

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

Attach a personality to a voice profile, compose fresh in-character lines, and rewrite input text in their voice — all powered by a local LLM.

## [Overview](https://docs.voicebox.sh/overview/voice-personalities#overview)
[Overview](https://docs.voicebox.sh/overview/voice-personalities#overview)
A personality is an optional free-form description attached to a voice profile — who this voice is, how they speak, what they care about. Set one and two new controls appear next to the generate button, both powered by a bundled Qwen3 LLM running entirely locally:
- Compose — drop a fresh in-character line into the textarea. Click
again for a different take.
- Speak in character — a toggle that rewrites your input text in the
character's voice before TTS, preserving every idea.
The LLM produces the text. The voice profile speaks it. No cloud round-trip, no external API — the whole loop runs on your hardware.
Personalities shipped in 0.5.0. The same local LLM doubles as the refinement model for [Dictation](https://docs.voicebox.sh/overview/dictation) — one LLM in the app, not two, sharing one model cache and one GPU-memory footprint.

## [Setting a personality](https://docs.voicebox.sh/overview/voice-personalities#setting-a-personality)
[Setting a personality](https://docs.voicebox.sh/overview/voice-personalities#setting-a-personality)
Open a voice profile's edit view. The Personality field is free-form text up to 2,000 characters. Describe the voice however helps you — past lines they'd say, speech patterns, tone, boundaries.
Good descriptions tend to include:
- A one-line identity (who they are)
- Speech patterns (rhythm, vocabulary, what they avoid)
- Representative phrases — example lines show the LLM the target tone
better than adjectives
- What the character wouldn't do (they don't explain, they don't
apologize, they refuse to break character, etc.)
You can set a personality on any voice profile type — cloned or preset. The three modes work identically regardless of engine.

## [The two actions](https://docs.voicebox.sh/overview/voice-personalities#the-two-actions)
[The two actions](https://docs.voicebox.sh/overview/voice-personalities#the-two-actions)
Each action is tuned for a specific job and the LLM temperature is adjusted to match.

### [Compose](https://docs.voicebox.sh/overview/voice-personalities#compose)
[Compose](https://docs.voicebox.sh/overview/voice-personalities#compose)
Generate a fresh utterance in the character's voice, with no seed text. Click the shuffle button to drop a line straight into the generate textarea; click again for a different take.
- When to use: prototyping, sampling a character's voice, brainstorming
a line without typing one first
- Temperature: hot — variety is the point
- Typical output: a short, punchy line that fits the character's
register

### [Speak in character (rewrite)](https://docs.voicebox.sh/overview/voice-personalities#speak-in-character-rewrite)
[Speak in character (rewrite)](https://docs.voicebox.sh/overview/voice-personalities#speak-in-character-rewrite)
Flip the persona toggle and whatever you type (or dictate) gets rewritten in the character's voice before TTS — every idea preserved, only the phrasing changes. High-fidelity mode: the content doesn't change, only the voice does.
- When to use: turning a dictated memo into in-character speech; lifting
a plain-English script into a specific voice without editing by hand
- Temperature: cold — faithfulness wins
- Typical output: same ideas, same order, different phrasing and cadence

## [Speech-only framing](https://docs.voicebox.sh/overview/voice-personalities#speech-only-framing)
[Speech-only framing](https://docs.voicebox.sh/overview/voice-personalities#speech-only-framing)
Both modes enforce speech-only output. The LLM is prompted to produce things a person would actually say out loud — no narration, no action tags (*sighs*, [laughs]), no meta-commentary, no markdown formatting, no stage directions.

```
*sighs*
```


```
[laughs]
```

This is deliberate: the output is going straight into TTS, and anything that isn't speakable ends up either ignored or read literally. The speech-only framing also makes the output land cleanly inside dialogue, so you can drop a Respond result straight into a Story.

## [The local LLM](https://docs.voicebox.sh/overview/voice-personalities#the-local-llm)
[The local LLM](https://docs.voicebox.sh/overview/voice-personalities#the-local-llm)
The bundled LLM is Qwen3, available in three sizes:
The model runs through the same backend split Voicebox already uses for TTS — MLX (4-bit community quants) on Apple Silicon, PyTorch (transformers AutoModelForCausalLM) everywhere else. Downloads go through the same cache and model-management UI as TTS models.

```
AutoModelForCausalLM
```

Pick a size in Settings → Captures → Refinement → Refinement model — the personality modes reuse it. If you switch models, both refinement and personality output pick up the change on the next call.

## [Using the controls](https://docs.voicebox.sh/overview/voice-personalities#using-the-controls)
[Using the controls](https://docs.voicebox.sh/overview/voice-personalities#using-the-controls)
Both controls appear on the floating generate box when the selected profile has a personality set.
Click the shuffle button. The LLM runs and the result fills the generate textarea. Edit if you want, then hit generate.
Type (or dictate) what you want said. Flip the wand toggle on. Hit generate — Voicebox runs the text through the personality LLM first, then TTS speaks the rewritten version. Leave the toggle off for plain TTS.
Compose always gives you something different on re-click. The persona toggle, on the other hand, is a mode — it applies to every generate call until you flip it back off.

## [Use cases](https://docs.voicebox.sh/overview/voice-personalities#use-cases)
[Use cases](https://docs.voicebox.sh/overview/voice-personalities#use-cases)
- Agents that speak in a voice you own. Combine the persona toggle with
the built-in [MCP Server](https://docs.voicebox.sh/overview/mcp-server) so Claude Code, Cursor,
Cline, or any MCP-aware agent can talk back through a profile with a
personality. The agent calls voicebox.speak({ text, profile, personality: true }) and Voicebox rewrites the text in character before speaking.
- Interactive characters. Games, narrative tools, accessibility
experiences. A character with a personality description plus a cloned
voice becomes a reusable prop.
- Accessibility. People who can't speak in their original voice can
keep a personality description of how they used to sound and use the
rewrite toggle to turn typed input into in-character speech.
- Creative drafting. Write a plain outline, flip the persona toggle,
generate line-by-line into the character's voice, drop the audio into a
Story.
[MCP Server](https://docs.voicebox.sh/overview/mcp-server)

```
voicebox.speak({ text, profile, personality: true })
```

## [API surface](https://docs.voicebox.sh/overview/voice-personalities#api-surface)
[API surface](https://docs.voicebox.sh/overview/voice-personalities#api-surface)
Personalities are accessible via REST:

```
PUT
```


```
/profiles/{id}
```


```
personality
```


```
POST
```


```
/profiles/{id}/compose
```


```
POST
```


```
/generate
```


```
personality: true
```


```
POST /speak
```

POST /generate with personality: true is the same primitive MCP's voicebox.speak tool uses when you pass personality: true. Scripts and agents can use it directly.

```
POST /generate
```


```
personality: true
```


```
voicebox.speak
```


```
personality: true
```

## [Limits and gotchas](https://docs.voicebox.sh/overview/voice-personalities#limits-and-gotchas)
[Limits and gotchas](https://docs.voicebox.sh/overview/voice-personalities#limits-and-gotchas)
- The personality is a prompt, not a fine-tune. The LLM will sometimes
drift out of character, especially on Compose at high temperature. Click
again for another take.
- Long personalities are not always better. 2,000 chars is a ceiling,
not a goal. A sharp 300-char description with two example lines
typically outperforms a long one.
- Speech-only framing is enforced, but not bulletproof. Very large
prompts or unusual inputs can sneak an action tag through. If you see
[laughs] in TTS output, it's usually a personality-field hint the
model anchored onto — remove it from the description.
- Rewrite is stricter than Respond. If the output is changing your
meaning, you probably want Respond (or a wholesale Compose with context
in the input), not Rewrite.

```
[laughs]
```

## [Next steps](https://docs.voicebox.sh/overview/voice-personalities#next-steps)
[Next steps](https://docs.voicebox.sh/overview/voice-personalities#next-steps)
[DictationDictate the input for Rewrite or Respond from anywhere on your machine.](https://docs.voicebox.sh/overview/dictation)

### Dictation
Dictate the input for Rewrite or Respond from anywhere on your machine.
[CapturesCaptures feed personalities naturally — dictate a memo, rewrite it in
a character voice, generate speech.](https://docs.voicebox.sh/overview/captures)

### Captures
Captures feed personalities naturally — dictate a memo, rewrite it in a character voice, generate speech.
[Creating Voice ProfilesAdd a personality to an existing profile.](https://docs.voicebox.sh/overview/creating-voice-profiles)

### Creating Voice Profiles
Add a personality to an existing profile.
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/voice-personalities.mdx)
[Preset VoicesUse built-in, ready-made voices without recording audio samples](https://docs.voicebox.sh/overview/preset-voices)
Preset Voices
Use built-in, ready-made voices without recording audio samples
[MCP ServerLet Claude Code, Cursor, Cline, or any MCP-aware agent speak in one of your cloned voices — locally, with no cloud.](https://docs.voicebox.sh/overview/mcp-server)
MCP Server
Let Claude Code, Cursor, Cline, or any MCP-aware agent speak in one of your cloned voices — locally, with no cloud.

### On this page
[Overview](https://docs.voicebox.sh/overview/voice-personalities#overview)
[Setting a personality](https://docs.voicebox.sh/overview/voice-personalities#setting-a-personality)
[The two actions](https://docs.voicebox.sh/overview/voice-personalities#the-two-actions)
[Compose](https://docs.voicebox.sh/overview/voice-personalities#compose)
[Speak in character (rewrite)](https://docs.voicebox.sh/overview/voice-personalities#speak-in-character-rewrite)
[Speech-only framing](https://docs.voicebox.sh/overview/voice-personalities#speech-only-framing)
[The local LLM](https://docs.voicebox.sh/overview/voice-personalities#the-local-llm)
[Using the controls](https://docs.voicebox.sh/overview/voice-personalities#using-the-controls)
[Use cases](https://docs.voicebox.sh/overview/voice-personalities#use-cases)
[API surface](https://docs.voicebox.sh/overview/voice-personalities#api-surface)
[Limits and gotchas](https://docs.voicebox.sh/overview/voice-personalities#limits-and-gotchas)
[Next steps](https://docs.voicebox.sh/overview/voice-personalities#next-steps)

