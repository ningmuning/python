class Programer:

    def __init__(self,name,age):
        self.name=name
        if isinstance(age,int):#判断参数类型
            self.age=age
        else:
            raise Exception('age must be int')
    def __eq__(self, other):
        if isinstance(other,Programer):
            if self.age==other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other,Programer):
            return self.age+other.age
        else:
            raise Exception('The type of object must be Programer')

if __name__=='__main__':
    p1=Programer('Tom',20)
    p2=Programer('Jack',30)
    #判断p1,p2不一样
    print(p1)
    print(p2)
    print(p1==p2)
    print(p1+p2)