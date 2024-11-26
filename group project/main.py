from datetime import datetime
from TaskClass import Task


def main():
    task_name, task_description, task_date = "","",""  # Holds the string information the user input
    date_list = []  # Used to separate the date that the user put in
    task_priority = 0  # Holds the priority of the task
    choice = 0  # int variable to hold user's menu choice
    year, month, day = 0, 0, 0  # int variables to hold the year, month, and day of the task's deadline

    # Choice Selection Menu
    while choice != 6:
        print("Select an option from below:")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. Complete a Task")
        print("5. View all Tasks")
        print("6. Exit Program")
        # Tries to input user's choice, if any error, print error message and loops back to get user's input again
        try:
            choice = int(input("Enter choice number here: "))
            if choice < 1 or choice > 6:
                print("\n*********************************************************************")
                print("ERROR: Choice must be an integer between 1 and 6. Please try again")
                print("*********************************************************************\n")
        except ValueError:
            print("\n*********************************************************************")
            print("ERROR: Choice must be an integer between 1 and 6. Please try again")
            print("*********************************************************************\n")

        # Call Function for each Selection
        if choice == 1:
            # Call AddTask function
            AddTask(task_queue)


        elif choice == 2:
            # Call UpdateTask function
            print("\n")
            AddTask()


        elif choice == 3:
            # Call DeleteTask function
            print("\n")
        elif choice == 4:
            # Call CompleteTask function
            print("\n")
        elif choice == 5:
            # Call ViewTasks function
            print("\n")
            print(new_task) # Temporary print statement to test if printing the task works



def AddTask(task_queue):
    task_name = input("Enter the name of the task: ")
    task_description = input("Enter the description of the task: ")
    task_priority = int(input("Enter the priority of the task: "))

    # This section gets the deadline of the task from the user and converts it to a datetime object
    task_date = input("Enter the deadline of the task (MM/DD/YYYY): ")
    # Creates the new task object to be added to the Prioirty Queue
    new_task = Task(task_name, task_description, task_priority, task_date)
    


def UpdateTask(task_queue):
    task_name = input("Enter the name of the task to be updated: ")
    
    print("Below you will be input fields to update each of the task's information, leave a field blank to not make any changes.")
    update_name = input("Enter the updated name of the task: ")
    update_description = input("Enter the upated description of the task: ")
    update_priority = input("Enter the updated priority of the task: ")
    update_deadline = input("Enter the updated deadline of the task (MM/DD/YYYY): ")

    task_queue.update_tasks(update_name, update_description, update_priority, update_deadline)





if __name__ == "__main__":
    main()