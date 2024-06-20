import constants, helpers

if __name__ == '__main__':
    print('Welcome to tasks app')
    constants.displayOptions()

    choice = input('Enter a choice  ')
    if choice == '1':
        tasks = helpers.listTasks()
    elif choice == '2':
        helpers.addTask()
    elif choice == '3':
        helpers.updateTask()
    elif choice == '4':
        helpers.deleteTask()
    else:
        print('please enter a valid choice')
        

