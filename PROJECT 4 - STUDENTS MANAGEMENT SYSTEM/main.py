import json


# =====================================================
# LOAD DATA FROM JSON FILE
# =====================================================

try:

    with open("data.json", "r") as f:
        data = json.load(f)

except FileNotFoundError:

    data = {}


# =====================================================
# STUDENT CLASS
# =====================================================

class Student:

    # Constructor
    def __init__(self, name, roll, marks):

        self.name = name
        self.roll = roll
        self.marks = marks


    # Display student details
    def show_student(self):

        print(f"Name  : {self.name}")
        print(f"Roll  : {self.roll}")
        print(f"Marks : {self.marks}")


# =====================================================
# SAVE NEW STUDENT DATA
# =====================================================

def save_data(roll, name, marks):

    # Saving data inside dictionary
    data[str(roll)] = {
        "Name": name,
        "Marks": marks
    }

    # Saving dictionary into JSON file
    with open("data.json", "w") as f:

        json.dump(data, f, indent=4)


# =====================================================
# SAVE UPDATED DATA
# =====================================================

def save():

    with open("data.json", "w") as f:

        json.dump(data, f, indent=4)


# =====================================================
# MAIN MENU FUNCTION
# =====================================================

def UserChoice(User_input):


    # =================================================
    # ADD STUDENT
    # =================================================

    if User_input == 1:

        name = input("Enter name of the student : ")


        # Function for roll and marks validation
        def num():

            try:

                roll = int(input("Enter roll number : "))


                # Checking if roll already exists
                if str(roll) in data:

                    print("")
                    print("Already existing roll number")


                else:

                    marks = int(
                        input("Enter marks of the student : ")
                    )


                    # Checking valid marks range
                    if marks > 0 and marks <= 100:

                        # Creating student object
                        student = Student(name, roll, marks)

                        # Saving data
                        save_data(roll, name, marks)

                        print("")
                        print("Student added successfully!")


                    else:

                        print("Enter marks between 0 to 100")


            except ValueError:

                print("")
                print("Enter roll/marks in numbers only")
                print("")

                # Calling function again if invalid
                num()


        num()


    # =================================================
    # VIEW ALL STUDENTS
    # =================================================

    elif User_input == 2:

        if data == {}:

            print("")
            print("No student records found")

        else:

            for roll, detail in data.items():

                print("")

                print(f'Name  : {detail["Name"]}')
                print(f'Roll  : {roll}')
                print(f'Marks : {detail["Marks"]}')


    # =================================================
    # SEARCH STUDENT
    # =================================================

    elif User_input == 3:

        roll = input("Enter roll number to find : ")

        if roll in data:

            detail = data[roll]

            print("")

            print(f'Name  : {detail["Name"]}')
            print(f'Roll  : {roll}')
            print(f'Marks : {detail["Marks"]}')


        else:

            print("")
            print("Student not found, check again")


    # =================================================
    # UPDATE STUDENT MARKS
    # =================================================

    elif User_input == 4:

        roll = input(
            "Enter roll number of student to update marks : "
        )


        if roll in data:

            detail = data[roll]

            try:

                new_marks = int(
                    input("Enter marks of the student : ")
                )


                # Validating marks
                if new_marks > 0 and new_marks <= 100:

                    print("")

                    # Updating marks
                    detail.update({
                        "Marks": new_marks
                    })

                    save()

                    print("Marks updated successfully!")


                else:

                    print("Enter marks between 0 to 100")


            except ValueError:

                print("Enter only numbers")


        else:

            print("")
            print("Student not found, check again")


    # =================================================
    # DELETE STUDENT
    # =================================================

    elif User_input == 5:

        roll = input("Enter roll number to delete : ")


        if roll in data:

            # Removing student from dictionary
            data.pop(roll)

            save()

            print("")
            print("Student deleted successfully!")


        else:

            print("")
            print("Student not found, check again")


    # =================================================
    # EXIT PROGRAM
    # =================================================

    elif User_input == 6:

        print("")
        print("Program terminates!")
        print("")

        return False


    # =================================================
    # INVALID MENU INPUT
    # =================================================

    else:

        print("")
        print("You are entering invalid number of list")


    return True


# =====================================================
# MAIN LOOP
# =====================================================

while True:

    print("")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    print("")


    try:

        User_input = int(
            input("Enter a number to select the following : ")
        )


    except ValueError:

        print("")
        print(
            "You are entering other than a number between 1 to 6"
        )

        continue


    # Stop program if function returns False
    if not UserChoice(User_input):

        break