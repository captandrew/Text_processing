import sqlite3


class User:

    db_name = 'simpledb.db'

    def __init__(self, pk, name, mail):
        self.id = pk
        self.name = name
        self.mail = mail

    def __str__(self):
        return 'User: id - {0}, name - {1}, mail - {2}'.format(self.id, self.name, self.mail)

    @classmethod
    def get(cls, pk):
        with sqlite3.connect(cls.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM user WHERE id={}'.format(pk))
            pk, name, mail = cur.fetchone()
            return User(pk, name, mail)

    @classmethod
    def get_all(cls):
        with sqlite3.connect(cls.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM user')
            rows = cur.fetchall()
            return rows

    @classmethod
    def add_user(cls):
        with sqlite3.connect(cls.db_name) as conn:
            pk = input('Enter new user id:')
            name = input('Enter new user name:')
            mail = input('Enter new user mail:')
            cur = conn.cursor()
            cur.execute("INSERT INTO user VALUES({0}, '{1}', '{2}')".format(pk, name, mail))
            print('User added')

    @classmethod
    def remove_user(cls):
        with sqlite3.connect(cls.db_name) as conn:
            pk = input('Enter user id to delete:')
            cur = conn.cursor()
            cur.execute("DELETE FROM user WHERE id={0}".format(pk))
            print('User deleted')
