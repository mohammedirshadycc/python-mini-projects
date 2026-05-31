import json

#Created dictionary only for key values as menu
menu = {"Add Task- 1":1,
        "View Task- 2":2,
        "Delete Task- 3":3,
        "Exit- 4" :4,}

#Empty list which stores tasks of user
user_task = []   

try:
    with open("data.json","r") as f:
        data=json.load(f)
except Exception:
    data={}

name = input("Enter your name: ") 


if name in data:
    user_task=data[name]
    print(f"Welcome back {name}")
else:
    print("Created new Account!")

def save_data(name):
    data[name]=user_task
    with open("data.json","w") as f:
        json.dump(data,f,indent=4)


#Main fuction for selection engine 
def selection(user_selection):
                         
        #if user select Add task by entering 1 , it will append in the list
        if (user_selection == 1):
            in_task =input("Enter your Task: ")
            user_task.append(in_task.upper())
            save_data(name)


        #if user select View Task by entering 2, it prints the existing list
        elif (user_selection == 2):
    
            if user_task == [] :
                 print("You entered nothing")
            else:
                print(user_task)


        #if user select Delete task by entering 3 , it will ask which task and remove from the list
        elif (user_selection == 3):
            in_task2 = input("Enter the Task to delete: ")
            if str(in_task2.upper()) in user_task:
                user_task.remove(in_task2.upper())
            else:
                 print("Make sure you entered correct task")


        #if user select Exit by entering 4, it return false which can be use to break the loop 
        elif user_selection == 4:
            return False
        
        
        #if user enter other number than this , it prints invalid number
        else:
             print("invalid number")

        #whole function return true to run infinite loop     
        return True


        

#Using while loop for representing the menu again and again
while True:
    #For displaying menu
    for i in menu.keys():
        print(i)

    #Using try to handle the error
    try:
        user_selection = int(input("Enter the number: "))
        
    except Exception as e:
        print("Enter between 1 to 4 to run the program",e)
        continue

            
    #If user enter 4 it will exit the loop or continue till exit
    if not selection(user_selection):
        break

