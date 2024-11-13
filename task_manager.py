import json

class Task:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self):
        """Adds a new task with a unique ID, title, and completion status."""
        task_id = len(self.tasks) + 1
        title = input('Enter the Task title: ')
        # Handle empty titles
        if not title.strip():  
            print("Task title cannot be empty.")
            return
        completed = False
        self.tasks.append({'id': task_id, 'title': title, 'completed': completed})
        print(f"Task '{title}' is added.")

    def view_tasks(self):
        """Displays all tasks with their ID, title, and completion status."""
        if self.tasks:
            for task in self.tasks:
                status = "Completed" if task['completed'] else "Pending"
                print(f"Task ID: {task['id']}, Task Title: {task['title']}, Status: {status}")
        else:
            print("No tasks available.")

    def delete_task(self):
        """Deletes a task by its ID and reassigns IDs if needed."""
        try:
            task_id = int(input('Enter the Task ID to delete: '))
            for task in self.tasks:
                if task['id'] == task_id:
                    self.tasks.remove(task)
                    print(f"Task '{task['title']}' is deleted.")
                    for index, task in enumerate(self.tasks):
                        task['id'] = index + 1
                    return
            print(f'Task with ID {task_id} not found.')
        except ValueError:
            print("Please enter a valid task ID.")

    def update_task(self):
        """Marks a task as completed by updating its status to True."""
        try:
            task_id = int(input('Enter the Task ID to mark as completed: '))
            for task in self.tasks:
                if task['id'] == task_id:
                    task['completed'] = True
                    print(f"Task '{task['title']}' marked as completed.")
                    return
            print(f'Task with ID {task_id} not found.')
        except ValueError:
            print("Please enter a valid task ID.")

    def exit(self):
        """Saves tasks to the file and exits the application."""
        self.save_tasks()
        print("Thanks for visiting our application.")

    def save_tasks(self):
        """Saves all tasks to a JSON file for persistent storage."""
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks have been saved.")

    def load_tasks(self):
        """Loads tasks from a JSON file if it exists, otherwise starts with an empty list."""
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error loading tasks. Starting with an empty task list.")
            self.tasks = []

options = ['Add a Task', 'View Tasks', 'Delete a Task', 'Complete The Tasks', 'Exit']
task_manager = Task()

def display_menu():
    """Displays the menu and handles user input to execute corresponding functions."""
    while True:
        print("\nTask Manager Menu")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            user_input = int(input('Choose an option: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_input == 1:
            task_manager.add_task()
        elif user_input == 2:
            task_manager.view_tasks()
        elif user_input == 3:
            task_manager.delete_task()
        elif user_input == 4:
            task_manager.update_task()
        elif user_input == 5:
            task_manager.exit()
            break
        else:
            print('Invalid option. Please choose a valid option.')

display_menu()
