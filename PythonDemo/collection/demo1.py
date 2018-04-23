__author__='yuan'
from collections import namedtuple
User=namedtuple('User',['name','age','height','edu'])
# user=User('Tom',28,175)
user_tuple=('Tom',28,175)
user_list=['Tom',28,175]
user_dict={
    'name':'Jack',
    'age':19,
    'height':175,
    'edu':'master',
}
user=User(*user_tuple,edu='master')
# print(user)
# name,age,*other=user
# print(name,age,other)
user_info_dict=user._asdict()
user=User._make(user_dict)
print(user_info_dict)

# 获得user_dict的key值
print(user.name,user.age,user.height)

