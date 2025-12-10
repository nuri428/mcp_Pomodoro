![release](https://github.com/nuri428/pomodoro-cli/actions/workflows/release.yml/badge.svg)

# Pomodoro Timer (CLI)

A minimal, cross-platform Pomodoro timer for developers and deep-work practitioners.  
Lightweight, configurable, and designed to integrate easily with automation tools or AI agents.

---

---

## Features
- Customizable focus, break, and long-break durations  
- Desktop notifications on macOS, Linux, and Windows  
- Optional config.json support  
- Zero external dependencies for macOS/Linux  
- Ideal for terminal workflow (tmux, VSCode, SSH, MCP)

---

## Installation

Clone the repository:

```
git clone https://github.com/nuri428/pomodoro-cli.git
cd pomodoro-cli
```

Windows notification support:

```
pip install -r requirements.txt
```

---

## Usage

### Default (25 min focus / 5 min break)

```
python3 cli.py
```

### Custom durations

```
python3 cli.py --focus 50 --break 10
```

### Quick test

```
python3 cli.py --focus 1 --break 1
```

### Using a config.json

Example config:

```
{
    "focus_time": 25,
    "break_time": 5,
    "long_break_time": 15,
    "cycles": 4
}
```

If this file exists, the CLI will load it automatically.

---

## Project Structure

```
pomodoro/        # Core timer logic
cli.py           # CLI entry point
config.json      # Optional user config
README.md
```

---

## Roadmap
- GUI version  
- macOS menu bar timer  
- Windows tray version  
- MCP (Model Context Protocol) integration  
- Google Calendar syncing  
- Webhook-based automation  

---

## License
MIT License.

---

