import smtplib
import os
import Text
import mail_data
from Dbase import User
from Interactive import chose_receiver


def chosen_user():
    necessary_name = chose_receiver()
    for user in User.get_all():
        if necessary_name in user:
            return user[2]


def send_mail():
    searching_results = Text.search_word()
    receiver = chosen_user()
    subj = 'Text processing'
    body = 'Found "{0}" {1} times.\n\n'.format(searching_results[2], searching_results[0])
    for line in searching_results[1].items():
        body += '{0}) {1}'.format(line[0], line[1]) + '\n'
    msg = 'From: {0}\nTo: {1}\nSubject: {2}\n\n{3}'.format(mail_data.from_addr, receiver, subj, body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_data.user_name, mail_data.pass_word)
    server.sendmail(mail_data.from_addr, receiver, msg)
    server.quit()

os.chdir('/home/andrew/Files')
send_mail()
