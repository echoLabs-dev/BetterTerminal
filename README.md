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

Command	Description
ls:	List files in the current directory
cd: <dir>	Change the current directory
pwd:	Show the current directory path
mkdir: <dir>	Create a new directory
rm: <file/dir>	Remove a file or directory
touch: <file>	Create an empty file
echo: <text>	Print text to the terminal
cat: <file>	Display file contents
cp: <source> <destination>	Copy files or directories
mv: <source> <destination>	Move or rename files
grep: <word> <file>	Search for a word in a file
find: <filename>	Search for a file in the current directory and subdirectories
history:	Show command history
chmod: <mode> <file>	Change file permissions
head: <file> <lines>	Show the first N lines of a file
tail: <file> <lines>	Show the last N lines of a file
du:	Show total disk usage in the current directory
ps:	List running processes
kill: <pid>	Terminate a process
df:	Show disk usage statistics
whoami:	Display the current username
uptime:	Show system uptime
uname:	Show system information
clear:	Clear the terminal screen
exit:	Exit the terminal

###

📌 TODO
Implement clear command using a better cross-platform approach
Add support for more Unix commands
Improve error handling and add more meaningful error messages

🤝 Contributing
Contributions are welcome! If you have an idea or want to improve BetterTerminal, feel free to:

Fork this repository
Create a new branch (git checkout -b feature-name)
Commit your changes (git commit -m "Added feature X")
Push to your fork (git push origin feature-name)
Submit a Pull Request

📜 License
This project is licensed under the MIT License.

