_author_='yuan'
from collections import Counter

users=['hobby1','hobby2','hobby3','hobby1','hobby2','hobby1','hobby3','hobby1']
user_counter=Counter(users)
user_counter2=Counter('hobby1')
# print(user_counter)
# print(user_counter2)

# user_counter3=Counter('gf')
# user_counter.update('sda')
# print(user_counter)
user_counter.update(user_counter2)
# 把user_counter2更新进去
user_counter.most_common(2)
print(user_counter)