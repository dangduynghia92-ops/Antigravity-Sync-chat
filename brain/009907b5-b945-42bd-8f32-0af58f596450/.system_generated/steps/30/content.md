Title: Dictation

Description: Hold a key anywhere on your machine, speak, release — the transcript lands in whatever text field you had focused.

Source: https://docs.voicebox.sh/overview/dictation

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

Hold a key anywhere on your machine, speak, release — the transcript lands in whatever text field you had focused.

## [Overview](https://docs.voicebox.sh/overview/dictation#overview)
[Overview](https://docs.voicebox.sh/overview/dictation#overview)
Dictation lets you turn speech into clean text anywhere on your computer. Hold a chord, talk, release — Voicebox transcribes what you said with Whisper, optionally cleans it up with a local LLM, and pastes the result into the text field you had focused when you started.
Everything happens on your hardware. No cloud, no accounts, no audio leaving the machine.
Dictation was introduced in 0.5.0 alongside the Captures tab and the per-profile personality modes. It's the "input" half of Voicebox's voice I/O loop — cloning and TTS are still the "output" half.

## [The flow](https://docs.voicebox.sh/overview/dictation#the-flow)
[The flow](https://docs.voicebox.sh/overview/dictation#the-flow)
Hold the push-to-talk chord anywhere on your machine. A small pill fades in over your current app.
The pill shows Recording with a live waveform and an elapsed-time counter. Speak naturally — you don't have to wait for anything.

```
Recording
```

On release, the pill flips to Transcribing, then Refining if auto-refine is on, then disappears.

```
Transcribing
```


```
Refining
```

If auto-paste is enabled and Voicebox has Accessibility permission, the transcript pastes into the text field you had focused when you started talking — not wherever focus drifted while you were speaking.
Either way, every capture also appears in the [Captures](https://docs.voicebox.sh/overview/captures) tab with the original audio and the transcript paired together. See Captures for what you can do with them after the fact.

## [Push-to-talk and toggle modes](https://docs.voicebox.sh/overview/dictation#push-to-talk-and-toggle-modes)
[Push-to-talk and toggle modes](https://docs.voicebox.sh/overview/dictation#push-to-talk-and-toggle-modes)
Voicebox ships two chord behaviors out of the box:

```
⌘
```


```
⌥
```


```
Ctrl
```


```
Shift
```


```
Space
```


```
Space
```

Holding PTT and tapping Space mid-hold upgrades a hold into a toggled session without a gap in the audio. This is the single most useful detail of the chord system — short bursts feel fast, long-form narration feels hands-free, and there's no decision up front about which mode you wanted.

```
Space
```

## [The on-screen pill](https://docs.voicebox.sh/overview/dictation#the-on-screen-pill)
[The on-screen pill](https://docs.voicebox.sh/overview/dictation#the-on-screen-pill)
While you're dictating, a floating pill appears over the current app. It walks through the states of the capture cycle and shows live signals for each:

```
Recording
```


```
Transcribing
```


```
Refining
```

The pill is transparent, always-on-top, and pre-created hidden at app start — so it appears instantly when you hit the chord, with no window flash.

## [Customizing the chord](https://docs.voicebox.sh/overview/dictation#customizing-the-chord)
[Customizing the chord](https://docs.voicebox.sh/overview/dictation#customizing-the-chord)
Open Settings → Captures → Dictation to change either chord.
- Left vs right modifier badges. When you hold keys into the chord
picker, Voicebox records whether each modifier is the left or right variant.
That means you can bind to just the right ⌥ while leaving the left ⌥
alone — useful if you want dictation on one hand and keep your
other-hand shortcuts intact.
- Chord defaults are picked to stay out of your way. On macOS, the
defaults deliberately avoid left-hand Cmd+Option chords so
Cmd+Option+I (devtools), Cmd+Option+Esc (force quit), and
Cmd+Option+Space (Spotlight) all remain yours. On Windows, the defaults
route around AltGr collisions on German / French / Spanish layouts where
Ctrl+Alt synthesizes AltGr.
- Live reload. Changing a chord in Settings takes effect immediately —
no restart, no tab reload.

```
⌥
```


```
⌥
```


```
Cmd+Option
```


```
Cmd+Option+I
```


```
Cmd+Option+Esc
```


```
Cmd+Option+Space
```


```
Ctrl+Alt
```

## [Auto-paste into the focused app](https://docs.voicebox.sh/overview/dictation#auto-paste-into-the-focused-app)
[Auto-paste into the focused app](https://docs.voicebox.sh/overview/dictation#auto-paste-into-the-focused-app)
Once transcription finishes, Voicebox can synthesize a native paste into whatever text field had focus when you started the chord. Your clipboard is saved before and restored after, so nothing you had copied goes missing.

```
CGEventPost
```


```
⌘V
```


```
NSRunningApplication
```


```
SendInput
```


```
SetForegroundWindow
```


```
AttachThreadInput
```

Focus is snapshotted at chord-start. The paste targets the original field even if focus drifts during transcribe / refine — that's the "pastes where you were talking from, not where you're looking now" behavior.
Auto-paste is optional. If Accessibility permission isn't granted (macOS), or you prefer to keep synthetic input off, dictation still runs — transcripts land in the Captures tab and you can copy them manually. The setting lives inline next to the Accessibility prompt in Settings → Captures → Dictation, not as a global banner.

## [Refinement](https://docs.voicebox.sh/overview/dictation#refinement)
[Refinement](https://docs.voicebox.sh/overview/dictation#refinement)
If auto-refine is on, a local LLM cleans up the raw Whisper transcript before it's pasted. The goal is to remove verbal clutter without rewriting what you actually said.
What refinement typically fixes:
- Filler words (um, uh, like used as pauses, you know)
- Self-corrections — the LLM keeps the final version and drops earlier
attempts (could you uh run the migration real quick, and then, yeah, check the logs → Could you run the migration, then check the logs?)
- Basic punctuation and capitalization
- Whisper loop hallucinations — Voicebox strips repeated tokens (six or
more identical tokens in a row, case-insensitive) before the LLM
sees the transcript, so a small refinement model can't echo them back

```
um
```


```
uh
```


```
like
```


```
you know
```


```
could you uh run the migration real quick, and then, yeah, check the logs
```


```
Could you run the migration, then check the logs?
```

What refinement deliberately preserves:
- Technical terms and code identifiers (npm install, handleSubmit)
- Legitimate repetition (no, no, no, no, no has fewer than six identical
tokens, so it survives)
- Your intent — refinement is cleanup, not rewriting

```
npm install
```


```
handleSubmit
```


```
no, no, no, no, no
```

Flags are snapshotted per capture, so you can re-refine the same raw transcript later with different flags without losing the original. The refinement model picker (Settings → Captures → Refinement) offers three bundled Qwen3 sizes:
This is the same local LLM used by the per-profile personality modes — one LLM in the app, not two. See [Voice Personalities](https://docs.voicebox.sh/overview/voice-personalities).

## [Platform notes](https://docs.voicebox.sh/overview/dictation#platform-notes)
[Platform notes](https://docs.voicebox.sh/overview/dictation#platform-notes)

### [macOS](https://docs.voicebox.sh/overview/dictation#macos)
[macOS](https://docs.voicebox.sh/overview/dictation#macos)
- Accessibility permission is required for auto-paste. The prompt lives
inline next to the toggle in Settings → Captures → Dictation, with a
deep link to System Settings → Privacy & Security → Accessibility.
- TSM crash mitigation. The global hotkey listener runs on a background
thread with set_is_main_thread(false) to sidestep a known
macOS 14+ crash in the rdev library. If you hit an unexpected dictation
failure on macOS, check the logs for TSM-related messages.

```
set_is_main_thread(false)
```


```
rdev
```

### [Windows](https://docs.voicebox.sh/overview/dictation#windows)
[Windows](https://docs.voicebox.sh/overview/dictation#windows)
- UAC / UIPI caveat. Synthetic paste into an elevated window from a
non-elevated Voicebox is blocked by Windows itself. Run Voicebox elevated
if you regularly dictate into elevated apps (e.g. an elevated terminal or
Task Manager).
- Right-hand default chord (Ctrl+Shift) avoids AltGr collisions on
keyboard layouts where Ctrl+Alt is the compose key (German, French,
Spanish, some others).

```
Ctrl+Shift
```


```
Ctrl+Alt
```

### [Linux](https://docs.voicebox.sh/overview/dictation#linux)
[Linux](https://docs.voicebox.sh/overview/dictation#linux)
- Not yet in this release. The Rust shim ships the macOS and Windows
paths in 0.5.0. Linux uinput / AT-SPI support and the Wayland paste
story are tracked in docs/plans/VOICE_IO.md.

```
uinput
```


```
docs/plans/VOICE_IO.md
```

## [When auto-paste skips itself](https://docs.voicebox.sh/overview/dictation#when-auto-paste-skips-itself)
[When auto-paste skips itself](https://docs.voicebox.sh/overview/dictation#when-auto-paste-skips-itself)
A few cases where Voicebox deliberately does not synthesize a paste:
- Focus was inside Voicebox when the chord started. The transcript goes
to the Captures tab so a dictation-into-Voicebox round-trip doesn't
accidentally paste into the generate box.
- No text focus detected. The transcript still lands in the Captures
tab; copy it from there with one click.
- Accessibility permission not granted on macOS. Same — Captures tab
only.

## [Next steps](https://docs.voicebox.sh/overview/dictation#next-steps)
[Next steps](https://docs.voicebox.sh/overview/dictation#next-steps)
[CapturesThe paired audio + transcript archive every dictation lands in.](https://docs.voicebox.sh/overview/captures)

### Captures
The paired audio + transcript archive every dictation lands in.
[Voice PersonalitiesThe same local LLM powers per-profile compose and persona rewrite.](https://docs.voicebox.sh/overview/voice-personalities)

### Voice Personalities
The same local LLM powers per-profile compose and persona rewrite.
[TranscriptionDeveloper-level details on Whisper, Whisper Turbo, and the STT backend.](https://docs.voicebox.sh/developer/transcription)

### Transcription
Developer-level details on Whisper, Whisper Turbo, and the STT backend.
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/dictation.mdx)
[GPU AccelerationHow Voicebox uses your GPU — auto-detection, manual setup, troubleshooting](https://docs.voicebox.sh/overview/gpu-acceleration)
GPU Acceleration
How Voicebox uses your GPU — auto-detection, manual setup, troubleshooting
[CapturesThe paired audio + transcript archive — every dictation, recording, and uploaded audio file shows up here, replayable and retranscribable.](https://docs.voicebox.sh/overview/captures)
Captures
The paired audio + transcript archive — every dictation, recording, and uploaded audio file shows up here, replayable and retranscribable.

### On this page
[Overview](https://docs.voicebox.sh/overview/dictation#overview)
[The flow](https://docs.voicebox.sh/overview/dictation#the-flow)
[Push-to-talk and toggle modes](https://docs.voicebox.sh/overview/dictation#push-to-talk-and-toggle-modes)
[The on-screen pill](https://docs.voicebox.sh/overview/dictation#the-on-screen-pill)
[Customizing the chord](https://docs.voicebox.sh/overview/dictation#customizing-the-chord)
[Auto-paste into the focused app](https://docs.voicebox.sh/overview/dictation#auto-paste-into-the-focused-app)
[Refinement](https://docs.voicebox.sh/overview/dictation#refinement)
[Platform notes](https://docs.voicebox.sh/overview/dictation#platform-notes)
[macOS](https://docs.voicebox.sh/overview/dictation#macos)
[Windows](https://docs.voicebox.sh/overview/dictation#windows)
[Linux](https://docs.voicebox.sh/overview/dictation#linux)
[When auto-paste skips itself](https://docs.voicebox.sh/overview/dictation#when-auto-paste-skips-itself)
[Next steps](https://docs.voicebox.sh/overview/dictation#next-steps)

