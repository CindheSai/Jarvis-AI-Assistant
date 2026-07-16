# Security policy

## Protecting your credentials

J.A.R.V.I.S. requires an Anthropic API key to function. Treat this key like a password.

- **Never commit your API key to source control.** Store it as the `ANTHROPIC_API_KEY`
  environment variable, or in a local `.env` file based on `.env.example`.
- **Never upload your `.env` file.** It is excluded by `.gitignore` by default — do not
  remove that entry.
- **Rotate immediately** if a key is ever exposed in a commit, screenshot, log file, or
  shared terminal session. Revoke it from the Anthropic Console and generate a new one.
- **Scope access** by using a key with the minimum permissions needed, if your Anthropic
  account supports scoped keys.
- **Avoid logging secrets.** Don't print `API_KEY` or include it in error messages,
  issue reports, or debug output.

## Reporting a vulnerability

If you discover a security vulnerability in this project (for example, a way the
assistant could execute unintended system commands, leak credentials, or be triggered
by untrusted audio input):

1. Do **not** open a public GitHub issue.
2. Email the maintainer directly (see the repository's contact details) with a
   description of the issue, steps to reproduce, and potential impact.
3. Allow a reasonable window for the maintainer to investigate and patch before any
   public disclosure.

Responsible disclosure helps keep users of this project safe.

## Supported versions

| Version | Supported |
| ------- | --------- |
| 1.0.x   | Yes       |
