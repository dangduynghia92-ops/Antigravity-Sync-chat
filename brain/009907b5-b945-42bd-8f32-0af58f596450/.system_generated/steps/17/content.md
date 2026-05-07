Title: Voice Cloning

Description: Clone any voice from a few seconds of reference audio

Source: https://docs.voicebox.sh/overview/voice-cloning

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

Clone any voice from a few seconds of reference audio

## [Overview](https://docs.voicebox.sh/overview/voice-cloning#overview)
[Overview](https://docs.voicebox.sh/overview/voice-cloning#overview)
Voicebox can replicate a specific person's voice from a short audio sample — known as zero-shot voice cloning. You provide 10-30 seconds of clear speech, the model extracts a voice embedding, and from then on you can generate any text in that voice.
Five engines in 0.4 support cloning:

```
[laugh]
```


```
[sigh]
```

Don't want to record audio? Use a curated voice from Kokoro or Qwen CustomVoice instead — see [Preset Voices](https://docs.voicebox.sh/overview/preset-voices).

## [How It Works](https://docs.voicebox.sh/overview/voice-cloning#how-it-works)
[How It Works](https://docs.voicebox.sh/overview/voice-cloning#how-it-works)
Provide 10-30 seconds of clear speech from the target voice
The selected engine analyzes vocal characteristics, tone, and speaking patterns
A voice embedding is generated and stored with your profile
Use the profile to generate any text in the cloned voice

## [Choosing an Engine for Cloning](https://docs.voicebox.sh/overview/voice-cloning#choosing-an-engine-for-cloning)
[Choosing an Engine for Cloning](https://docs.voicebox.sh/overview/voice-cloning#choosing-an-engine-for-cloning)
Different engines suit different use cases. The profile grid greys out unsupported engines so you can switch easily.

```
[laugh]
```


```
[sigh]
```

## [Best Practices](https://docs.voicebox.sh/overview/voice-cloning#best-practices)
[Best Practices](https://docs.voicebox.sh/overview/voice-cloning#best-practices)

### [Sample Quality](https://docs.voicebox.sh/overview/voice-cloning#sample-quality)
[Sample Quality](https://docs.voicebox.sh/overview/voice-cloning#sample-quality)

### Do
- Use 10-30 seconds of audio
- Clear, consistent speaking
- Minimal background noise
- Natural speaking pace

### Don't
- Very short clips (< 5 seconds)
- Heavy background noise
- Music or overlapping voices
- Heavily processed audio

### [Multiple Samples](https://docs.voicebox.sh/overview/voice-cloning#multiple-samples)
[Multiple Samples](https://docs.voicebox.sh/overview/voice-cloning#multiple-samples)
Adding multiple samples from the same speaker can improve quality:
- Different speaking styles (casual, formal)
- Different emotions (happy, serious)
- Different recording conditions
The model will learn a more robust representation from diverse samples. Especially helpful for distinctive voices the model might otherwise smooth over.

## [Supported Languages by Engine](https://docs.voicebox.sh/overview/voice-cloning#supported-languages-by-engine)
[Supported Languages by Engine](https://docs.voicebox.sh/overview/voice-cloning#supported-languages-by-engine)
- Qwen3-TTS — English, Chinese, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian (10)
- Chatterbox Multilingual — Arabic, Chinese, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Italian, Japanese, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swahili, Swedish, Turkish (23)
- Chatterbox Turbo — English
- LuxTTS — English
- TADA 3B — 10 multilingual; TADA 1B — English
For complete language tables and engine-specific notes, see the [TTS Engines developer guide](https://docs.voicebox.sh/developer/tts-engines).

## [Limitations](https://docs.voicebox.sh/overview/voice-cloning#limitations)
[Limitations](https://docs.voicebox.sh/overview/voice-cloning#limitations)
Voice cloning should only be used with consent. Ensure you have permission to clone someone's voice. See the project's [SECURITY.md](https://github.com/jamiepine/voicebox/blob/main/SECURITY.md) and your local laws on synthetic voice content.
- Quality depends on sample clarity — noisy samples produce noisy clones
- Works best with consistent speaking tone within a sample
- May struggle with extreme accents or speech impediments
- Background noise reduces quality and can introduce artifacts

## [Next Steps](https://docs.voicebox.sh/overview/voice-cloning#next-steps)
[Next Steps](https://docs.voicebox.sh/overview/voice-cloning#next-steps)
[Creating Voice ProfilesStep-by-step guide to creating profiles](https://docs.voicebox.sh/overview/creating-voice-profiles)

### Creating Voice Profiles
Step-by-step guide to creating profiles
[Preset VoicesUse built-in voices instead of cloning](https://docs.voicebox.sh/overview/preset-voices)

### Preset Voices
Use built-in voices instead of cloning
[Generating SpeechUse a profile to generate audio](https://docs.voicebox.sh/overview/generating-speech)

### Generating Speech
Use a profile to generate audio
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/voice-cloning.mdx)
[CapturesThe paired audio + transcript archive — every dictation, recording, and uploaded audio file shows up here, replayable and retranscribable.](https://docs.voicebox.sh/overview/captures)
Captures
The paired audio + transcript archive — every dictation, recording, and uploaded audio file shows up here, replayable and retranscribable.
[Preset VoicesUse built-in, ready-made voices without recording audio samples](https://docs.voicebox.sh/overview/preset-voices)
Preset Voices
Use built-in, ready-made voices without recording audio samples

### On this page
[Overview](https://docs.voicebox.sh/overview/voice-cloning#overview)
[How It Works](https://docs.voicebox.sh/overview/voice-cloning#how-it-works)
[Choosing an Engine for Cloning](https://docs.voicebox.sh/overview/voice-cloning#choosing-an-engine-for-cloning)
[Best Practices](https://docs.voicebox.sh/overview/voice-cloning#best-practices)
[Sample Quality](https://docs.voicebox.sh/overview/voice-cloning#sample-quality)
[Multiple Samples](https://docs.voicebox.sh/overview/voice-cloning#multiple-samples)
[Supported Languages by Engine](https://docs.voicebox.sh/overview/voice-cloning#supported-languages-by-engine)
[Limitations](https://docs.voicebox.sh/overview/voice-cloning#limitations)
[Next Steps](https://docs.voicebox.sh/overview/voice-cloning#next-steps)

