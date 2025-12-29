import sys
from pystruct.main import ml, web, ds, script, lib, pract

def main():
    """Main Entry Point for the CLI."""
    if len(sys.argv) < 2:
        print("Usage: pystruct [ml|web|ds|script|lib]")
        return

    command = sys.argv[1].lower()
    command2 = sys.argv[2] if len(sys.argv) > 2 else None

    if command == "ml":
        ml()
    elif command == "web":
        web()
    elif command == "ds":
        ds()
    elif command == "script": 
        script()
    elif command == "lib":
        lib(command2)
    elif command == "pract":
        pract(command2)
    else:
        print(f"Error: Command '{command}' not recognized.")
        print("Available commands: ml, web, ds, script, lib")