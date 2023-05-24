import PySimpleGUI as sg

import functions

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
add_btn = sg.Button("Add")
# create a window instance
window = sg.Window('ToDo App',
                   layout=[[label], [input_box, add_btn]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
