# Expense Tracker 💰

A simple Python Expense Tracker application that allows users to:

* Add expenses
* View expenses
* Calculate total expenses
* Delete expenses
* Save data permanently using JSON

---

# Features 🚀

✅ Create multiple user accounts
✅ Save expenses in `data.json`
✅ View all expenses with categories
✅ Calculate total spending
✅ Delete unwanted expenses
✅ Data remains saved after closing program

---

# Technologies Used 🛠️

* Python
* JSON File Handling

---

# Project Structure 📁

```plaintext
ExpenseTracker/
│
├── main.py
├── data.json
└── README.md
```

---

# How It Works ⚙️

When the program starts:

1. User enters their name
2. Program checks if user already exists
3. Existing expenses are loaded
4. User can manage expenses using menu options

---

# Menu Options 📋

```plaintext
1. Add Expense
2. View Expenses
3. Show Total Expense
4. Delete Expense
5. Exit
```

---

# Example Output 🖥️

```plaintext
Enter your name: Irshad

1. Add Expense
2. View Expenses
3. Show Total Expense
4. Delete Expense
5. Exit

Enter the number to select: 1

Enter name of expense: Food
Enter amount: 250
Enter category: Daily Needs
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

All expenses are stored inside:

```plaintext
data.json
```

Example:

```json
{
    "Irshad": [
        {
            "Expense": "Food",
            "Amount": 250,
            "Category": "Daily Needs"
        }
    ]
}
```

---

# Future Improvements 🔥

* Add expense date & time
* Monthly expense reports
* GUI version using Tkinter
* Charts and graphs
* Expense categories summary

---

# Author 👨‍💻

Created by Irshad

---

# License 📄

This project is free to use for learning purposes.
