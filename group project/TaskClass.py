from datetime import datetime


class Task:
    def __init__(self, name, description, priority, deadline):
        """Initialize the Task object with a name, description, priority, and deadline.
        Deadline is a string in the format MM/DD/YYYY"""
        self.name = name
        self.description = description
        self.priority = priority
        try:
            self.deadline = datetime.strptime(deadline, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please use the format MM/DD/YYYY (e.g 5/2/2024).")

        self.priority_str = {1: "Extreme", 2: "High", 3: "Medium", 4: "Low"}

    def __str__(self):
        """Return a string representation of the Task object."""
        return (f'Task Name: {self.name}\nDescription: {self.description}\nPriority: {self.priority_str[self.priority]}\nDeadline: {self.deadline.strftime("%m/%d/%Y")}')

    def get_name(self):
        """Return the name of the task."""
        return self.name

    def get_description(self):
        """Return the description of the task."""
        return self.description

    def get_priority(self):
        """Return the priority of the task."""
        return self.priority

    def get_deadline(self):
        """Return the deadline of the task."""
        return self.deadline.strftime("%m/%d/%Y")
    
    def update_task(self, name, description):
        """Update the name and description of the task."""
        self.name = name
        self.description = description