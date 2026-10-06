
from pathlib import Path


FILE_PATH = Path("data/sample_read.txt")


def read_file():
    """Read the complete file."""

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
        return

    with FILE_PATH.open("r", encoding="utf-8") as file:
        content = file.read()

    print("File Content:")
    print(content)


def check_file_exists():
    """Check whether the file exists."""

    if FILE_PATH.exists():
        print(f"File exists: {FILE_PATH}")
    else:
        print(f"File does not exist: {FILE_PATH}")


def show_file_info():
    """Display basic file information."""

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
        return

    print(f"File name: {FILE_PATH.name}")
    print(f"File extension: {FILE_PATH.suffix}")
    print(f"File size: {FILE_PATH.stat().st_size} bytes")


def main():
    """Run all file handling examples."""

    print("=" * 40)
    print("Python File Handling Examples")
    print("=" * 40)

    print("\n1. Check File")
    check_file_exists()

    print("\n2. Read File")
    read_file()

    print("\n3. File Information")
    show_file_info()


if __name__ == "__main__":
    main()

