import os


def file_name_accept():
    file_name = input('Enter file name:')
    return file_name


def helper():
    while True:
        help_question = input('Show all ".txt" files?(y/n):')
        if help_question in ('y', 'yes', 'Y', 'Yes'):
            return 'yes'
        elif help_question in ('n', 'no', 'N', 'No'):
            return 'no'
        else:
            pass


def showing_files():
    t = os.walk(top=os.getcwd(), topdown=True)
    print('------------------------------')
    for tpl in t:
        for file in tpl[2]:
            if file.endswith('.txt'):
                print(tpl[0], '-----', file)
    print('------------------------------')
    while True:
        parameters_question = input('Type "1" to change folder,\ntype "2" to enter file name:')
        if parameters_question == '1':
            chosen_folder = input('Enter the path:')
            try:
                os.chdir(chosen_folder)
                break
            except FileNotFoundError:
                print('Wrong path! Just copy the path from the list.')
        elif parameters_question == '2':
            break
        else:
            pass


def chose_receiver():
    chose_question = input('Enter user name to share search results:')
    return chose_question
