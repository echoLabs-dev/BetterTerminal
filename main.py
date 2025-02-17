import commands

def run_terminal():
    while True:
        cmd_input = input("[BetterTerminal]-> ").strip()
        if not cmd_input:
            continue

        cmd_parts = cmd_input.split()
        cmd = cmd_parts[0]  # First word is the command name
        args = cmd_parts[1:]  # The rest are arguments

        # Add to command history
        commands.command_history.append(cmd_input)

        if cmd in commands.commands:
            try:
                commands.commands[cmd](*args)  # Pass arguments to the function
            except TypeError:
                print(f"Error: Missing or incorrect arguments for command '{cmd}'!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Command not found!")

if __name__ == "__main__":
    run_terminal()
