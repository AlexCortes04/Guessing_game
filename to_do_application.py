import os, json


class ToDoApplication:
    def __init__(self):
        if os.path.isfile("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = list()

    def __del__(self):
        if self.tasks:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file)
        else:
            if os.path.isfile("tasks.json"):
                os.remove("tasks.json")

    def add_task(self):
        while True:
            usr_inpt = input("Enter the task: ")
            if usr_inpt == "":
                print("You have to type something.")
                continue
            break

        self.tasks.append(usr_inpt)
        print(f"'{usr_inpt}' has been added to the list.")

    def remove_task(self):
        if not self.tasks:
            print("Task list is empty!")
            return

        usr_inpt = input("Enter the task to remove: ")
        if usr_inpt in self.tasks:
            self.tasks.remove(usr_inpt)
            print(f"'{usr_inpt}' has been removed from the list.")
        elif usr_inpt == "":
            print("You have to type something.")
        else:
            print(f"'{usr_inpt}' is not in the list")


    def view_task(self):
        if not self.tasks:
            print("Task list is empty!")
        else:
            print("To-Do list")

            for i in range(len(self.tasks)):
                print(f"{i+1}.", self.tasks[i])


    def start(self):
        while True:
            print("\nTo do Application\n"
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
                    exit()


def main():
    app = ToDoApplication()
    app.start()


if __name__ == "__main__":
    main()