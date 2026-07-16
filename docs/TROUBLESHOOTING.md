# Troubleshooting

## Microphone not detected / "No default input device"

- Ensure a microphone is connected and set as the default recording device in
  Windows Sound Settings.
- Grant microphone permission: **Settings → Privacy & security → Microphone**,
  and allow desktop apps to access it.
- List available microphones to confirm detection:
  ```python
  import speech_recognition as sr
  print(sr.Microphone.list_microphone_names())
  ```

## PyAudio fails to install

`pip install pyaudio` commonly fails on Windows because it needs to compile
against PortAudio. Fix with a prebuilt wheel:
```powershell
pip install pipwin
pipwin install pyaudio
```
Alternatively, download a matching `.whl` from Christoph Gohlke's unofficial
Windows binaries and install it directly with `pip install <wheel_file>`.

## Anthropic API errors

- **`AI connection failed: Could not resolve authentication method`** — the
  `ANTHROPIC_API_KEY` environment variable isn't set. Confirm it with:
  ```powershell
  echo %ANTHROPIC_API_KEY%
  ```
  and make sure `.env` was copied from `.env.example` and loaded.
- **`401 Unauthorized`** — the key is invalid, expired, or was revoked. Generate
  a new key in the Anthropic Console.
- **`429 Rate limit exceeded`** — you've hit your usage tier's rate limit; wait
  and retry, or check your plan limits.

## No internet connection

Google Speech Recognition, Google/YouTube search, Wikipedia lookups, and the
Claude API all require an active internet connection. Offline, only local
commands (time, date, app launching, system controls) will work — voice
recognition itself also depends on Google's API and will fail offline.

## Speech recognition returns empty / commands not detected

- Speak clearly and reduce background noise; `adjust_for_ambient_noise` needs
  a brief quiet moment to calibrate.
- Increase the `timeout` or `phrase_time_limit` values in `listen()` if you
  tend to pause before speaking or need more time to finish a sentence.
- Confirm the wake word is being picked up by checking the console output for
  `[Listening...]` and `YOU »` lines.

## Windows permission errors

- **Shutdown/restart/sleep commands fail** — run the terminal or IDE as
  Administrator.
- **App launch fails silently** — verify the executable name in `APPS` matches
  what's actually on your PATH, or that the app is installed at all.
- **Lock screen / recycle bin errors** — these use Windows-only libraries
  (`ctypes.windll`, `winshell`) and will not work on macOS or Linux.
