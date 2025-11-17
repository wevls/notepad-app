import os


def note():
    """Simple interactive note reader.

    Menu:
    1 - list files in the script directory
    2 - open and read a file (prints contents)
    3 - quit

    This fixes the previous behavior where the file object was printed
    instead of its contents and where exceptions were swallowed.
    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    print("Script directory:", dir_path)

    while True:
        try:
            selection = int(input(
                "\nmenu, pick an option:\n 1. list files in directory\n 2. open and read a file\n 3. quit\n> "
            ))
        except ValueError:
            print("Please enter a number (1-3).")
            continue

        if selection == 1:
            try:
                entries = os.listdir(dir_path)
                print("Files in directory:")
                for e in entries:
                    print(" -", e)
            except OSError as e:
                print("Error listing directory:", e)

        elif selection == 2:
            namefile = input("Enter filename (relative to script or full path): ")
            # allow absolute or relative paths
            path = os.path.expanduser(namefile)
            if not os.path.isabs(path):
                path = os.path.join(dir_path, path)

            if not os.path.exists(path):
                print(f"File not found: {path}")
                continue

            try:
                with open(path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                print("\n--- file content start ---\n")
                print(content)
                print("\n--- file content end ---\n")
            except OSError as e:
                print("Error opening/reading file:", e)

        elif selection == 3:
            print("Goodbye")
            break

        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    note()
