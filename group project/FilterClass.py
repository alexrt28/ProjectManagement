from datetime import datetime

class Filter:
    def __init__(self, tasks):
        self.tasks = tasks

    def filter_by_keyword(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.get_name().lower() or keyword.lower() in task.get_description().lower()]
        self.display_results(results)

    def filter_by_priority(self, priority):
        results = [task for task in self.tasks if task.get_priority() == priority]
        self.display_results(results)

    def filter_by_deadline(self, deadline):
        try:
            deadline_date = datetime.strptime(deadline, "%m/%d/%Y")
            results = [task for task in self.tasks if task.get_deadline() == deadline_date.strftime("%m/%d/%Y")]
            self.display_results(results)
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY.")

    def display_results(self, results):
        if results:
            print("\nFiltered Tasks:")
            for task in results:
                print(task)
                print("----------")
        else:
            print("No tasks found matching the criteria.")
