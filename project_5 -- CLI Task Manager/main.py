
def ask_for_action():

    running = True
    
    try:
        todo_list_file = open("todo_list.txt", "x+")
        todo_list_file.close()
    except FileExistsError: 
        pass # ---> means it already exists

    # Count existing tasks
    todo_list_file = open("todo_list.txt", "r")
    num_of_tasks = len(todo_list_file.readlines())
    todo_list_file.close()

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
            todo_list_file = open("todo_list.txt", "r")
            task_lines = todo_list_file.readlines()
            todo_list_file.close()
            
            # Display tasks
            for task in task_lines:
                print(task, end="")
            
            task_to_delete = int(input("which task do you want to delete: "))
            
            # Validate task number
            if task_to_delete <= 0 or task_to_delete > len(task_lines):
                print("The task doesn't exist!")
            else:
                # Create new list without deleted task and with updated numbering
                new_lines = []
                new_num = 1
                
                for i, task in enumerate(task_lines, 1):
                    if i != task_to_delete:
                        # Get the task description without the number
                        task_content = task.split(":", 1)[1].strip()
                        new_lines.append(f"{new_num}: {task_content}\n")
                        new_num += 1
                
                # Write updated tasks to file
                todo_list_file = open("todo_list.txt", "w")
                todo_list_file.writelines(new_lines)
                todo_list_file.close()
                
                print(f"You removed task {task_to_delete}!")
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