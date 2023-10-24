
class DataBase:
    __instance = None # Ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, pwd, port):
        self.user = user
        self.pwd = pwd
        self.port = port

    def connect(self):
        print(f'Соединение м БД: {self.user=}, {self.pwd=}, {self.port}')

    def cloce(self):
        print('Соединение закрыто')

    def read(self):
        return 'Данные БД'

    def write(self, data):
        print(f'Записьв БД  {data}')


db = DataBase('root', '1234', '80')
db2 = DataBase('root2', '5678', '80')
print(id(db), id(db2))