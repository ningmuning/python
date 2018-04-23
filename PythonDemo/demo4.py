class Programer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __getattribute__(self, name):
        # return getattr(self,name)
        # return self.__dict__[name]
        return super(Programer, self).__getattribute__(name)

    def __setattr__(self, name, value):
        # setattr(self,name,value)
        self.__dict__[name]=value


if __name__=='__main__':
    p=Programer('Tom',20)
    print(p.__dict__)
    print(p.name)

