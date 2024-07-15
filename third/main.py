import sys
from pathlib import Path
from colorama import init, Fore, Style

def list_directory_contents(directory, prefix=""):
    items = list(directory.iterdir())
    for index, item in enumerate(items):
        connector = "┗" if index == len(items) - 1 else "┣"
        if item.is_dir():
            print(f"{prefix}{connector} 📂 {Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            list_directory_contents(item, prefix + ("  " if index == len(items) - 1 else "┃ "))
        else:
            print(f"{prefix}{connector} 📜 {Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ./third/main.py ./third/picture")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"The path '{directory_path}' does not exist.")
        return

    if not directory_path.is_dir():
        print(f"The path '{directory_path}' is not a directory.")
        return

    init(autoreset=True)
    print(f"📦{Fore.BLUE}{directory_path.name}/")
    list_directory_contents(directory_path)

if __name__ == "__main__":
    main()