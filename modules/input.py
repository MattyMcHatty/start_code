def select_an_option():
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option

def is_task_complete_input():
    description = input("Enter task description to search for: ")
    return description

def create_task_input():
    description = input("Enter description: ")
    time_taken = int(input("Enter time taken: "))
    return description, time_taken