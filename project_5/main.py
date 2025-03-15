


def ask_for_action():

    running = True

    while running:
        print("To-Do List Menu:")
        print("1: Add Task")
        print("2: Display Tasks")
        print("3: Remove Task")
        print("4: Quit and Save")
        print()

        todo_list_file = open("todo_list.txt", "w+")
        action = input("Enter a choice: ")
        if int(action) == 1:
            print("You added a task!")
            todo_list_file.write("Added Task\n")
            print()
        elif int(action) == 2:
            print("You displayed your tasks!")
            todo_list_file.read()
            print()
        elif int(action) == 3:
            print("You removed a task")
            print()
        elif int(action) == 4:
            print("You saved and quit")
            print()
            running = False
        else:
            print("That input is not recognized")
            print()
        todo_list_file.close()
    

ask_for_action()