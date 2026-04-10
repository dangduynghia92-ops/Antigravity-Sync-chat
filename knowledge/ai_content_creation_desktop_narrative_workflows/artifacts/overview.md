# AI-Powered Narrative and Visual Workflow Systems: Overview

This knowledge item describes a robust architectural pattern for building desktop applications (PyQt/PySide) that leverage LLMs to automate complex content creation tasks, specifically focused on **historical narratives, script rewriting, and visual prompt generation.**

## The Core Philosophy: Hierarchical Context-Aware Generation

A defining feature of these systems is the **Two-Stage Generation Model**, which ensures global consistency across fragmented outputs (chapters or time-based segments):

1. **Stage 1: Global Analysis (The "Bible" Step)**
   - Before individual generation begins, the AI performs a comprehensive review of the entire source document (full SRT or multi-chapter script).
   - It identifies key constants: Historical Era, Character Descriptions, Tone/Mood, and Shared Architecture.
   - This metadata is cached as a "Visual Bible" or "Narrative Review" document.

2. **Stage 2: Discrete Segment Generation**
   - The system processes the source in manageable chunks (5-second intervals or narrative chapters).
   - For *each* chunk, the Global Analysis from Stage 1 is prepended as a "Reference Section."
   - The AI is instructed to cross-reference the local chunk with the global guide, ensuring that characters and settings remain visually and narratively consistent throughout the entire project.

## Project Contexts

The patterns in this KI were developed across several specialized projects:
- **SRT to Visual Prompt Generator**: Converting subtitle files into descriptive, consistent image generation prompts for video production.
- **Narrative Script Review and Rewriting**: An AI-powered system for scoring, refining, and modularly rewriting complex historical mystery scripts.
- **Script Renew**: A deep restructuring tool that re-outlines scripts based on narrative frameworks and regenerates chapters from scratch.
- **TTS Cleanup and Hygiene**: Preparing AI-generated text for natural-sounding speech by stripping formatting and normalizing language.

## Key System Pillars
- **Structured Outputs (CSV-Only)**: Moving away from flat text files to structured CSV data allows for granular review, automated scoring, and centralized batch merging.
- **Resilient AI Comms**: Multi-endpoint fallback and interactive rate-limit recovery allow the desktop app to remain stable despite varying AI provider availability.
- **Desktop Integration**: Handling file locks (Excel) and ensuring thread-safe UI updates from background workers.
- **Script Hygiene**: Built-in logic to strip system-generated "noise" (markdown, meta-tags) ensuring final outputs are broadcast-ready or TTS-compatible.
