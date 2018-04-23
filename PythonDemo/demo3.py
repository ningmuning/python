class Programer:
    def __init__(self,name,age):
        self.name=name
        if isinstance(age,int):
            self.age=age
        else:
            raise Exception('age must be int')

    def __str__(self):
        return '%s is %s years old'%(self.name,self.age)

    def __dir__(self):
        return self.__dict__.keys()

if __name__=='__main__':
    p=Programer('Tom',20)
    print(p)
    print(dir(p))