import json

END_FLAGS = ['good bye', 'close', 'exit', '.']
OPERATIONS = ['add', 'change', 'phone', 'show all']
    
def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except ValueError:
            print('Give me name and phone please')
        except KeyError:
            print('User doesn`t exist')
        except IndexError:
            print('Enter user name')
        except UnboundLocalError:
            print('Try again')
    return inner


def command_parser(user_command: str):
    command_elements = user_command.split()
    if command_elements[0] in ['show'] :
        command_elements[0] = f'{command_elements[0]} {command_elements.pop(1)}'
    return command_elements


def end_process():
    with open('./contact_book.json', 'w') as file:
        json.dump(contact_book, file)
    
    return False


def greeting_func():
    print('How can I help you?')


@input_error
def add_contact(*args):
    name, phone = args
    contact_book[name] = phone
    result = f'Contact: {name} have been created with phone: {phone}!'
    return result

@input_error
def change_contact(*args):
    name, phone = args
    old_phone = contact_book[name] 
    contact_book[name] = phone
    result = f'Contact: {name} has been saved with phone: {phone}!'
    return result
    
@input_error   
def show_name_contact(*args):
    phone = args[0]
    for key, value in contact_book.items():
        if value == phone:
            name = key
    result = f'Contact name: {name}!'
    return name


@input_error
def show_all_contact():
    result = ''
    for key, value in contact_book.items():
        result += f'Name: {key:<12}| Phone: {value:^14}|\n' 
    return result
         

def main_controller(user_command: str):
    command_elements = command_parser(user_command)
    command, *args = command_elements
    if command == 'add':
        result = add_contact(*args)
        return result
    elif command == 'change':
        result = change_contact(*args)
        return result
    elif command == 'phone':
        result = show_name_contact(*args)
        return result
    elif command == 'show all':
        result = f'Full contact list:\n{show_all_contact()}'
        return result
        
def main():
    '''---------------------------
        add [contact] [phone] - add new contact.
        change [contact] [phone]- change existing contact.
        phone [contact] - show number.
        show all - show all stored contacts and their numbers.

        To terminate the program, enter one of the following commands:
        good bye
        close
        exit
        \n---------------------------'''
    process_status = True
    while process_status:
        user_command = input('\nWait for command!\nTry "help" for more options.\n____________________________\nInput #: ').lower()
        if user_command in END_FLAGS:
            print('Good bye!')
            process_status = end_process()
        elif user_command == 'help':
            help(main)
        elif user_command == 'hello':
            greeting_func()
        else:
            result = main_controller(user_command)
            result and print(result)


if __name__ == '__main__':
    with open('./contact_book.json', 'r') as file:
        contact_book = json.load(file)
    print(contact_book)
    main()