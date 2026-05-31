# To-Do List Application 📝

A simple Python To-Do List application that helps users manage daily tasks.

The program allows users to:

* Add tasks
* View tasks
* Delete tasks
* Save tasks permanently using JSON

---

# Features 🚀

✅ Multiple user support
✅ Save tasks in `data.json`
✅ Add unlimited tasks
✅ Delete completed tasks
✅ Data remains saved after program closes
✅ Beginner-friendly project structure

---

# Technologies Used 🛠️

* Python
* JSON File Handling

---

# Project Structure 📁

```plaintext
ToDoList/
│
├── main.py
├── data.json
└── README.md
```

---

# How the Program Works ⚙️

1. User enters their name
2. Program checks existing data
3. Old tasks are loaded if account exists
4. User can manage tasks using menu options

---

# Menu Options 📋

```plaintext
Add Task - 1
View Task - 2
Delete Task - 3
Exit - 4
```

---

# Example Output 🖥️

```plaintext
Enter your name: Irshad

Created new Account!

Add Task - 1
View Task - 2
Delete Task - 3
Exit - 4

Enter the number: 1

Enter your Task: Learn Python
```

---

# How to Run ▶️

## Step 1: Install Python

Download Python from:

https://www.python.org/

---

## Step 2: Run the Program

Open terminal or command prompt and run:

```bash
python main.py
```

---

# Data Storage 💾

All tasks are stored inside:

```plaintext
data.json
```

Example:

```json
{
    "Irshad": [
        "LEARN PYTHON",
        "COMPLETE PROJECT"
    ]
}
```

---

# Concepts Used 📚

This project uses:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* Exception Handling
* File Handling
* JSON

---

# Future Improvements 🔥

* Add task priority
* Add due dates
* Mark tasks as completed
* GUI version using Tkinter
* Search tasks feature

---

# Author 👨‍💻

Created by Irshad

---

# License 📄

This project is free to use for learning purposes.
