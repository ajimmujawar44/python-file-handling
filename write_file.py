from pathlib import Path

FILE_PATH = Path("data/sample_write.txt")

def write_file():
    """
Write content to a file.

Warning:
Write mode ('w') replaces existing file content.
    """

with FILE_PATH.open("w", encoding="utf-8") as file:
    file.write("Hello from Python File Handling!\n")
    file.write("This file was created using Python.\n")
    file.write("Write mode replaces existing content.\n")

print(f"✅ File written successfully: {FILE_PATH}")

def append_file():
    """
Add new content to the end of an existing file.

Append mode ('a') preserves existing content.
    """

with FILE_PATH.open("a", encoding="utf-8") as file:
    file.write("This line was added using append mode.\n")

print(f"✅ Content appended successfully: {FILE_PATH}")

def read_file():
    """Read and display the current file content."""

    if not FILE_PATH.exists():
        print(f"❌ File not found: {FILE_PATH}")
    return

with FILE_PATH.open("r", encoding="utf-8") as file:
    content = file.read()

print("\n📖 Current File Content:")
print(content)

def main():
    """Run writing and appending examples."""

print("✍️ Python File Writing")
print("=" * 30)

print("\n1. Writing to file")
write_file()

print("\n2. Appending to file")
append_file()

print("\n3. Reading updated file")
read_file()

if __name__ == "__main__":
    main()