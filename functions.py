def get_todos(filepath='todos.txt'):
    """Read a textfile and return a todo list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write the todos items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines([todo + "\n" for todo in todos_arg])