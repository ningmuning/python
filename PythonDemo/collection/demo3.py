_author_='yuan'
from collections import deque

user_list=['hobby1','hobby2']
# user_hobby=user_list.pop()
# print(user_hobby,user_list)

# user_list=deque(['hobby1','hobby2'])
# named_tuple=('hobby1','hobby2')
# user_list.append(named_tuple)
# user_list.appendleft('hobby3')
# print(user_list)
import copy
#copy分深层次的和浅层次的
user_list2=copy.deepcopy(user_list)
user_list3=user_list.copy()
print(user_list3)
print(user_list,user_list2)
print(id(user_list),id(user_list2),id(user_list3))
print(user_list)