def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid selection!")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()