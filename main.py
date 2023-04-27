
def input_error(func):
    def inner(*args):
        pass
    return inner


def help_function():
    '''---------------------------
            add - add new contact.
            change - change existing contact.
            phone - show all numbers.
            show all - show all stored contacts and their numbers.

            To terminate the program, enter one of the following commands:
            good bye
            close
            exit
            \n---------------------------'''
    

def main():
    process_status = True
    while True:
        user_command = input('\nWait for command!\nTry "help" for more options.\n____________________________\nInput #: ')
        main_controller(user_command)
            
def main_controller(user_command: str):
    print('main')



def check_command(user_command: str):
    if user_command.lower() == 'hi':
        print('Hello! How can I help you?')


def end_process(user_command):
    return False

END_FlAGS = ['good bye', 'close', 'exit']
OPERATIONS = {'add': 'x',
            'change': 'x',
            'phone': 'x',
            'show all': 'x',
            'good bye': end_process,
            'close': end_process,
            'exit': end_process
            }

if __name__ == '__main__':
    main()
