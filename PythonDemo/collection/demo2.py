_author_='yuan'
from collections import defaultdict

user_dict={}
users=['hobby1','hobby2','hobby3','hobby1','hobby2','hobby2']
for user in users:
    # if user not in user_dict:
    #     user_dict[user]=1
    # else:
    #     user_dict[user]+=1

    user_dict.setdefault(user,0)
    user_dict[user]+=1

print(user_dict)

# default_dict=defaultdict(int)
# students=['hobby1','hobby2','hobby3','hobby1','hobby2','hobby2']
# for student in students:
#     default_dict[student]+=1
# print(default_dict)

def gen_default():
    return {
        'name':'',
        'nums':0,
    }

default_dict={
    'group1':{
        'name':'',
        'nums':0,
    }
}
default_dict=defaultdict(gen_default)
default_dict['group1']
print(default_dict)