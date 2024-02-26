# command line interface
todos = []

while True:
    user_action = input('Type add, show, clear or exit: ')

    match user_action:
        case 'add':
            todo = input('enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
            # print(todos)
        case 'clear':
            todos = []
            print('todos cleared')
        case 'exit':
            break
        case _:
            print('Unknown command. Please try again')
print('Bye!')