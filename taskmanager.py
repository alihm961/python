class TaskNode:  #Node class representing a task in the task list
    def __init__(self, task):
        self.task = task  #Stores the task description
        self.next = None   #Pointer to the next task
        
class TaskManager:
    def __init__(self):
        self.head = None  #Head pointer "first task in the list"
        
    def add_task(self, task):
        new_task = TaskNode(task)  #Create a new task node
        
        if not self.head:
            self.head = new_task  #If the list is empty, the newe task becomes the head.
        else:   #Traverse to the end of the list and add the new task.
            current = self.head
            while current.next:
                current = current.next 
            current.next = new_task  #Linked the last task to the new task.
                
    def remove_task(self, task):
        
        if not self.head:
            print("Task list is empty! nothing to remove.")
            
        if self.head.task == task:
            self.head = self.head.next
            print(f"Task '{task}' removed successfully!")
            return
        
        current = self.head
        while current.next:
            if current.next.task == task:
                current.next = current.next.next 
                print(f"Task '{task}' removed successfully!")
                return
            
            current = current.next
            
        print(f"Task '{task}' is not found! ")
            
    def display_tasks(self):   #Display all tasks in the task list.
        if not self.head:
            print(f"No tasks available.")
            return
        
        print("Task List: ")
        current = self.head
        while current:
            print(f"-{current.task}")  #Print eavh task.
            current = current.next
            
task_manager = TaskManager()

while True:
    print("Task Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter the task: ")
        task_manager.add_task(task)  #Call add_task method
        print(f"Task '{task}' added successfully!")
        
    elif choice == "2":
        task = input("Enter the task to remove: ")
        task_manager.remove_task(task)  #Call remove_task method
        
    elif choice == "3":
        task_manager.display_tasks() #Call display_tasks method
        
    elif choice == "4":
        print("Exiting Task Manager. Have a nice day!")
        break
    else:
        print("Invalid option! Please try again.")
        