"""
J.A.R.V.I.S. - AI Voice Assistant
=================================
A Windows voice assistant powered by the Anthropic Claude API.
Listens for the wake word "jarvis", then routes spoken commands to either
built-in system/OS actions or the Claude API for open-ended conversation.

Author: Cindhe Sai Mukesh Rao
License: MIT
"""

import os
import sys
import time
import datetime
import subprocess

import anthropic
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import wikipedia
import psutil

# =============================================================
#   Configuration
# =============================================================
# The API key is never hardcoded. Set it as an environment variable
# named ANTHROPIC_API_KEY, or place it in a local .env file
# (see .env.example) and load it with a tool like python-dotenv.
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise EnvironmentError(
        "ANTHROPIC_API_KEY is not set. "
        "Copy .env.example to .env, add your key, and load it before running, "
        "or export it directly in your shell."
    )

client = anthropic.Anthropic(api_key=API_KEY)
recognizer = sr.Recognizer()
history = []  # Rolling conversation memory sent to Claude for context

# =============================================================
#   Voice Engine Setup (text-to-speech)
# =============================================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # index 0 is usually a male voice
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


def speak(text):
    """Print and speak JARVIS's response."""
    print(f"\n  JARVIS » {text}\n")
    engine.say(text)
    engine.runAndWait()


def listen(timeout=6):
    """Capture a single spoken command from the microphone."""
    with sr.Microphone() as source:
        print("  [Listening...]")
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=12)
            text = recognizer.recognize_google(audio)
            print(f"  YOU » {text}")
            return text.lower()
        except Exception:
            return ""


# =============================================================
#   AI Brain (Claude)
# =============================================================
SYSTEM = """You are J.A.R.V.I.S., a highly intelligent AI assistant like in Iron Man.
Be helpful, confident, and slightly witty. Keep answers short (2-4 sentences max).
Occasionally address the user as 'Sir'. You help with anything — coding, knowledge, 
advice, creative work, math, analysis. Be direct and smart."""


def ask_ai(prompt):
    """Send a prompt to Claude and return its reply, keeping rolling history."""
    history.append({"role": "user", "content": prompt})
    try:
        res = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=400,
            system=SYSTEM,
            messages=history[-12:],  # keep last 12 turns for context
        )
        reply = res.content[0].text
        history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"AI connection failed: {e}"


# =============================================================
#   App Launcher
# =============================================================
APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "vs code": "code.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "settings": "ms-settings:",
    "camera": "microsoft.windows.camera:",
    "spotify": "spotify.exe",
}


def open_app(name):
    """Launch a known Windows application, or fall back to a raw process name."""
    for key, exe in APPS.items():
        if key in name:
            try:
                if exe.startswith("ms"):
                    os.startfile(exe)
                else:
                    subprocess.Popen(exe, shell=True)
                speak(f"Opening {key}, Sir.")
                return True
            except Exception:
                speak(f"Could not open {key}.")
                return True
    words = name.replace("open", "").replace("launch", "").replace("start", "").strip()
    if words:
        try:
            subprocess.Popen(words, shell=True)
            speak(f"Launching {words}.")
            return True
        except Exception:
            pass
    return False


# =============================================================
#   System Controls
# =============================================================
def set_volume(action):
    """Adjust system volume using simulated media keys."""
    if action == "up":
        for _ in range(8):
            pyautogui.press("volumeup")
        speak("Volume increased.")
    elif action == "down":
        for _ in range(8):
            pyautogui.press("volumedown")
        speak("Volume decreased.")
    elif action == "mute":
        pyautogui.press("volumemute")
        speak("Audio muted.")
    elif action == "unmute":
        pyautogui.press("volumemute")
        speak("Audio unmuted.")
    elif "max" in action:
        for _ in range(50):
            pyautogui.press("volumeup")
        speak("Volume set to maximum.")


def system_info():
    """Report CPU, RAM, and disk usage."""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    info = (
        f"CPU usage is {cpu} percent. "
        f"RAM: {ram.percent} percent used, "
        f"{round(ram.available / 1e9, 1)} gigabytes free. "
        f"Disk: {round(disk.free / 1e9, 1)} gigabytes free."
    )
    speak(info)


def take_screenshot():
    """Save a screenshot of the current desktop."""
    path = os.path.join(os.path.expanduser("~"), "Desktop", f"screenshot_{int(time.time())}.png")
    pyautogui.screenshot(path)
    speak("Screenshot saved to your desktop, Sir.")


def lock_screen():
    """Lock the Windows session."""
    import ctypes
    ctypes.windll.user32.LockWorkStation()
    speak("Locking your screen.")


def empty_recycle_bin():
    """Empty the Windows Recycle Bin silently."""
    import winshell
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    speak("Recycle bin emptied.")


# =============================================================
#   Web & Search
# =============================================================
def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    speak(f"Searching Google for {query}.")


def search_youtube(query):
    webbrowser.open(f"https://youtube.com/results?search_query={query.replace(' ', '+')}")
    speak(f"Searching YouTube for {query}.")


def open_website(cmd):
    """Open a known website if it's mentioned in the command."""
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com",
        "gmail": "https://mail.google.com",
        "twitter": "https://twitter.com",
        "instagram": "https://instagram.com",
        "facebook": "https://facebook.com",
        "reddit": "https://reddit.com",
        "netflix": "https://netflix.com",
        "amazon": "https://amazon.com",
        "chatgpt": "https://chat.openai.com",
        "linkedin": "https://linkedin.com",
        "whatsapp": "https://web.whatsapp.com",
    }
    for site, url in sites.items():
        if site in cmd:
            webbrowser.open(url)
            speak(f"Opening {site}, Sir.")
            return True
    return False


def wikipedia_search(query):
    """Look up a topic on Wikipedia, falling back to Claude if not found."""
    try:
        result = wikipedia.summary(query, sentences=2, auto_suggest=True)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found. Did you mean: {e.options[0]}?")
    except Exception:
        speak("Couldn't find that on Wikipedia. Let me ask the AI instead.")
        speak(ask_ai(query))


# =============================================================
#   File & Folder Management
# =============================================================
def create_file(cmd):
    """Create an empty file on the desktop with a given or default name."""
    name = cmd.replace("create file", "").replace("make file", "").replace("new file", "").strip()
    if not name:
        name = "new_file.txt"
    if "." not in name:
        name += ".txt"
    path = os.path.join(os.path.expanduser("~"), "Desktop", name)
    open(path, 'w').close()
    speak(f"Created {name} on your desktop.")


def open_folder(cmd):
    """Open a well-known user folder (Desktop, Downloads, etc.)."""
    folders = {
        "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
        "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
        "documents": os.path.join(os.path.expanduser("~"), "Documents"),
        "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
        "music": os.path.join(os.path.expanduser("~"), "Music"),
        "videos": os.path.join(os.path.expanduser("~"), "Videos"),
    }
    for folder, path in folders.items():
        if folder in cmd:
            os.startfile(path)
            speak(f"Opening {folder} folder.")
            return True
    return False


# =============================================================
#   Typing / Clipboard
# =============================================================
def type_text(cmd):
    """Type out spoken text using simulated keystrokes."""
    text = cmd.replace("type", "").replace("write", "").strip()
    pyautogui.write(text, interval=0.05)
    speak(f"Typed: {text}")


# =============================================================
#   Power Controls
# =============================================================
def power_control(cmd):
    """Handle shutdown, restart, sleep, cancel, and sign-out commands."""
    if "shutdown" in cmd:
        speak("Shutting down your PC in 10 seconds. Say cancel to abort.")
        os.system("shutdown /s /t 10")
    elif "restart" in cmd or "reboot" in cmd:
        speak("Restarting in 10 seconds.")
        os.system("shutdown /r /t 10")
    elif "sleep" in cmd or "hibernate" in cmd:
        speak("Putting your PC to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "cancel" in cmd:
        os.system("shutdown /a")
        speak("Power action cancelled, Sir.")
    elif "log off" in cmd or "sign out" in cmd:
        speak("Signing you out.")
        os.system("shutdown /l")


# =============================================================
#   Main Command Processor
# =============================================================
def process(cmd):
    """Route a recognized voice command to the right handler."""
    if not cmd:
        return

    if any(w in cmd for w in ["time", "what time"]):
        t = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It's {t}, Sir.")
        return

    if any(w in cmd for w in ["date", "today", "what day"]):
        d = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {d}.")
        return

    if any(w in cmd for w in ["shutdown", "restart", "reboot", "sleep", "hibernate", "log off", "sign out", "cancel shutdown"]):
        power_control(cmd)
        return

    if "lock" in cmd and "screen" in cmd:
        lock_screen()
        return

    if "screenshot" in cmd or "screen capture" in cmd:
        take_screenshot()
        return

    if "volume up" in cmd or "increase volume" in cmd or "louder" in cmd:
        set_volume("up")
        return
    if "volume down" in cmd or "decrease volume" in cmd or "quieter" in cmd or "lower volume" in cmd:
        set_volume("down")
        return
    if "mute" in cmd:
        set_volume("mute")
        return
    if "unmute" in cmd or "volume on" in cmd:
        set_volume("unmute")
        return
    if "max volume" in cmd or "full volume" in cmd:
        set_volume("max")
        return

    if any(w in cmd for w in ["system info", "cpu", "ram", "memory", "disk space", "battery"]):
        system_info()
        return

    if any(w in cmd for w in ["open youtube", "open google", "open github", "open gmail",
                               "open twitter", "open instagram", "open facebook",
                               "open reddit", "open netflix", "open amazon",
                               "open chatgpt", "open linkedin", "open whatsapp"]):
        if open_website(cmd):
            return

    if "search youtube" in cmd or "youtube search" in cmd or ("search" in cmd and "youtube" in cmd):
        query = (cmd.replace("search youtube for", "")
                 .replace("search on youtube", "")
                 .replace("youtube search", "")
                 .replace("search youtube", "")
                 .strip())
        search_youtube(query)
        return

    if "search" in cmd or "google" in cmd:
        query = (cmd.replace("search for", "")
                 .replace("search google for", "")
                 .replace("google search", "")
                 .replace("google", "")
                 .replace("search", "")
                 .strip())
        if query:
            search_google(query)
            return

    if "wikipedia" in cmd or "who is" in cmd or "tell me about" in cmd:
        query = cmd.replace("wikipedia", "").replace("who is", "").replace("tell me about", "").strip()
        wikipedia_search(query)
        return

    if any(w in cmd for w in ["open", "launch", "start"]):
        if open_app(cmd):
            return

    if "open" in cmd and any(f in cmd for f in ["desktop", "downloads", "documents", "pictures", "music", "videos"]):
        if open_folder(cmd):
            return

    if any(w in cmd for w in ["create file", "make file", "new file"]):
        create_file(cmd)
        return

    if cmd.startswith("type ") or cmd.startswith("write "):
        type_text(cmd)
        return

    if "close" in cmd or "quit" in cmd or "exit" in cmd:
        pyautogui.hotkey("alt", "f4")
        speak("Closing the current window.")
        return

    if "minimize" in cmd:
        pyautogui.hotkey("win", "down")
        speak("Minimized.")
        return
    if "maximize" in cmd:
        pyautogui.hotkey("win", "up")
        speak("Maximized.")
        return

    if "copy" in cmd:
        pyautogui.hotkey("ctrl", "c")
        speak("Copied.")
        return
    if "paste" in cmd:
        pyautogui.hotkey("ctrl", "v")
        speak("Pasted.")
        return
    if "undo" in cmd:
        pyautogui.hotkey("ctrl", "z")
        speak("Undone.")
        return
    if "select all" in cmd:
        pyautogui.hotkey("ctrl", "a")
        speak("Selected all.")
        return

    if "switch window" in cmd or "alt tab" in cmd or "next window" in cmd:
        pyautogui.hotkey("alt", "tab")
        speak("Switching window.")
        return

    if any(w in cmd for w in ["goodbye", "bye jarvis", "exit jarvis", "stop jarvis", "shut down jarvis"]):
        speak("Goodbye, Sir. Stay sharp.")
        sys.exit(0)

    if "joke" in cmd or "make me laugh" in cmd:
        reply = ask_ai("Tell me a short, clever joke.")
        speak(reply)
        return

    # Anything unmatched goes to Claude
    reply = ask_ai(cmd)
    speak(reply)


# =============================================================
#   Wake Word Loop
# =============================================================
def wait_for_wake_word():
    """Listen continuously for the word 'jarvis' to activate a command."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            text = recognizer.recognize_google(audio).lower()
            return "jarvis" in text
        except Exception:
            return False


BANNER = r"""
     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
        AI Voice Assistant  •  v1.0.0
"""

if __name__ == "__main__":
    print(BANNER)
    print("  Say 'Jarvis' to activate.")
    print("  Say 'goodbye' to quit.\n")

    speak("J.A.R.V.I.S. online. All systems ready. Good day, Sir.")

    while True:
        print("  [Waiting for 'Jarvis'...]")
        if wait_for_wake_word():
            speak("Yes, Sir?")
            command = listen()
            if command:
                process(command)
