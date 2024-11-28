from datetime import datetime
from TaskClass import Task
from PriorityQueue import TaskPriorityQueue


def main():
    task_name, task_description, task_date = "","",""  # Holds the string information the user input
    date_list = []  # Used to separate the date that the user put in
    task_priority = 0  # Holds the priority of the task
    choice = 0  # int variable to hold user's menu choice
    year, month, day = 0, 0, 0  # int variables to hold the year, month, and day of the task's deadline

    # Create a new TaskPriorityQueue object
    task_queue = TaskPriorityQueue()

    # Choice Selection Menu
    while choice != 7:
        choice = 0
        print("Select an option from below:")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. Complete a Task")
        print("5. View all Tasks")
        print("6. Filter a Task")
        print("7. Exit Program")
        # Tries to input user's choice, if any error, print error message and loops back to get user's input again
        try:
            choice = int(input("Enter choice number here: "))
            if choice < 1 or choice > 7:
                print("\n*********************************************************************")
                print("ERROR: Choice must be an integer between 1 and 7. Please try again")
                print("*********************************************************************\n")
        except ValueError:
            print("\n*********************************************************************")
            print("ERROR: Choice must be an integer between 1 and 7. Please try again")
            print("*********************************************************************\n")

        # Call Function for each Selection
        if choice == 1:
            # Call AddTask function
            print("\nAdding a Task")
            AddTask(task_queue)

        elif choice == 2:
            # Call UpdateTask function
            print("\nUpdating a Task")
            UpdateTask(task_queue)

        elif choice == 3:
            # Call DeleteTask function
            DeleteTask(task_queue)

        elif choice == 4:
            # Call CompleteTask function
            print("")
            CompleteTask(task_queue)
            
        elif choice == 5:
            # Prints all of the tasks in the queue
            task_queue.show_tasks()

        elif choice == 6:
            # Calll Filtering Function
            FilterTasks(task_queue)


def AddTask(task_queue):
    task_name = input("Enter the name of the task: ")
    task_description = input("Enter the description of the task: ")

    task_priority = int(input("Enter the priority of the task (1/2/3/4 = Extreme/High/Medium/Low Priority): "))

    while task_priority < 1 or task_priority > 4:
        print("\n*********************************************************************")
        print("ERROR: Priority must be an integer between 1 and 4. Please try again")
        print("*********************************************************************\n")
        task_priority = int(input("Enter the priority of the task (1/2/3/4 = Extreme/High/Medium/Low Priority): "))

    # This section gets the deadline of the task from the user and converts it to a datetime object
    task_date = input("Enter the deadline of the task (MM/DD/YYYY): ")
    # Creates the new task object to be added to the Prioirty Queue
    new_task = Task(task_name, task_description, task_priority, task_date)
    task_queue.add_task(new_task)
    


def UpdateTask(task_queue):
    task_name = input("Enter the name of the task to be updated: ")

    if task_queue.isEmpty():
        print("No tasks in the queue.")
    elif task_queue.get_task(task_name) is None:
        print("Task not found.")
    else:   
        print("Below you will be input fields to update each of the task's information, type \"SAME\" (0 for priority) if you do not want to update that information.")
        update_name = input("Enter the updated name of the task: ")
        update_description = input("Enter the upated description of the task: ")

        update_priority = int(input("Enter the updated priority of the task (1/2/3/4 = Extreme/High/Medium/Low Priority, 0 for no change) : "))
        while update_priority < 0 or update_priority > 4:
            print("\n*********************************************************************")
            print("ERROR: Updated Priority must be an integer between 0 and 4. Please try again")
            print("*********************************************************************\n")
            task_priority = int(input("Enter the priority of the task (1/2/3/4 = Extreme/High/Medium/Low Priority, 0 for no change): "))

        update_deadline = input("Enter the updated deadline of the task (MM/DD/YYYY): ")

        task_queue.update_task(task_name,update_name, update_description, update_priority, update_deadline)
    
def DeleteTask(task_queue):
    task_name = input("Enter the name of the task to be deleted: ")
    task_queue.remove_task(task_name)

def CompleteTask(task_queue):
    task_queue.complete_task()


def FilterTasks(task_queue):
    if task_queue.isEmpty():
        print("No tasks in the queue.")
        return
    
    task_filter = TaskFilter(task_queue.queue)
    print("\nFilter Options:")
    print("1. Filter by Keyword")
    print("2. Filter by Priority")
    print("3. Filter by Deadline")

    try:
        filter_choice = int(input("Enter filter option number: "))
        if filter_choice == 1:
            keyword = input("Enter keyword to search: ")
            task_filter.filter_by_keyword(keyword)
        elif filter_choice == 2:
            priority = int(input("Enter priority level (1/2/3/4 = Extreme/High/Medium/Low): "))
            task_filter.filter_by_priority(priority)
        elif filter_choice == 3:
            deadline = input("Enter deadline (MM/DD/YYYY): ")
            task_filter.filter_by_deadline(deadline)
        else:
            print("Invalid option. Returning to main menu.")
    except ValueError:
        print("Invalid input. Returning to main menu.")


if __name__ == "__main__":
    main()
