#2
"""
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)
"""

#3
"""
num = ['12', '34', '56']
for i in num:
    i = int(i)
print(num)
"""

#4
"""
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])
"""

#5
'''
num = 0
i = 1
while i<8:
    if i%3 == 0:
        break
    i+=1
    num+=i
print(num)
'''
#6
'''
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)
'''
#7

#8
'''
first_value = 0
second_value = 0
for i in range(1,10):
    if i is 5:
        continue
        first_value = i
    if i is 10:
        break
        second_value = i
print(first_value+second_value)
'''

#9
'''
num = ""
for i in range(10):
    if i <= 5 and (i%2)==0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) +num
print(num)
'''

#10
'''
def work_status(task, worker, day):
    rest_task = task
    for k in range(day):
        if rest_task > 0:
            rest_task = rest_task-worker
        elif rest_task <= 0:
            print("Task end")
    if rest_task > 0:
        print("Hire more workers")
work_status(100,11,10)
work_status(100,1,10)
work_status(100,9,10)
work_status(100,10,10)
'''

#11
'''
score_list = [5,10,15,20,25]
sum_of_score=0
i=0
while i <len(score_list):
    if i%2 ==0:
        sum_of_score +=score_list[i]
    i +=1
print(sum_of_score)
'''

#12
'''
coupon = 0
money = 200000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon+=1
    else:
        money+=2800
        coupon=0
print(money)
'''
#13
a='369'
b='693'
strike = 0
ball = 0

for number in a:
    if b.count(number) >=1:
        if b.find(number) != a.find(number):
            ball +=1
        else:
            strike +=1
print("Strike: ",strike,"Ball: ",ball)


#14
'''
list_data_a=[1,2]
list_data_b=[3,4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j
print(result)
'''

#15
'''
list_1=[[1,2],[3],[4,5,6]]
a,b,c = list_1
list_2=a+b+c
print(list_2)
'''
































