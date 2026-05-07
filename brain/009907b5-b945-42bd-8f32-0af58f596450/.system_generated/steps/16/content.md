Title: Quick Start

Description: Get started with Voicebox in 5 minutes

Source: https://docs.voicebox.sh/overview/quick-start

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

Get started with Voicebox in 5 minutes
This guide will walk you through creating your first voice profile and generating speech.

## [Prerequisites](https://docs.voicebox.sh/overview/quick-start#prerequisites)
[Prerequisites](https://docs.voicebox.sh/overview/quick-start#prerequisites)
Make sure you have [installed Voicebox](https://docs.voicebox.sh/overview/installation) and launched the app.

## [Step 1: Create a Voice Profile](https://docs.voicebox.sh/overview/quick-start#step-1-create-a-voice-profile)
[Step 1: Create a Voice Profile](https://docs.voicebox.sh/overview/quick-start#step-1-create-a-voice-profile)
Voice profiles are the foundation of Voicebox. Each profile contains voice samples that the AI uses to clone the voice.
Click the Profiles tab in the sidebar
Click the + New Profile button
Fill in the details:
- Name: A descriptive name (e.g., "John Smith")
- Language: Select the primary language
- Description: Optional notes about the voice
You have two options:
Option A: Upload Audio
- Click Upload Sample
- Select an audio file (WAV, MP3, or M4A)
- Ideal length: 10-30 seconds of clear speech
Option B: Record Live
- Click Record Sample
- Speak clearly for 10-30 seconds
- Click stop when finished
Click Create Profile to save
For best results, use clean audio with minimal background noise and consistent speaking tone.

## [Step 2: Generate Speech](https://docs.voicebox.sh/overview/quick-start#step-2-generate-speech)
[Step 2: Generate Speech](https://docs.voicebox.sh/overview/quick-start#step-2-generate-speech)
Now let's use your new voice profile to generate speech.
Click the Generate tab in the sidebar
Choose your newly created profile from the dropdown
Type or paste the text you want to generate:

```
Hello! This is my first voice generation with Voicebox.
```


```
Hello! This is my first voice generation with Voicebox.
```

Paralinguistic tags like [laugh], [sigh], and [gasp] only work with Chatterbox Turbo. Qwen3-TTS, LuxTTS, Chatterbox Multilingual, and HumeAI TADA will read those tags literally instead of turning them into expressive sounds.

```
[laugh]
```


```
[sigh]
```


```
[gasp]
```

To insert supported tags, select Chatterbox Turbo and type / in the text input to open the tag inserter.

```
/
```

Click Generate and wait a few seconds
First generation may take longer due to model initialization. Subsequent generations will be faster.
- Click Play to preview the audio
- Click Download to save the audio file
- The generation is also saved to your History

## [Step 3: Build a Story (Optional)](https://docs.voicebox.sh/overview/quick-start#step-3-build-a-story-optional)
[Step 3: Build a Story (Optional)](https://docs.voicebox.sh/overview/quick-start#step-3-build-a-story-optional)
The Stories Editor lets you create multi-voice narratives with a timeline-based interface.
Navigate to Stories and click + New Story
Click + Add Track to create tracks for different speakers
- Drag generated audio from your History
- Or generate new clips directly in the timeline
- Arrange clips on the timeline
- Trim clips by dragging edges
- Adjust timing and spacing
- Click Export to render the final audio

## [What's Next?](https://docs.voicebox.sh/overview/quick-start#whats-next)
[What's Next?](https://docs.voicebox.sh/overview/quick-start#whats-next)
[Voice Cloning GuideLearn advanced techniques for high-quality voice cloning](https://docs.voicebox.sh/overview/creating-voice-profiles)

### Voice Cloning Guide
Learn advanced techniques for high-quality voice cloning
[API IntegrationIntegrate Voicebox into your own applications](https://docs.voicebox.sh/api-reference)

### API Integration
Integrate Voicebox into your own applications
[Stories EditorMaster the multi-track timeline editor](https://docs.voicebox.sh/overview/stories-editor)

### Stories Editor
Master the multi-track timeline editor
[Remote ModeConnect to a GPU server for faster generation](https://docs.voicebox.sh/overview/remote-mode)

### Remote Mode
Connect to a GPU server for faster generation

[Tips for Success](https://docs.voicebox.sh/overview/quick-start#tips-for-success)
- Use 10-30 seconds of clear, consistent speech
- Avoid background noise and echo
- Multiple samples from the same speaker improve quality
- Match the speaking style you want to generate
- Use a CUDA-capable GPU for 5-10x faster generation
- Enable voice prompt caching for repeated generations
- Consider running the backend on a remote GPU server
- Server won't start: Check if port 17493 is available
- Poor audio quality: Try adding more voice samples
- Slow generation: Verify GPU acceleration is enabled
- See the full [Troubleshooting Guide](https://docs.voicebox.sh/overview/troubleshooting) for more
[Troubleshooting Guide](https://docs.voicebox.sh/overview/troubleshooting)
[Edit on GitHub](https://github.com/jamiepine/voicebox/blob/main/docs/content/docs/overview/quick-start.mdx)
[Docker DeploymentRun Voicebox as a headless server with a web UI using Docker](https://docs.voicebox.sh/overview/docker)
Docker Deployment
Run Voicebox as a headless server with a web UI using Docker
[GPU AccelerationHow Voicebox uses your GPU — auto-detection, manual setup, troubleshooting](https://docs.voicebox.sh/overview/gpu-acceleration)
GPU Acceleration
How Voicebox uses your GPU — auto-detection, manual setup, troubleshooting

[Prerequisites](https://docs.voicebox.sh/overview/quick-start#prerequisites)
[Step 1: Create a Voice Profile](https://docs.voicebox.sh/overview/quick-start#step-1-create-a-voice-profile)
[Step 2: Generate Speech](https://docs.voicebox.sh/overview/quick-start#step-2-generate-speech)
[Step 3: Build a Story (Optional)](https://docs.voicebox.sh/overview/quick-start#step-3-build-a-story-optional)
[What's Next?](https://docs.voicebox.sh/overview/quick-start#whats-next)
[Tips for Success](https://docs.voicebox.sh/overview/quick-start#tips-for-success)

