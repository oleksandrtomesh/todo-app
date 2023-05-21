import PySimpleGUI as sg

import functions

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_btn = sg.Button("Add")
# create a window instance
window = sg.Window('ToDo App', layout=[[label], [input_box, add_btn]])

window.read()
window.close()
