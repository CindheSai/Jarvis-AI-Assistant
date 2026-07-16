# Features

## Wake-word activation
JARVIS listens passively for the word "jarvis". Once detected, it acknowledges
with "Yes, Sir?" and listens for a single follow-up command.

## Conversational AI (Claude)
Any command that doesn't match a built-in action is sent to the Anthropic
Claude API, using a system prompt that gives JARVIS a confident, witty,
Iron-Man-style persona. The last 12 turns of conversation are kept as context.

## Application launcher
Opens common Windows applications by name — Notepad, Calculator, Paint, Word,
Excel, PowerPoint, Chrome, Firefox, VS Code, File Explorer, Task Manager,
Settings, Camera, and Spotify. If the requested app isn't in the known list,
JARVIS attempts to launch it as a raw process name.

## Website shortcuts
Opens popular websites directly in the default browser: YouTube, Google,
GitHub, Gmail, Twitter, Instagram, Facebook, Reddit, Netflix, Amazon, ChatGPT,
LinkedIn, and WhatsApp Web.

## Search
- **Google search** — opens a Google results page for the spoken query.
- **YouTube search** — opens YouTube results for the spoken query.
- **Wikipedia lookup** — returns a two-sentence summary; falls back to Claude
  if the topic isn't found or is ambiguous.

## System controls
- Volume up / down / mute / unmute / max, via simulated media keys.
- CPU, RAM, and disk usage report, spoken aloud.
- Screenshot capture, saved to the desktop with a timestamped filename.
- Lock screen.
- Empty recycle bin.

## Power controls
Shutdown, restart, sleep/hibernate, cancel a pending shutdown, and sign out —
each triggered by voice and confirmed with a spoken warning before executing.

## File and folder management
- Create an empty file on the desktop with a given name (defaults to `.txt`).
- Open well-known folders: Desktop, Downloads, Documents, Pictures, Music,
  Videos.

## Typing and clipboard
- Type out spoken text directly into the focused window.
- Copy, paste, undo, and select-all via simulated keyboard shortcuts.

## Window management
Minimize, maximize, close/quit the active window, and switch between open
windows (Alt+Tab).

## Time and date
Speaks the current time or the current date on request.
