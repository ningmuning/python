_author_='yuan'
from collections import ChainMap

user_dict1={'a':'hobby1','b':'hobby2'}
user_dict2={'b':'hobby3','d':'hobby4'}
# for key,value in user_dict1.items():
#     print(key,value)
#一般遍历

new_dict=ChainMap(user_dict1,user_dict2)
for key,value in new_dict.items():
    print(key,value)

#如果key值重复，只出现一次,但并不证明消失不见
print(new_dict['b'])
#hobby3不会出现

print(new_dict.maps)
new_dict.maps[0]['a']='yuan'
print(new_dict['a'])
#值变为yuan