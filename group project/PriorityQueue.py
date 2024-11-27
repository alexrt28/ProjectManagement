class PriorityQueue:
    def __init__(self):
        self.queue = []  # Initialize the queue to store tasks.

    def add_task(self, task):
        """Add a task to the queue."""
        self.queue.append(task)  # Simply append the task to the queue.

    def view_tasks(self):
        """View all tasks in the queue."""
        if not self.queue:
            print("No tasks in the queue.")
        else:
            for task in self.queue:
                print(task)  # Use Task's __str__ method to display task details.

    def update_task(self, task_name, new_name="", new_description="", new_priority=0, new_deadline=""):
        """Update a task by its name."""
        for task in self.queue:
            if task.get_name() == task_name:  # Find the task by name
                task.update_task(new_name, new_description, new_priority, new_deadline)  # Update task
                print(f"Task '{task_name}' updated.")
                break
        else:
            print("Task not found.")

    def remove_task(self, task_name):
        """Remove a task from the queue."""
        for task in self.queue:
            if task.get_name() == task_name:  # Find the task by name
                self.queue.remove(task)  # Remove the task from the list
                print(f"Task '{task_name}' removed.")
                break
        else:
            print("Task not found.")

    def complete_task(self, task_name):
        """Mark a task as completed."""
        for task in self.queue:
            if task.get_name() == task_name:  # Find the task by name
                task.complete()  # Mark the task as completed
                print(f"Task '{task_name}' marked as completed.")
                break
        else:
            print("Task not found.")