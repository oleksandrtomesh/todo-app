FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a file and return the list of
    to-do items
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    :param filepath:
    :param todos_arg:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

