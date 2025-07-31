
todo_list= []

while (True):
    user_action=input("Enter a command (add,view,remove,exit): ")

    if( user_action=="add"):
        task=input("Enter the task:")
        todo_list.append (task)
        print("task added.")

    elif( user_action=="view"):
        if not todo_list:
            print("No tasks to display.")
        else: 
            for task in todo_list:
                print(task)

    elif ( user_action=="remove"):
        if not todo_list: 
            print("No tasks to remove.")
        else:
            task=input("Enter a task:")
            if task in todo_list:
                todo_list.remove(task)
                print ("task removed.")
            else:
                print("task not found")

    elif ( user_action=="exit"):
        break

    else:
        print("invalid command.")
            


