# Task Manager CLI Application

## Project Overview
This Task Manager is a command-line interface (CLI) application that allows users to manage their tasks effectively. The application supports adding, viewing, deleting, and marking tasks as completed. It also saves tasks to a file, so they can be reloaded upon restarting the program, ensuring persistent data storage.

## Features
1. **Add Task** - Users can add a new task with a unique ID, title, and completion status.
2. **View Tasks** - Displays all tasks along with their ID, title, and current status (Pending or Completed).
3. **Delete Task** - Deletes a specified task by its ID and reassigns IDs to maintain consistency.
4. **Complete Task** - Marks a specified task as completed.
5. **Save and Load** - Automatically saves tasks to a `tasks.json` file and loads them at startup, maintaining data across sessions.

## How to Run the Application
### Prerequisites
- Python 3.x installed on your machine.

### Steps
1. Clone this repository or download the code files.
2. Open a terminal or command prompt in the project directory.
3. Run the application with the following command:
   ```
   python task_manager.py
   ```
## Usage
Upon running the application, you will see a menu with the following options:

1. **Add a Task** - Allows you to enter a new task title. The application will assign it a unique ID and default it to "Pending" status.
2. **View Tasks** - Displays all tasks with their ID, title, and status.
3. **Delete a Task** - Prompts for the task ID to delete, then removes it from the list and reorders the remaining task IDs.
4. **Complete the Task** - Prompts for the task ID to mark as completed, updating its status.
5. **Exit** - Saves the tasks to a JSON file (tasks.json) and exits the program.
### Example
   ```
   Task Manager Menu
   1. Add a Task
   2. View Tasks
   3. Delete a Task
   4. Complete The Tasks
   5. Exit
   Choose an option: 1
   Enter the Task title: Buy groceries
   Task 'Buy groceries' is added.
   
   Task Manager Menu
   1. Add a Task
   2. View Tasks
   3. Delete a Task
   4. Complete The Tasks
   5. Exit
   Choose an option: 2 
   Task ID: 1, Task Title: Buy groceries, Status: Pending
   ```
## Code Structure
- task_manager.py: Main script that contains all functionality, including adding, viewing, deleting, completing, and saving tasks.
- tasks.json: Data file where tasks are stored in JSON format. It is automatically created and managed by the program.

## Error Handling
The program includes error handling for:

- Invalid inputs (non-integer task IDs).
- Empty or corrupted tasks.json file.
- Empty task titles when adding a task.

## File Persistence
The tasks are saved in `tasks.json`, and this file is loaded each time the program starts. If the file is corrupted or missing, the application will start with an empty task list.
