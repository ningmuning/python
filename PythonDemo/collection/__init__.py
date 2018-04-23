__author__='yuan'

name_list=('hobby1','hobby2')
user_tuple=('Tom',19,175,'sing')
user_tuple2=('Tom',19,175)
# 拆包
name,age,height=user_tuple2
print(name,age,height)
name_tuple=('list',[1,2])
name_tuple[1].append(3)
print(name_tuple)
name,*other=user_tuple
# *other接收其他参数组成列表
print(name,other)
for name in name_list:
    print(name)