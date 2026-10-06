# 🐍 Python File Handling

A beginner-friendly Python project demonstrating the fundamentals of **file handling in Python**, including reading, writing, appending, deleting files, using context managers, and working with file paths using `pathlib`.

## 📌 What is File Handling?

File handling allows a Python program to **create, read, write, update, and delete files** stored on a computer.

For example:

```text
Python Program
      │
      ├── 📖 Read
      ├── ✍️ Write
      ├── ➕ Append
      ├── 📄 Create
      └── 🗑️ Delete
```

File handling is useful when we need to store data permanently instead of keeping it only in program memory.

---

## 📂 Project Structure

```text
python-file-handling/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── sample_read.txt
│   └── sample_write.txt
│
├── src/
│   ├── read_file.py
│   ├── write_file.py
│   ├── file_with_context_manager.py
│   └── delete_file.py
│
└── examples/
    └── file_handling_examples.py
```

---

## 📚 Concepts Covered

### 1. Read a File

Python provides several ways to read file content:

```python
file.read()
file.readline()
file.readlines()
```

Example:

```python
with open("data/sample_read.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

---

### 2. Write to a File

The `"w"` mode is used to write data.

```python
with open("data/sample_write.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!")
```

⚠️ **Important:** Write mode can overwrite existing content.

---

### 3. Append to a File

The `"a"` mode adds content to the end of an existing file.

```python
with open("data/sample_write.txt", "a", encoding="utf-8") as file:
    file.write("\nNew content added.")
```

Existing content is preserved.

---

### 4. Context Manager

The recommended way to work with files is:

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The `with` statement automatically closes the file after the operation is completed.

```text
with open()
     ↓
Open file
     ↓
Perform operation
     ↓
Automatically close ✅
```

---

### 5. Delete a File

Python's `pathlib` can be used to delete files:

```python
from pathlib import Path

file_path = Path("data/sample_write.txt")

if file_path.exists():
    file_path.unlink()
```

---

## 🔑 File Modes

| Mode | Purpose           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write / overwrite |
| `a`  | Append            |
| `x`  | Create a new file |
| `r+` | Read and write    |

---

## 🛠️ Technologies Used

* Python 3
* Python Standard Library
* `pathlib`

No external packages are required.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-file-handling.git
```

### 2. Open the project

```bash
cd python-file-handling
```

### 3. Run an example

```bash
python examples/file_handling_examples.py
```

Or run an individual file:

```bash
python src/file_with_context_manager.py
```

---

## 🎯 Learning Goals

After completing this project, you should understand:

* How to open files
* How to read files
* How to write files
* How to append data
* How to delete files
* How `with open()` works
* Why context managers are useful
* How to use `pathlib`
* How to create portable file paths

---

## 👨‍💻 Author

**Ajim Mujawar**

Learning Python, Data Science, Machine Learning, Generative AI and Agentic AI.

---

## ⭐ If this project helped you learn Python

Feel free to star ⭐ the repository and use the examples for your own Python learning journey.
