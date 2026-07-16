# Project structure

```
jarvis-assistant/
├── jarvis.py                  # Main application: voice loop, command router, all features
├── requirements.txt            # Python dependencies
├── .env.example                 # Template for required environment variables
├── .gitignore                    # Files and folders excluded from git
├── LICENSE                       # MIT License
├── README.md                     # Project overview and usage guide
├── SECURITY.md                   # Credential handling and vulnerability reporting
├── CONTRIBUTING.md                # Contribution workflow and standards
├── CHANGELOG.md                   # Version history
├── CODE_OF_CONDUCT.md              # Contributor Covenant
├── assets/
│   └── screenshots/                # App screenshots for the README (empty until added)
└── docs/
    ├── PROJECT_STRUCTURE.md         # This file
    ├── FEATURES.md                  # Detailed feature descriptions
    ├── COMMANDS.md                  # Full voice command reference
    ├── INSTALLATION.md              # Step-by-step Windows setup guide
    └── TROUBLESHOOTING.md            # Common errors and fixes
```

## File responsibilities

| File | Responsibility |
| --- | --- |
| `jarvis.py` | Everything the assistant does: listening, text-to-speech, Claude integration, app launching, system/power controls, web and Wikipedia search, file/folder actions, and the main command router (`process()`). |
| `requirements.txt` | Pinned minimum versions of every third-party package imported in `jarvis.py`. |
| `.env.example` | Documents the one required environment variable, `ANTHROPIC_API_KEY`, without exposing a real key. |
| `docs/COMMANDS.md` | Reference list of every voice phrase the router in `process()` recognizes, grouped by category. |
| `docs/FEATURES.md` | Plain-language explanation of each capability, for users evaluating the project. |
