import hashlib

from data_classes import UserDataClass


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
        
    def _make_str(self, user_data: UserDataClass, field_order: tuple) -> str:
        '''
        Make a String concatenated by all UserData values
        in a given order
        '''
        string = ''
        for field in field_order:
            string += getattr(user_data, field) + '*'

        return string
            
    def _encript(self, string) -> str:
        return hashlib.sha256(string.encode('utf-8')).hexdigest()


    def run(self) -> str:
        string = self._make_str(self.user_data, self.field_order)
        return self._encript(string)
