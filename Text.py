import os
import re
import Interactive


def check_file_exist(file_name_for_checking):
    if os.path.isfile('{0}/{1}.txt'.format(os.getcwd(), file_name_for_checking)):
        return 'file exists'


def search_word():
    dct = {}
    word_counter = 0
    splitter1 = re.compile(r'\W+')
    splitter2 = re.compile('[.!?\n]')
    while True:
        try:
            with open('{0}.txt'.format(Interactive.file_name_accept())) as opened_file:
                word = input('Enter a word for searching:')
                for sentence in splitter2.split(opened_file.read()):
                    for words in splitter1.split(sentence):
                        if word in words:
                            word_counter += 1
                            dct[word_counter] = sentence.strip()
            return word_counter, dct, word
        except FileNotFoundError:
            answer = Interactive.helper()
            if answer == 'yes':
                Interactive.showing_files()
            elif answer == 'no':
                pass
