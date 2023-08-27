def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def main():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added to your to-do list.")
        elif choice == '2':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed from your to-do list.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
