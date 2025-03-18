import json
import os

TASKS_FILE = "tasks.json"


# Optimization:
# - The read function should really just read the file and return it in a variable
# - Making the dictionary key a int --> Not a string
# - Fix indexing, when deleting objects, the indexing gets messed up


def read_data():
    """Loads tasks file if it exists and returns an empty [] if it doesn't"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
            for key,value in data.items():
                print(f"{int(key) + 1}: {value}")
    else:
        print("There are currently no tasks.")
        return []


def save_task(task):
    """if the file exists, opens it and writes over the existing file with the new task otherwise it'll create the file."""
    if os.path.exists(TASKS_FILE):
        data = dict()
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
        with open(TASKS_FILE, "w") as file:
            data[len(data)] = task
            json.dump(data, file, indent=4)
    else:
        data = dict()
        with open(TASKS_FILE, "w") as file:
            data[len(data)] = task
            json.dump(data, file, indent=4)


def delete_task(task_number):
    """Deletes a designated task and then rewrites the json in the file"""
    if os.path.exists(TASKS_FILE):
        data = dict()
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
        with open(TASKS_FILE, "w") as file:
            del data[str(task_number)]
            json.dump(data, file, indent=4)



def task_list_program():
    while True: 
        print("\n\n")
        print("1: View Tasks")
        print("2; Add a Task")
        print("3: Delete a Task")
        print("4: Save and Quit")
        option = int(input("What would you like to do? "))
        if option == 1:
            read_data()
            print("\n\n")

        elif option == 2:
            print("You added a task")
            task = input("What would you like to add: ")
            save_task(task)
            print("\n\n")

        elif option == 3:
            task_number = int(input("Which task do you want to delete: "))
            delete_task(task_number)
            print("\n\n")

        elif option == 4:
            print("You quit the program")
            return False
        
        else:
            print("The input was not recognized")

task_list_program()


# if __name__ == "main.py":
#     task_list_program()
