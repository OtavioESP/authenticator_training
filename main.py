# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

import datetime
import hashlib
from dataclasses import dataclass


def format_ip(ip: int) -> str:
    str_ip = str(ip)
    if len(str_ip) == 12:
        return f'{str_ip[:3]}.{str_ip[3:6]}.{str_ip[6:9]}.{str_ip[9:12]}'
    else:
        raise Exception

time_stamp: str = str(datetime.date.today())
username: str = 'otavio'
password: str = 'teste123'
machine_ip: str = format_ip(293855348332)

concat_str = time_stamp + '*' + username + '*' + password + '*' + machine_ip

returnal = hashlib.sha256(concat_str.encode('utf-8')).hexdigest()


@dataclass
class UserDataClass:
    time_stamp: str
    username: str
    password: str
    machine_ip: str


# for field in UserData.__dataclass_fields__:
# print(UserData.__dataclass_fields__)
# if UserData.__dataclass_fields__ in teste.__iter__():
#     print('ola')


test3 = UserDataClass(  
        time_stamp=time_stamp,
        username=username,
        password=password,
        machine_ip=machine_ip
    )
    
tupla = ('time_stamp', 'username', 'password', 'machine_ip')
        

us3r_data = {
    'time_stamp': time_stamp,
    'username': username,
    'password': password,
    'machine_ip': machine_ip
}



class Encription:
    def __init__(self, user_data: dict, fields: tuple):
        self.user_data = self.__validate_data(user_data)
        self.field_order = fields

    def __validate_data(self, user_data) -> UserDataClass:
        try:
            user = UserDataClass(
                time_stamp=user_data.get('time_stamp'),
                username=user_data.get('username'),
                password=user_data.get('password'),
                machine_ip=user_data.get('machine_ip')
            )
            for field in UserDataClass.__dataclass_fields__:
                if getattr(user, field) == None:
                    raise Exception
                else:
                    return user
        except:
            print('Erro de validação nos campos')
            
    # def 
        
        
        
    def _make_str(self, user_data: UserDataClass, field_order: tuple) -> str:
        '''
        Make a String concatenated by all UserData values
        in a given order
        '''
        string = ''
        for field in field_order:
            string += getattr(user_data, field)

        return string
            
    def _encript(self, string) -> str:
        return hashlib.sha256(concat_str.encode('utf-8')).hexdigest()


    def run(self) -> str:
        string = self._make_str(self.user_data, self.field_order)


# tupla = ('time_stamp', 'username', 'password', 'machine_ip')

def make_str() -> str:
    '''
    Make a String concatenated by all UserData values
    in a given order
    '''
    user = UserDataClass(
        time_stamp=us3r_data.get('time_stamp'),
        username=us3r_data.get('username'),
        password=us3r_data.get('password'),
        machine_ip=us3r_data.get('machine_ip')
    )
    string = ''
    breakpoint()
    for i in tupla:
        string += getattr(user, i)
        
    return string

a = make_str()
print(a)