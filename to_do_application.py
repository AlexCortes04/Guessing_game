import datetime
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
            task_name = input("Enter the task: ").strip()
            if task_name == "":
                print("You have to type something.")
            elif task_name in [v['task_name'] for v in self.tasks]:
                print("Task already exists")
            else:
                break

        while True:
            priority = input("Enter the priority (high, medium, low): ")
            if priority in ("high", "medium", "low"):
                break
            else:
                print("Type one of the three priority options")
        
        while True:
            deadline = input(f"Enter the deadline (YYYY-MM-DD): ")
            try:
                deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
                if deadline < datetime.datetime.now():
                    usr_inpt = input("You typed a past date or today, is that okay? (Y/N): ")
                    if usr_inpt.lower() != "y":
                        continue
                break
            except:
                print("Type the date in the correct format")

        self.tasks.append({'task_name': task_name, 'priority': priority, 'deadline': deadline})
        deadline = deadline.strftime("%Y-%m-%d")
        print(f"'{task_name}' with {priority} priority and deadline {deadline} has been added to the list.")

    def remove_task(self):
        if not self.tasks:
            print("Task list is empty!")
            return

        while True:
            usr_inpt = input(f"Enter the task to remove: ")
            if usr_inpt == "":
                print("You have to type something.")
            break

        task_list = [v['task_name'] for v in self.tasks]
        if usr_inpt in task_list:
            del self.tasks[task_list.index(usr_inpt)]
            print(f"'{usr_inpt}' has been removed from the list. Advanced")
        else:
            print(f"'{usr_inpt}' is not in the list")

    def view_task(self):
        if not self.tasks:
            print("Task list is empty!")
        else:
            print("To-Do list")

            for i, t in enumerate(self.tasks):
                values = list(t.values())
                values[2] = values[2].strftime("%Y-%m-%d")
                print(f"{i+1}.", " - ".join(values))

    def suggest_task(self):
        if not self.tasks:
            print("Task list is empty!")
            return
        
        current_time = datetime.datetime.now()
        if current_time.hour < 12:
            print("Good morning! ")
        elif current_time.hour < 18:
            print("Good afternoon! ")
        else:
            print("Good evening! ")
        print("Here are some tasks you might want to work on: ")

        min_deadline = min([v["deadline"] for v in self.tasks])
        suggest_tasks = [v for v in self.tasks if v["deadline"] == min_deadline]
        suggest_tasks = [{
            "task_name": v["task_name"], "priority": v["priority"],
            "deadline": v["deadline"].strftime("%Y-%m-%d")
            } for v in suggest_tasks]

        if len(suggest_tasks) == 1:
            print(" - ".join(suggest_tasks[0].values()))
            return
        
        tmp = [v for v in suggest_tasks if v["priority"] == "high"]
        if tmp:
            [print(" - ".join(v.values())) for v in tmp]
            return
        
        tmp = [v for v in suggest_tasks if v["priority"] == "medium"]
        if tmp:
            [print(" - ".join(v.values())) for v in tmp]
            return
        
        [print(" - ".join(v.values())) for v in suggest_tasks]

    def start(self):
        while True:
            print("\nAdvanced To do Application\n"
                  "1. Add Task\n"
                  "2. Remove Task\n"
                  "3. View Tasks\n"
                  "4. Suggest Tasks\n"
                  "5. Exit")
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

            print()
            match usr_inpt:
                case 1:
                    self.add_task()
                case 2:
                    self.remove_task()
                case 3:
                    self.view_task()
                case 4:
                    self.suggest_task()
                case 5:
                    print("Exiting the application. Goodbye!")
                    exit()


def main():
    app = ToDoApplication()
    app.start()


if __name__ == "__main__":
    main()
