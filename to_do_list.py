def main_function():
    tasks = []  
    print("****To do list****")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Clear tasks")
    print("4. Exit")
    
    while True:
        user_input = input("Enter your choice: ")

        if user_input == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")
        elif user_input == "2":
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif user_input == "3":
            tasks.clear()
            print("All tasks cleared.")
        elif user_input == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_function()
