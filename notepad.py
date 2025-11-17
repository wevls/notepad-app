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
            selection = int(input("\nMenu: 1) List 2) View 3) Append 4) Edit 5) Quit\n> "))
        except ValueError:
            print("Enter 1-5")
            continue

        if selection == 1:
            for e in os.listdir(dir_path):
                print(e)

        elif selection == 2:
            name = input("Filename: ")
            path = os.path.expanduser(name)
            if not os.path.isabs(path):
                path = os.path.join(dir_path, path)
            if not os.path.exists(path):
                print("Not found")
                continue
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    print(f.read())
            except OSError as e:
                print("Error:", e)

        elif selection == 3:
            name = input("Filename to append: ")
            path = os.path.expanduser(name)
            if not os.path.isabs(path):
                path = os.path.join(dir_path, path)
            print("Type lines. Single '.' on a line to finish.")
            try:
                with open(path, 'a', encoding='utf-8') as f:
                    while True:
                        line = input()
                        if line == '.':
                            break
                        f.write(line + '\n')
                print("Saved")
            except OSError as e:
                print("Error:", e)

        elif selection == 4:
            name = input("Filename to edit: ")
            path = os.path.expanduser(name)
            if not os.path.isabs(path):
                path = os.path.join(dir_path, path)
            lines = []
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                except OSError as e:
                    print("Error reading:", e)
                    continue

            dirty = False
            print("Commands: p=print, e <n>=edit, a=append, d <n>=delete, s=save, q=quit")
            while True:
                cmd = input("edit> ").strip()
                if not cmd:
                    continue
                if cmd == 'p':
                    for i, ln in enumerate(lines, 1):
                        print(f"{i}: {ln.rstrip()}")
                elif cmd.startswith('e '):
                    parts = cmd.split(maxsplit=1)
                    if len(parts) < 2 or not parts[1].isdigit():
                        print('Usage: e <line>')
                        continue
                    n = int(parts[1])
                    if 1 <= n <= len(lines):
                        new = input('New text: ')
                        lines[n-1] = new + '\n'
                        dirty = True
                    else:
                        print('No such line')
                elif cmd == 'a':
                    new = input('Append text: ')
                    lines.append(new + '\n')
                    dirty = True
                elif cmd.startswith('d '):
                    parts = cmd.split(maxsplit=1)
                    if len(parts) < 2 or not parts[1].isdigit():
                        print('Usage: d <line>')
                        continue
                    n = int(parts[1])
                    if 1 <= n <= len(lines):
                        lines.pop(n-1)
                        dirty = True
                    else:
                        print('No such line')
                elif cmd == 's':
                    try:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        print('Saved')
                        dirty = False
                    except OSError as e:
                        print('Error saving:', e)
                elif cmd == 'q':
                    if dirty:
                        yn = input('Unsaved changes — save? (y/N): ')
                        if yn.lower() == 'y':
                            try:
                                with open(path, 'w', encoding='utf-8') as f:
                                    f.writelines(lines)
                                print('Saved')
                            except OSError as e:
                                print('Error saving:', e)
                    break
                else:
                    print('Unknown')

        elif selection == 5:
            break

        else:
            print('Enter 1-5')


if __name__ == "__main__":
    note()
