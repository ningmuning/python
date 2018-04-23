_author_='yuan'
from collections import OrderedDict

# 有序
user_dict=OrderedDict()

# user_dict=dict()
# 无序

user_dict['b']='hobby1'
user_dict['a']='hobby2'
user_dict['c']='hobby3'

print(user_dict)
print(user_dict.popitem())

#直接使用pop错误,必须传入一个key值
# print(user_dict.pop('c'))

user_dict.move_to_end('b')
# 将key值为b的value移到最后，则它后面没有值

print(user_dict)