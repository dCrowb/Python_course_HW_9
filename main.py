
# def input_error(func):
#     def inner(*args):
#         pass
#     return inner


# def help_function():
#     '''---------------------------
#             add - add new contact.
#             change - change existing contact.
#             phone - show all numbers.
#             show all - show all stored contacts and their numbers.

#             To terminate the program, enter one of the following commands:
#             good bye
#             close
#             exit
#             \n---------------------------'''
    

# def main():
#     process_status = True
#     while True:
#         user_command = input('\nWait for command!\nTry "help" for more options.\n____________________________\nInput #: ')
#         result = main_controller(user_command)
#         print(result)


# def get_handler(command):
#     return OPERATIONS[command]


# def main_controller(user_command: str):
#     command_elements = command_parser(user_command)
#     command = command_elements[0]
#     handler = get_handler(command)




# def command_parser(user_command: str):
#     result = user_command.split(' ')
#     if result[0] in ['good', 'show']:
#         result[0] = f'{result[0]}_{result.pop(1)}'
#     return result 


# def end_process(user_command):
#     return False


# def hello_func():
#     answer = 'How can I help you?'
#     return answer
    

# END_FlAGS = ['good bye', 'close', 'exit']
# OPERATIONS = {'hello': hello_func,
#             'add': 'x',
#             'change': 'x',
#             'phone': 'x',
#             'show all': 'x',
#             'good bye': end_process,
#             'close': end_process,
#             'exit': end_process
#             }

# if __name__ == '__main__':
#     main()







def main():
    result = True
    while result:
       user_command = input('\nWait for command!\nTry "help" for more options.\n____________________________\nInput #: ').lower()
       result = main_controller(user_command)



def main_controller(user_command: str):
    command_elements = command_parser(user_command)
    command = command_elements[0]
    handler = get_handler(command)
    if isinstance(handler, bool):
        return False


def command_parser(user_command: str):
    result = user_command.split(' ')
    if result[0] in ['good', 'show']:
        result[0] = f'{result[0]}_{result.pop(1)}'
    return result 


def get_handler(command):
    return OPERATIONS[command]
    

def end_process():
    print('Good bye!')
    return False


END_FlAGS = ['good bye', 'close', 'exit']
OPERATIONS = {'hello': 'x',
            'add': 'x',
            'change': 'x',
            'phone': 'x',
            'show_all': 'x',
            'good_bye': end_process(),
            'close': end_process(),
            'exit': end_process()
            }

if __name__ == '__main__':
    main()
