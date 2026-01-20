import sys
from pystruct.main import *

def main():
    if len(sys.argv) < 2:
        print("Usage: pystruct [ml|web|ds|script|lib|pract|gitcom]")
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
    elif command == "gitcom":
        gitcom()
    else:
        print(f"Error: Command '{command}' not recognized.")
        print("Available commands: ml, web, ds, script, lib, pract, gitcom")