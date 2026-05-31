import json

# ==============================
# Expense Tracker Program
# ==============================

# List to store expenses of current user
expense_list = []

# Menu dictionary
menu = {
    "1. Add Expense": 1,
    "2. View Expenses": 2,
    "3. Show Total Expense": 3,
    "4. Delete Expense": 4,
    "5. Exit": 5
}

# ==============================
# Get User Name
# ==============================

name = input("Enter your name: ")

# ==============================
# Load Existing Data from JSON
# ==============================

try:
    with open("data.json", "r") as f:
        data = json.load(f)

except:
    # If file does not exist
    data = {}

# Check if user already exists
if name in data:
    expense_list = data[name]
    print(f"Welcome back {name}!")

else:
    print("Created new account!")

# ==============================
# Function to Save Data
# ==============================

def save(user_name):
    """
    Save current user's expense list into data.json
    """

    data[user_name] = expense_list

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


# ==============================
# Function to View Expenses
# ==============================

def view():
    """
    Display all expenses
    """

    for index, item in enumerate(expense_list, start=1):

        print(
            f"{index}. "
            f"{item['Expense']} - "
            f"{item['Amount']} - "
            f"{item['Category']}"
        )


# ==============================
# Main Menu Engine
# ==============================

def engine_of_menu(user_choice):

    # --------------------------------
    # 1. Add Expense
    # --------------------------------
    if user_choice == 1:

        expense_name = input("Enter name of expense: ")

        amount = int(input("Enter amount: "))

        category = input("Enter category: ")

        # Create dictionary for one expense
        dict_data = {
            "Expense": expense_name,
            "Amount": amount,
            "Category": category
        }

        # Add expense to list
        expense_list.append(dict_data)

        # Save data
        save(name)

        print()

    # --------------------------------
    # 2. View Expenses
    # --------------------------------
    elif user_choice == 2:

        if expense_list == []:
            print("No expenses entered.")

        else:
            view()

        print()

    # --------------------------------
    # 3. Show Total Expense
    # --------------------------------
    elif user_choice == 3:

        total_expense = 0

        for item in expense_list:
            total_expense += item["Amount"]

        print(f"Your total expense is {total_expense}")

        print()

    # --------------------------------
    # 4. Delete Expense
    # --------------------------------
    elif user_choice == 4:

        if expense_list == []:
            print("No expenses available to delete.")

        else:
            # Show expenses first
            view()

            expense_delete = int(
                input("Enter expense number to delete: ")
            )

            # Check valid number
            if expense_delete <= len(expense_list):

                expense_list.pop(expense_delete - 1)

                # Save updated data
                save(name)

                print("Successfully deleted.")

            else:
                print(
                    f"Expense number {expense_delete} not available."
                )

        print()

    # --------------------------------
    # 5. Exit Program
    # --------------------------------
    elif user_choice == 5:
        return False

    # Invalid menu choice
    else:
        print("Invalid menu choice.\n")

    return True


# ==============================
# Main Program Loop
# ==============================

while True:

    # Print Menu
    for item in menu.keys():
        print(item)

    try:
        print()

        user_choice = int(
            input("Enter the number to select: ")
        )

        print()

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    except Exception as e:
        print(e)
        continue

    # Run menu engine
    if not engine_of_menu(user_choice):
        break


print("Thank you for using Expense Tracker!")