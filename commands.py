import os
import shutil
import psutil
import platform
import time

command_history = []

command_history = []

def ls():
    """List files and directories in the current directory"""
    files = os.listdir()
    for file in files:
        print(file)

def cd(path=None):
    """Change directory"""
    if not path:
        print("Error: 'cd' requires a directory path!")
        return
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def pwd():
    """Print the current working directory"""
    print(os.getcwd())

def mkdir(name=None):
    """Create a new directory"""
    if not name:
        print("Error: 'mkdir' requires a directory name!")
        return
    try:
        os.mkdir(name)
        print(f"Directory created: {name}")
    except FileExistsError:
        print(f"Error: Directory '{name}' already exists!")
    except Exception as e:
        print(f"Error: {e}")

def rm(name=None):
    """Remove a file or directory"""
    if not name:
        print("Error: 'rm' requires a file or directory name!")
        return
    try:
        if os.path.isdir(name):
            os.rmdir(name)
            print(f"Directory deleted: {name}")
        elif os.path.isfile(name):
            os.remove(name)
            print(f"File deleted: {name}")
        else:
            print(f"Error: '{name}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def touch(filename=None):
    """Create an empty file"""
    if not filename:
        print("Error: 'touch' requires a filename!")
        return
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
        print(f"File created: {filename}")
    except Exception as e:
        print(f"Error: {e}")

def echo(*args):
    """Print text to the terminal"""
    if not args:
        print("Error: 'echo' requires text input!")
        return
    print(" ".join(args))

def cat(filename=None):
    """Display the contents of a file"""
    if not filename:
        print("Error: 'cat' requires a filename!")
        return
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def clear_screen():
    """Clear the terminal screen"""
    print("\033[H\033[J", end="")  # Clears screen using ANSI escape codes

def exit_terminal():
    """Exit the terminal"""
    print("Closing terminal...")
    exit()

def cp(source=None, destination=None):
    """Copy a file or directory"""
    if not source or not destination:
        print("Error: 'cp' requires source and destination!")
        return
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
        print(f"Copied: {source} → {destination}")
    except FileNotFoundError:
        print(f"Error: '{source}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def mv(source=None, destination=None):
    """Move or rename a file or directory"""
    if not source or not destination:
        print("Error: 'mv' requires source and destination!")
        return
    try:
        shutil.move(source, destination)
        print(f"Moved: {source} → {destination}")
    except FileNotFoundError:
        print(f"Error: '{source}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def grep(word=None, filename=None):
    """Search for a word in a file"""
    if not word or not filename:
        print("Error: 'grep' requires a word and a filename!")
        return
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if word in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def find(filename=None):
    """Find a file in the current directory and subdirectories"""
    if not filename:
        print("Error: 'find' requires a filename!")
        return
    found = False
    for root, _, files in os.walk("."):
        if filename in files:
            print(os.path.join(root, filename))
            found = True
    if not found:
        print(f"Error: '{filename}' not found!")

def history():
    """Show command history"""
    for index, command in enumerate(command_history, 1):
        print(f"{index}: {command}")

def chmod(mode=None, filename=None):
    """Change file permissions (Unix/Linux only)"""
    if not mode or not filename:
        print("Error: 'chmod' requires mode and filename!")
        return
    try:
        os.chmod(filename, int(mode, 8))
        print(f"Permissions changed: {filename} → {mode}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def head(filename=None, lines=10):
    """Display the first few lines of a file"""
    if not filename:
        print("Error: 'head' requires a filename!")
        return
    try:
        with open(filename, 'r') as file:
            for _ in range(int(lines)):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def tail(filename=None, lines=10):
    """Display the last few lines of a file"""
    if not filename:
        print("Error: 'tail' requires a filename!")
        return
    try:
        with open(filename, 'r') as file:
            all_lines = file.readlines()
            for line in all_lines[-int(lines):]:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")

def du():
    """Calculate the total size of the current directory"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk("."):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    print(f"Total size: {total_size / 1024:.2f} KB")

def ps():
    """List running processes"""
    for proc in psutil.process_iter(attrs=["pid", "name", "memory_info"]):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, Memory: {proc.info['memory_info'].rss / 1024:.2f} KB")

def kill(pid=None):
    """Terminate a process by PID"""
    if not pid:
        print("Error: 'kill' requires a PID!")
        return
    try:
        pid = int(pid)
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process terminated: PID {pid}")
    except psutil.NoSuchProcess:
        print(f"Error: PID {pid} not found!")
    except Exception as e:
        print(f"Error: {e}")

def df():
    """Show disk usage information"""
    disk_usage = psutil.disk_usage("/")
    print(f"Total: {disk_usage.total / (1024**3):.2f} GB")
    print(f"Used: {disk_usage.used / (1024**3):.2f} GB")
    print(f"Free: {disk_usage.free / (1024**3):.2f} GB")
    print(f"Usage Percentage: {disk_usage.percent}%")

def whoami():
    """Display the current username"""
    print(os.getlogin())

def uptime():
    """Show system uptime"""
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_str = time.strftime("%H hours, %M minutes, %S seconds", time.gmtime(uptime_seconds))
    print(f"System uptime: {uptime_str}")

def uname():
    """Display system information"""
    system_info = platform.uname()
    print(f"System: {system_info.system}")
    print(f"Machine: {system_info.machine}")
    print(f"Version: {system_info.version}")
    print(f"Kernel: {system_info.release}")
    print(f"Architecture: {system_info.processor}")


# Tüm komutları sözlük olarak tanımlıyoruz
commands = {
    "clear": clear_screen,
    "exit": exit_terminal,
    "ls": ls,
    "pwd": pwd,
    "mkdir": mkdir,
    "rm": rm,
    "touch": touch,
    "echo": echo,
    "cat": cat,
    "cp": cp,
    "mv": mv,
    "grep": grep,
    "find": find,
    "history": history,
    "chmod": chmod,
    "head": head,
    "tail": tail,
    "du": du,
    "ps": ps,
    "kill": kill,
    "df": df,
    "whoami": whoami,
    "uptime": uptime,
    "uname": uname,
}

def help_command():
    """List all available commands and their descriptions"""
    print("Available commands:")
    for cmd, func in commands.items():
        print(f"{cmd}: {func.__doc__}")

# Add the command to the commands dictionary
commands["help"] = help_command
