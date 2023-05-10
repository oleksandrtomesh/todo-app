from functions import get_todos, write_todos
from time import strftime

now = strftime('%b %d, %Y %H:%M:%S')

print(f'It is {now}')
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos( todos)
    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos()

        # new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row =f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            number = int(user_action[9:])
            todo_to_remove = todos[number - 1]
            todo_to_remove = todo_to_remove.strip("\n")
            todos.pop(number - 1)
            print(f"Task \"{todo_to_remove}\" has been completed and deleted from the list!")
            write_todos(todos)
        except IndexError:
            print('The length of list is ' + str(len(todos)))
            continue
    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            number = int(user_action[5:])
            number = number - 1
            new_todo = input('Add new todo: ')
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print('You provided wrong command. Should be number of item to edit')
            continue
    elif 'exit' in user_action:
        break
    else:
        print('Hey, you entered an unknown command')
print('Bye')