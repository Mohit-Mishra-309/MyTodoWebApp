def get_todos(filename ='todos.txt'):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filename = 'todos.txt'):
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_list)
