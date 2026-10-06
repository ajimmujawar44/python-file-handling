from pathlib import Path

FILE_PATH = Path("data/sample_read.txt")

def read_using_context_manager():
    """
Read a file using the 'with open()' context manager.

The context manager automatically closes the file
after the operation is completed.
    """

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
    return

with FILE_PATH.open("r", encoding="utf-8") as file:
    content = file.read()

print("📖 File Content:")
print(content)

print("\n✅ File automatically closed by the context manager.")

def write_using_context_manager():
    """Write data to a file using a context manager."""

output_file = Path("data/context_manager_output.txt")

with output_file.open("w", encoding="utf-8") as file:
    file.write("Hello from the context manager!\n")
    file.write("The file will be automatically closed.\n")

print(f"\n✅ File written successfully: {output_file}")

def main():
    """Run context manager examples."""

print("🔒 Python Context Manager - File Handling")
print("=" * 45)

print("\n1. Reading using context manager")
read_using_context_manager()

print("\n2. Writing using context manager")
write_using_context_manager()

if __name__ == "__main__":
    main()