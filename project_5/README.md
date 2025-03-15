# Project 5 -- CLI Task List

## Objective: 
- Build a console-based program to manage a to-do list, allowing users to add, remove, and display tasks, with the list saved to and loaded from a text file.

## Basic Knowledge / Concepts Needed  
- Variables: Store the list of tasks.  
- Input/Output: Interact with the user and handle file operations.  
- Lists: Manage the collection of tasks.  
- Loops: Provide a menu for repeated actions.  
- Conditionals: Handle user choices (add, remove, display).  
- File I/O: Read from and write to a text file for persistence.

## Modules/Packages
- os: Check if the file exists (optional for robustness).  

## Functions:  
print(): Display the menu, tasks, and messages.  
input(): Get user choices and task details.  
open(): Access the text file for reading/writing.  --> Args: Filename (e.g., "todo.txt"), mode ("r" for read, "w" for write, "a" for append).  --> Returns: File object (use with with statement for safety).
readlines(): Read all lines from the file into a list.  --> Called on a file object; returns list of strings.
write(): Write a string (task) to the file.  --> Called on a file object; takes a string (add \n for new lines).
os.path.exists(): Check if the file exists (optional).  --> Args: Filename; returns Boolean.

## Logic and Flow:  
- Start with an empty task list (or load from file if it exists).  
- Display a menu with options:  
- Add a task.  
- Save task.
- Remove a task (by number or name).  
- Display all tasks.  
- Quit (save to file).

### Based on user choice:  
- Add: Append task to list.  
- Remove: Delete task from list.  
- Display: Show numbered tasks.
- Save the updated list to the file when quitting.

Key Ideas:  
- Persistence: Tasks persist between runs via file.  
- Indexing: Use list indices for removal/display (e.g., "1. Buy milk").  
- User Input: Convert choice to integer for menu, handle task text as strings.  
- File Management: Read to load, write to save (overwrite or append).


## Example Output

To-Do List Menu:
1. Add Task
2. Remove Task
3. Display Tasks
4. Quit

Enter choice: 1
Enter a task: Buy milk

To-Do List Menu:
1. Add Task
2. Remove Task
3. Display Tasks
4. Quit

Enter choice: 3
1. Buy milk

To-Do List Menu:
1. Add Task
2. Remove Task
3. Display Tasks
4. Quit

Enter choice: 4
Tasks saved to file.

