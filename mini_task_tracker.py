
import json

FILENAME = "tasks.json"

def load_tasks():
    """Return saved tasks, or [] if the file is missing."""
    try:
        ...  # open FILENAME, return json.load(f)
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # return empty list if file not found

def save_tasks(tasks):
    ...  # open FILENAME with "w", json.dump(tasks, f)
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)
def get_task_number(tasks):
    """Return the list index for a valid task number, else None."""
    try:
        n = int(input("Task number: "))
    except ValueError:
        print("Please enter a number.")
        return None
    if 1 <= n <= len(tasks):
        return n - 1
    print("Invalid task number.")
    return None
def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(tasks):
    index = get_task_number(tasks)
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task completed.")

def delete_task(tasks):
    index = get_task_number(tasks)
    if index is not None:
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

main()