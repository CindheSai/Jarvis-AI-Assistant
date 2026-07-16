# Contributing to J.A.R.V.I.S.

Thanks for considering a contribution. This guide covers the workflow for
submitting changes.

## Workflow

1. **Fork** the repository to your own GitHub account.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/jarvis-assistant.git
   ```
3. **Create a branch** for your change, using a descriptive name:
   ```bash
   git checkout -b feature/add-spotify-controls
   ```
4. **Make your changes**, following the coding standards below.
5. **Commit** with a clear, conventional message:
   ```bash
   git commit -m "feat: add pause/resume voice commands for Spotify"
   ```
6. **Push** your branch and **open a pull request** against `main`, describing:
   - What the change does
   - Why it's needed
   - How you tested it

## Coding standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python style.
- Keep functions small and single-purpose, matching the existing module layout
  (voice engine, AI brain, app launcher, system controls, etc.).
- Add a docstring to any new function explaining what it does.
- Never hardcode API keys, file paths, or credentials — use environment variables.
- Prefer explicit `except Exception:` over bare `except:` in new code.
- Test voice commands manually before submitting, and note the commands you tried
  in your pull request description.

## Reporting issues

When filing a bug report, please include:

- Your OS and Python version
- The exact voice command or text input that triggered the issue
- The full error message or console output
- Steps to reproduce

Feature requests are welcome — open an issue describing the use case before
submitting a large pull request, so the approach can be discussed first.

## Code of conduct

Participation in this project is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
