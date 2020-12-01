import pickle

fileName = "file.dat"

dictionary = {}

class Processor:
    @staticmethod
    def readFile():
        try:
            file = open(fileName, "rb")
        except IOError as e:
            file = None

        if file is not None:
            global dictionary
            dictionary = pickle.load(file)
            file.close()
        return 'Success'

    @staticmethod
    def add(task, priority):
        dictionary[task] = priority
        return 'Success'

    @staticmethod
    def remove(task):
        del dictionary[task]
        return 'Success'

    @staticmethod
    def writeFile():
        file = open(fileName, "wb")
        pickle.dump(dictionary, file)
        file.close()
        return 'Success'

class IO:
    @staticmethod
    def print_menu_Tasks():
        print('''
            Menu of Options
            1) Add a new Task
            2) Remove an existing Task
            3) Save Data to File
            4) Reload Data from File
            5) Exit Program
            ''')
        print()

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_Tasks_in_list():
        print("******* The current Tasks ToDo are: *******")
        print(dictionary)
        print("*******************************************")
        print()

    @staticmethod
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task = input("Enter task: ")
        priority = input("Enter priority: ")
        Processor.add(task, priority)

    @staticmethod
    def input_task_to_remove():
        task = input("Enter task: ")
        Processor.remove(task)

Processor.readFile()

while (True):
    IO.print_current_Tasks_in_list()
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()

    if strChoice.strip() == '1':
        IO.input_new_task_and_priority()
        IO.input_press_to_continue()
        continue

    elif strChoice == '2':
        IO.input_task_to_remove()
        IO.input_press_to_continue()
        continue

    elif strChoice == '3':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.writeFile()
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("Save Cancelled!")
            continue

    elif strChoice == '4':
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.readFile()
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue

    elif strChoice == '5':
        print("Goodbye!")
        break