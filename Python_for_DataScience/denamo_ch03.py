first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
"""
# 3번
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
print(john)
del john[2]
john.extend([order[2][0:1]])
print(john)
"""

"""
#4번
list_a = [3,2,1,4]
list_b = list_a.sort()
print(list_a, list_b)
"""
"""
#5
a=[5,7,3]
b=[3,9,1]
c=a+b
c=c.sort()
print(c)
"""

"""
#7
fruits=['apple','banana','cherry','grape','orange','strawberry','melon']
print(fruits[-3:],fruits[1::3])
"""

"""
#8
num=[1,2,3,4]
print(num*2)
"""
