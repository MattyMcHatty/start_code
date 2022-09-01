

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    # uncompleted_tasks = []
    # for task in list:
    #     if task['completed'] == False:
    #         uncompleted_tasks.append(task)
    # return uncompleted_tasks
    uncompleted_list = get_tasks_by_status(list, False)
    return uncompleted_list

## Get a list of completed tasks
def get_completed_tasks(list):
    # completed_tasks = []
    # for task in list:
    #     if task['completed'] == True:
    #         completed_tasks.append(task)
    # return completed_tasks
    completed_list = get_tasks_by_status(list, True)
    return completed_list


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_taken = []
    for task in list:
        if task['time_taken'] >= time:
            time_taken.append(task)
    return time_taken

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task['description'] == description:
            return task
    return None

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    completed_tasks = []
    uncompleted_tasks = []
    for task in list:
        if task['completed'] == True:
            completed_tasks.append(task)
        elif task['completed'] == False:
            uncompleted_tasks.append(task)
    if status == True:
        return completed_tasks
    elif status == False:
        return uncompleted_tasks

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

