from TaskClass import Task

class TaskPriorityQueue:
    def __init__(self, SourceCollection=None):
        self.queue = []  # Initialize the queue to store tasks.

        if SourceCollection:
            for item in SourceCollection:
                self.add_task(item)  # Add each item from the source collection to the queue if there is one.
    
    def __iter__(self):
        """Allow the queue to be iterable."""
        for item in self.queue:
            yield item;  # Allow the queue to be iterable.
    
    def __len__(self):
        """Return the length of the queue."""
        return len(self.queue)  # Return the length of the queue.

    def isEmpty(self):
        """Check if the queue is empty."""
        return len(self) == 0 # Check if the queue is empty
    
    def get_task(self, task_name):
        """Get a task by its name."""
        for task in self:
            if task.get_name() == task_name:
                return task  # Return the task if it is found

    def add_task(self, new_task):
        """Add a task to the queue."""
        if self.isEmpty():
            self.queue.append(new_task)  # Add the task to the end of the queue if it is empty.
        else:
            for i in range(len(self.queue)):
                if new_task.get_priority() < self.queue[i].get_priority():
                    self.queue.insert(i, new_task)  # Insert the task at the appropriate location in the queue.
                    return
                elif new_task.get_priority() == self.queue[i].get_priority():
                    if new_task.get_deadline() < self.queue[i].get_deadline():
                        self.queue.insert(i, new_task)  # Insert the task at the appropriate location in the queue.
                        return
            self.queue.append(new_task) 

    def show_tasks(self):
        """View all tasks in the queue."""
        if self.isEmpty():
            print("No tasks in the queue.")
        else:
            print ("All tasks in the queue:")
            for task in self:
                print(f'------------------------------\n{task}\n------------------------------')  # Use Task's __str__ method to display task details.

    def update_task(self, task_name, new_name, new_description, new_priority, new_deadline):
        """Update a task by its name.
        If the priority or deadline is updated, remove old task with new one so that the queue is ordered correctly
        If only the name or description is updated, just call the update_task method on the task"""
        if self.isEmpty():
            print("No tasks in the queue.")
        else:
            old_task = self.get_task(task_name)
            
            if old_task is None:
                print("Task not found.")
            else:
                if new_name.upper() == "SAME":
                    new_name = old_task.get_name()
                if new_description.upper() == "SAME":
                    new_description = old_task.get_description()
                if new_priority == 0:
                    new_priority = old_task.get_priority()
                if new_deadline.Upper() == "SAME":
                    new_deadline = old_task.get_deadline()

                if new_priority != None or new_deadline != None:  # If the priority or deadline is updated, remove old task with new one
                    self.remove_task(task_name)
                    updated_task = Task(new_name, new_description, new_priority, new_deadline)
                    self.add_task(updated_task)  # Add the updated task to the queue with the new priority and deadline)
                else:  # If only the name or description is updated, update the old task
                    self.get_task(task_name).update_task(new_name, new_description)

    def remove_task(self, task_name):
        """Remove a task from the queue."""
        if self.isEmpty():
            print("No tasks in the queue.")
        else:
            for task in self:
                if task.get_name() == task_name:
                    print(f"{task} \nTASK SUCCESSFULLY REMOVED!")
                    self.queue.remove(task)  # Remove the task from the queue if it is found

    def complete_task(self):
        """Remove the highest priority task from the queue and print out that it was completed."""
        if self.isEmpty():
            print("No tasks in the queue.")
        else:
            task = self.queue.pop(0)  # Remove the highest priority task from the list
            print(f"{task} \nTASK COMPLETED!")  # Print out that the task was completed