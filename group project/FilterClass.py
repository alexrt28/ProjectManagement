from datetime import datetime

class Filter:
    def __init__(self, tasks):
        self.tasks = tasks

    def filter_by_keyword(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.get_name().lower() or keyword.lower() in task.get_description().lower()]
        self.display_results(results, keyword)

    def filter_by_priority(self, priority):
        results = [task for task in self.tasks if task.get_priority() == priority]
        self.display_results(results, priority)

    def filter_by_deadline(self, deadline):
        try:
            deadline_date = datetime.strptime(deadline, "%m/%d/%Y")
            results = [task for task in self.tasks if task.get_deadline() == deadline_date.strftime("%m/%d/%Y")]
            self.display_results(results, deadline_date.strftime("%m/%d/%Y"))
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY.\n")

    def display_results(self, results, filter):
        if results:
            print(f'\nFiltered Tasks by {filter}:')
            for task in results:
                print("------------------------------")
                print(task)
            print("------------------------------\n")
        else:
            print("No tasks found matching the criteria.\n")
