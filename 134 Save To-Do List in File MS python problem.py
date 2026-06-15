def save_todo_list(filename, tasks):
    with open(filename, 'w') as file:
        file.write("My To-Do List:\n")
        for i, task in enumerate(tasks, 1):
            file.write(f"{i}. {task}\n")
# Usage:
# tasks = ["Buy groceries", "Pay bills", "Walk the dog"]
# save_todo_list('todo.txt', tasks)
tasks = ["python problem solving", "business intelligence with power bi", "excell practicing", "working on the physical growth"]
save_todo_list('python problem to do.txt', tasks)
