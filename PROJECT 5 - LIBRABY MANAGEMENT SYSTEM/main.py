import json


# =====================================================
# LOAD DATA FROM JSON FILE
# =====================================================

try:

    with open("data.json", "r") as f:

        books = json.load(f)

except FileNotFoundError:

    books = []


# =====================================================
# SAVE DATA FUNCTION
# =====================================================

def save_data():

    with open("data.json", "w") as f:

        json.dump(books, f, indent=4)


# =====================================================
# MAIN LOOP
# =====================================================

while True:

    print("")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")
    print("")


    # =================================================
    # TAKING USER INPUT
    # =================================================

    try:

        User_input = int(
            input("Enter the number to select among list : ")
        )

    except ValueError:

        print("")
        print("Enter number only")
        continue


    # =================================================
    # FUNCTION FOR MENU OPERATIONS
    # =================================================

    def selection():


        # =============================================
        # ADD BOOK
        # =============================================

        if User_input == 1:

            book_name = input("Enter book name : ")

            author_name = input(
                "Enter author name of book : "
            )

            available = input(
                "If available enter true or false : "
            )


            # Storing dictionary inside list
            books.append({

                "book_name": book_name.lower(),

                "author": author_name.lower(),

                "available": available.lower()

            })


            save_data()

            print("")
            print("Book added successfully!")


        # =============================================
        # VIEW BOOKS
        # =============================================

        elif User_input == 2:

            if books == []:

                print("")
                print("No books exist")

            else:

                for book in books:

                    print("")

                    print(
                        f"Book Name : {book['book_name']}"
                    )

                    print(
                        f"Author Name : {book['author']}"
                    )

                    print(
                        f"Available : {book['available']}"
                    )


        # =============================================
        # BORROW BOOK
        # =============================================

        elif User_input == 3:

            book_borrow = input(
                "Enter book name to borrow : "
            )

            found = False


            for book in books:

                if (
                    book["book_name"].lower()
                    ==
                    book_borrow.lower()
                ):

                    found = True


                    if book["available"] == "true":

                        book["available"] = "false"

                        save_data()

                        print("")
                        print(
                            "Successfully borrowed!"
                        )

                    else:

                        print("")
                        print(
                            "Already borrowed"
                        )


            if found == False:

                print("")
                print("Not found")


        # =============================================
        # RETURN BOOK
        # =============================================

        elif User_input == 4:

            book_return = input(
                "Enter book name to return : "
            )

            found = False


            for book in books:

                if (
                    book["book_name"].lower()
                    ==
                    book_return.lower()
                ):

                    found = True


                    if book["available"] == "false":

                        book["available"] = "true"

                        save_data()

                        print("")
                        print(
                            "Successfully returned!"
                        )

                    else:

                        print("")
                        print(
                            "Book already available"
                        )


            if found == False:

                print("")
                print("Not found")


        # =============================================
        # DELETE BOOK
        # =============================================

        elif User_input == 5:

            book_delete = input(
                "Enter book name to delete : "
            )

            found = False


            for book in books:

                if (
                    book["book_name"].lower()
                    ==
                    book_delete.lower()
                ):

                    found = True


                    if book["available"] == "true":

                        books.remove(book)

                        save_data()

                        print("")
                        print(
                            "Successfully removed!"
                        )

                    else:

                        print("")
                        print(
                            "Someone borrowed this book"
                        )


            if found == False:

                print("")
                print("Not found")


        # =============================================
        # EXIT
        # =============================================

        elif User_input == 6:

            print("")
            print("Program terminates!")

            return False


        # =============================================
        # INVALID NUMBER
        # =============================================

        else:

            print("")
            print(
                "You are entering invalid number"
            )


        return True


    # =================================================
    # CALLING FUNCTION
    # =================================================

    if not selection():

        break