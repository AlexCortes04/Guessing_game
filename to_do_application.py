from datetime import datetime

class ToDoApplication:
    def __init__(self):
        self.tasks = dict()

    def __del__(self):
        pass

    def add_task(self):
        while True:
            usr_inpt = input("Enter the task: ")
            if usr_inpt == "":
                print("You have to type something.")
                continue
            priority = input("Enter the priority (high, medium, low): ")
            if priority == "":
                print("You have to type something.")
            elif priority not in ("high", "medium", "low"):
                print("Type one of the three priority options")
                continue
            deadline = input(f"Enter the deadline (YYYY-MM-DD): ")
            if deadline == "":
                print("You have to type something.")
                continue
            break
        print(f"'{usr_inpt}' with {priority} priority and deadline {deadline} has been added to the list.")
        self.tasks[usr_inpt] = [priority, deadline]

    def remove_task(self):
        if not self.tasks:
            print("Task list is empty!")
            return

        usr_inpt = input("Enter the task to remove: ")
        if usr_inpt in self.tasks:
            self.tasks.remove(usr_inpt) #User had to type the task name with priotity and date
            print(f"'{usr_inpt}' has been removed from the list. Advanced")
        elif usr_inpt == "":
            print("You have to type something.")
        else:
            print(f"'{usr_inpt}' is not in the list")


    def view_task(self):
        if not self.tasks:
            print("Task list is empty!")
        else:
            print("To-Do list")

            for k, v in self.tasks:
                print(f"{k+1}.", self.tasks[k])


    def start(self):
        while True:
            print("\n Advanced To do Application\n"
                  "1. Add Task\n"
                  "2. Remove Task\n"
                  "3. View Tasks\n"
                  "4. Exit")
            while True:
                usr_inpt = input("Enter your choice: ")
                if not usr_inpt.isdecimal():
                    print("Choose one of the options in the menu")
                    continue

                usr_inpt = int(usr_inpt)
                if not 1 <= usr_inpt <= 4:
                    print("Enter a number from 1 to 4")
                    continue
                break

            match usr_inpt:
                case 1:
                    self.add_task()
                case 2:
                    self.remove_task()
                case 3:
                    self.view_task()
                case 4:
                    print("Goodbye!")
                    exit()

ToDoApplication().start()