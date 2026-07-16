# Installation guide (Windows)

## 1. Install Python

1. Download Python 3.11+ from [python.org/downloads](https://www.python.org/downloads/).
2. Run the installer and **check "Add Python to PATH"** before clicking Install.
3. Verify the install:
   ```powershell
   python --version
   ```

## 2. Install Git

1. Download Git from [git-scm.com/download/win](https://git-scm.com/download/win).
2. Run the installer with default options.
3. Verify the install:
   ```powershell
   git --version
   ```

## 3. Clone the repository

```powershell
git clone https://github.com/<your-username>/jarvis-assistant.git
cd jarvis-assistant
```

## 4. Create a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

## 5. Install dependencies

```powershell
pip install -r requirements.txt
```

> **Note:** `PyAudio` sometimes fails to install directly on Windows. If it does,
> install a prebuilt wheel instead:
> ```powershell
> pip install pipwin
> pipwin install pyaudio
> ```

## 6. Set your environment variables

1. Copy `.env.example` to `.env`:
   ```powershell
   copy .env.example .env
   ```
2. Open `.env` and paste in your real Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_real_key_here
   ```
3. Load the `.env` file before running (either export it manually in the shell,
   or add `from dotenv import load_dotenv; load_dotenv()` near the top of
   `jarvis.py` if you'd like it loaded automatically).

## 7. Run the project

```powershell
python jarvis.py
```

You should hear: *"J.A.R.V.I.S. online. All systems ready. Good day, Sir."*

Say **"Jarvis"**, wait for *"Yes, Sir?"*, then speak a command.

## Troubleshooting

See [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) for fixes to common setup errors
(microphone access, PyAudio install failures, API errors, and more).
