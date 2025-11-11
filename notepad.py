import time

print("notepad.py")
filename = input("filename? ")
path = filename + ".txt"
print(path)
try:
    with open(path, "x") as f:
        pass
except FileExistsError:
    print("File already exists, appending to it...")

time.sleep(0.5)
text = input("what to write to file? \n")

with open(path, "a") as f:
    f.write(text + "\n")

print("Done! Wrote to", path)
