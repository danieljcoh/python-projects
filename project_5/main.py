


def ask_for_action():

    running = True
    num_of_tasks = 0
    try:
        todo_list_file = open("todo_list.txt", "x")
    except FileExistsError: 
        pass # ---> means it already exists

    while running:
        print("To-Do List Menu:")
        print("1: Add Task")
        print("2: Display Tasks")
        print("3: Remove Task")
        print("4: Quit and Save")
        print()

        action = input("Enter a choice: ")
        if int(action) == 1:
            todo_list_file = open("todo_list.txt", "a+")
            task_to_add = input("Whats the task: ")
            todo_list_file.write(f"{num_of_tasks}: {task_to_add}\n")
            print("You added a task!")
            num_of_tasks += 1
            todo_list_file.close()
            print()

        elif int(action) == 2:
            todo_list_file = open("todo_list.txt", "r+")
            for task in todo_list_file.readlines():
                print(task, end="")
            todo_list_file.close()
            print()

        elif int(action) == 3:
            print("You removed a task")
            num_of_tasks -= 1
            print()

        elif int(action) == 4:
            print("You saved and quit")
            todo_list_file.close()
            print()

            running = False
        else:
            print("That input is not recognized")
            print()

ask_for_action()