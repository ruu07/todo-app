import functions
import PySimpleGUI as sg #use 4.60.1
#to do = input_box, todos = list_box
import time

# if todos.txt is not created, create it:
import os
if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('Black') # LightBlue7

clock = sg.Text('', key='clock')

label = sg.Text("Type in a todo item")
input_box = sg.InputText(tooltip='Enter a todo item', key='input_box')
add_button = sg.Button(size=2, image_source='/Users/janelle/Desktop/0 Udemy App/app1/add.png',
                       mouseover_colors='LightBlue2',
                       tooltip='Add todo', key="Add")
# add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                      key='list_box',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',20)
                   )
while True:
    event,values = window.read(timeout=6000) #runs until here until an action is done
    # need timeout in order for clock to display
    # timeout means that it will run every 10ms, compared to empty = only when an event happens
    window['clock'].update(value=time.strftime('%d %b  %Y %H:%M'))
    print(1, event)
    print(2, values)
    print(3, values['list_box'])
    match event:
        case "Add": # Button label
            todos = functions.get_todos() #reads to  do file
            new_todo = values['input_box'] + "\n" # make sure to add new line
            todos.append(new_todo) # so that when append will be in next line
            functions.write_todos(todos) #writes to to do file
            window['list_box'].update(values=todos)
            window['input_box'].update(value='')
        case "Edit": # Button label
            try:
                todos = functions.get_todos()
                todo_to_edit = values['list_box'][0]
                # get index of to do to edit
                index = todos.index(todo_to_edit)
                # update the todos text file
                new_todo = values['input_box']
                todos[index] = todos
                todos[index] = new_todo
                functions.write_todos(todos)
                # to show the changes in the list box
                window['list_box'].update(values=todos)
                window['input_box'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica',20))

        case "Complete":
            try:
                 todo_to_complete = values['list_box'][0]
                 todos = functions.get_todos()
                 todos.remove(todo_to_complete)
                 functions.write_todos(todos)
                 window['list_box'].update(values=todos)
                 window['input_box'].update(value ='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica',20))

        case "Exit":
            break
        case 'list_box':
            window['input_box'].update(value=values['list_box'][0])
        case sg.WIN_CLOSED: #when window closed
            break # break to break out of for loop
            #if use exit(), will exit whole program without close()

window.close()