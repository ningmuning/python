class Old:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class New(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Programer(object):
    hobby='Play computer'
    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight

    def get_weight(self):
        return self.__weight

    def get_hobby(cls):
        return cls.hobby

    def self_introduction(self):
        print('My name is %s\nI am %s years old.\n'%(self.name,self._age))

class BackProgramer(Programer):
    def __init__(self,name,age,weight,language):
        super(BackProgramer, self).__init__(name,age,weight)
        self.language=language

    def self_introduction(self):
        print('My name is %s\nMy favorite language is %s\n'%(self.name,self.language))

def introduce(programer):
    if isinstance(programer,Programer):
        programer.self_introduction()

if __name__=='__main__':
    # old=Old('old','Old class')
    # print(old)
    # print(type(old))
    # print(dir(old))
    # print(',,,,,,,,,,,,')
    # new=New('new','New class')
    # print(new)
    # print(type(new))
    # print(dir(new))

    programer=Programer('Albert',25,50)
    back_programer=BackProgramer('Tom',30,60,'Python')
    introduce(programer)
    introduce(back_programer)
    print(dir(programer))
    print(programer.get_hobby())
    print(programer.__dict__)
    print(type(programer))
    print(programer.get_weight())
    print(isinstance(programer,Programer))
    programer.self_introduction()
    print(programer._Programer__weight)