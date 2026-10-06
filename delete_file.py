from pathlib import Path

FILE_PATH = Path("data/sample_write.txt")

def delete_file():
    """Delete a file if it exists."""

if FILE_PATH.exists():
    FILE_PATH.unlink()
    print(f"🗑️ File deleted successfully: {FILE_PATH}")
else:
    print(f"ℹ️ File does not exist: {FILE_PATH}")

def check_file():
    """Check whether the file exists."""

if FILE_PATH.exists():
    print(f"📄 File exists: {FILE_PATH}")
else:
    print(f"❌ File does not exist: {FILE_PATH}")

def main():
    """Run file deletion example."""

print("🗑️ Python File Deletion")
print("=" * 30)

print("\n1. Checking file")
check_file()

print("\n2. Deleting file")
delete_file()

print("\n3. Checking file again")
check_file()

if __name__ == "__main__":
    main()