from pathlib import Path

FILE_PATH = Path("data/sample_read.txt")

def read_entire_file():

    """Read and display the complete file content."""

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
        return

with FILE_PATH.open("r", encoding="utf-8") as file:
    content = file.read()

print("File Content:")
print(content)

def read_first_line():

    """Read and display the first line of the file."""

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
    return

with FILE_PATH.open("r", encoding="utf-8") as file:
    first_line = file.readline()

print("First Line:")
print(first_line.strip())

def read_all_lines():
    """Read and display all lines using readlines()."""

    if not FILE_PATH.exists():
        print(f"File not found: {FILE_PATH}")
    return

with FILE_PATH.open("r", encoding="utf-8") as file:
    lines = file.readlines()

print("All Lines:")

for line in lines:
    print(line.strip())

def main():
    """Run file reading examples."""

print("Python File Reading")
print("=" * 30)

print("\n1. read()")
read_entire_file()

print("\n2. readline()")
read_first_line()

print("\n3. readlines()")
read_all_lines()

if __name__ == "__main__":
    main()