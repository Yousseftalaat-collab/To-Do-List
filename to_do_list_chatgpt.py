class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print("✅ Task added.")

    def view(self):
        if not self.tasks:
            print("📭 No tasks.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            print(f"🗑️ Removed: {removed}")
        except IndexError:
            print("❌ Invalid task number.")


todo = TodoList()

while True:
    print("\n1. Add  2. View  3. Remove  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        todo.add(input("Enter task: "))
    elif choice == "2":
        todo.view()
    elif choice == "3":
        todo.view()
        todo.remove(int(input("Task number to remove: ")))
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice.")
