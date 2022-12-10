class User():

    def __init__(self, user, password):
        self._user = user  #protected
        self.__password = password #private

class Person():

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    @property
    def name(self):
        '''get name'''
        return self.__name

    @name.setter
    def name(self, name):
        print('set name')
        self.__name = name

    @name.deleter
    def name(self):
        print('delete name')
        del self.__name


if __name__ == '__main__':
    user = User('xime', '1234')
    print(user._user)
    print(user._User__password)
    person = Person('Xime', 'Luna')
    print(person.name)
    person.name = 'Ximena'
    print(person.name)
    del person.name


