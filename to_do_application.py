class ToDoApplication:
    def __init__(self):
        self.tasks = list()

    def __del__(self):
        pass

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
        pass

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
