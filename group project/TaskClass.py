from datetime import datetime


class Task:
    def __init__(self, name, description, priority, deadline):
        self.name = name
        self.description = description
        self.priority = priority
        try:
            self.deadline = datetime.strptime(deadline, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Please use the format MM/DD/YYYY (e.g 5/2/2024).")

    def __str__(self):
        return (f'Task: {self.name}\nDescription: {self.description}\nPriority: {self.priority}\nDeadline: {self.deadline.strftime("%m/%d/%Y")}')

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_priority(self):
        return self.priority

    def get_deadline(self):
        return self.deadline
    
    def update_task(self, name, description, priority, deadline):
        if name == "":
            name = self.name
        if description == "":
            description = self.description
        if priority == "":
            priority = self.priority
        if deadline == "":
            deadline = self.deadline

        self.name = name
        self.description = description
        self.priority = int(priority)
        self.deadline = deadline