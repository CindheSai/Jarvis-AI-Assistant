# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-07-14

### Added
- Initial release of J.A.R.V.I.S. AI Voice Assistant.
- Wake-word activation ("jarvis") using `speech_recognition`.
- Claude-powered conversational fallback for open-ended questions.
- Voice-controlled application launcher (Notepad, Calculator, Chrome, VS Code, etc.).
- Website shortcuts (YouTube, GitHub, Gmail, Netflix, and more).
- Google and YouTube voice search.
- Wikipedia lookups with Claude fallback on failure.
- System controls: volume, screenshots, lock screen, recycle bin.
- Power controls: shutdown, restart, sleep, sign out, cancel.
- File and folder commands: create files, open common user folders.
- Typing, clipboard, and window management shortcuts.
- Text-to-speech responses via `pyttsx3`.

### Security
- API key moved from hardcoded source to the `ANTHROPIC_API_KEY` environment
  variable, loaded via `.env` (see `.env.example`).
