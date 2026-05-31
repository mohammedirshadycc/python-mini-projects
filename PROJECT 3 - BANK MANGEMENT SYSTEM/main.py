
import json


# =========================
# FUNCTION TO SAVE DATA
# =========================

def save():

    with open("data.json", "w") as f:

        json.dump(Data, f, indent=4)



# =========================
# MENU DICTIONARY
# =========================

menu = {

    "1.Create/login account": 1,
    "2.Deposit money": 2,
    "3.Withdraw money": 3,
    "4.Check balance": 4,
    "5.Delete account": 5,
    "6.Exit program": 6
}



# =========================
# LOADING OLD ACCOUNT DATA
# =========================

try:

    with open("data.json", "r") as f:

        Data = json.load(f)

except FileNotFoundError:

    Data = {}



# =========================
# GLOBAL VARIABLE
# STORES CURRENT LOGGED USER
# =========================

account_name = ""



# =========================
# MAIN SYSTEM FUNCTION
# =========================

def System(User_input):

    global account_name



    # =========================
    # CREATE / LOGIN ACCOUNT
    # =========================

    if User_input == 1:

        print("")

        account_name = input("Enter name : ")


        # If account already exists
        if account_name in Data:

            print("")

            print("Welcome back sir!")


        # Create new account
        else:

            print("")

            print("Created new account!")

            Data[account_name] = 0

            save()



    # =========================
    # DEPOSIT MONEY
    # =========================

    elif User_input == 2:

        # Check if account exists
        if account_name in Data:

            try:

                deposit_money = int(
                    input("Enter amount to deposit into your account : ")
                )


                # Deposit must be greater than 0
                if deposit_money > 0:

                    Data[account_name] += deposit_money

                    print("")

                    print(f"Your {deposit_money} has deposited!")

                    save()

                else:

                    print("You are entering negative number or zero")


            except ValueError:

                print("")

                print("Enter only number even comma's are not allowed")


        else:

            print("First create/login an account to deposit!")



    # =========================
    # WITHDRAW MONEY
    # =========================

    elif User_input == 3:

        # Check if account exists
        if account_name in Data:

            try:

                withdraw_money = int(
                    input("Enter amount to withdraw into your account : ")
                )


                # Check balance and valid amount
                if withdraw_money > 0 and withdraw_money <= Data[account_name]:

                    Data[account_name] -= withdraw_money

                    print("")

                    print(f"Your {withdraw_money} has withdrawal!")

                    save()

                else:

                    print("Insufficient balance")


            except ValueError:

                print("")

                print("Enter only number even comma's are not allowed")


        else:

            print("First create/login an account to withdrawal!")



    # =========================
    # CHECK BALANCE
    # =========================

    elif User_input == 4:

        if account_name in Data:

            print(f"Your balance is {Data[account_name]}")

        else:

            print("First create/login an account to check balance!")



    # =========================
    # DELETE ACCOUNT
    # =========================

    elif User_input == 5:

        if account_name in Data:

            Data.pop(account_name)

            print(f"Your account {account_name} is deleted!")

            save()


            # Reset current user
            account_name = ""

        else:

            print("First create/login an account to delete account!")



    # =========================
    # EXIT PROGRAM
    # =========================

    elif User_input == 6:

        print("Program terminates!!!")

        print("")

        return False



    # =========================
    # INVALID MENU INPUT
    # =========================

    else:

        print("You are entering invalid number of the list to select")


    return True




# =========================
# MAIN LOOP
# =========================

while True:

    print("")


    # Display menu
    for i in menu.keys():

        print(i)

    print("")



    # Taking menu input
    try:

        User_input = int(
            input("Enter your choice number to go ahead: ")
        )

        print("")


    except ValueError:

        print("")

        print("Enter number of list to select")

        continue



    # Run main system
    if not System(User_input):

        break

