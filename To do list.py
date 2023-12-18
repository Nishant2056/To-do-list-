class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"{self.description} - {status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

# Example Usage
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)

        elif choice == "2":
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_as_completed(index - 1)

        elif choice == "3":
            todo_list.view_tasks()

        elif choice == "4":
            print("Exiting the to-do list manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")