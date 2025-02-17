**# BetterTerminal**

BetterTerminal is a cross-platform terminal emulator written in Python. It does **not** use system-specific commands (like Windows `cmd` or Unix `bash` commands), but instead implements all commands manually in Python.

## 🚀 Features
- Works on **Windows, Linux, and macOS**
- Supports classic Unix commands like `ls`, `cd`, `mkdir`, `rm`, `touch`, `echo`, `cat`, `cp`, `mv`, `grep`, `find`, `chmod`, `history`, `head`, `tail`, `ps`, `kill`, `df`, `whoami`, `uptime`, `uname`
- **Fully customizable** – You can add your own commands!
- No external dependencies except `psutil` and `shutil`

## 🛠️ Installation
### **Prerequisites**
- Python 3.7+
- `psutil` package (for process management)

Install dependencies with:
```sh
pip install psutil

Clone the Repository:

git clone https://github.com/echoLabs-dev/BetterTerminal.git
cd BetterTerminal

Run BetterTerminal:

**python main.py**
