import random
#1
'''
f = open("hello_python.txt",'a')
f.write('hello, python!')
f.close()
'''

#3
'''
def get_half_value(number):
    assert isinstance(number, int), 'input value must be integer.'
    result = number/2
    assert isinstance(result, int), 'output value must be transformed integer.'
    return result
print(get_half_value(50))
'''
#4
'''
def sum_data(list_data_a, list_data_b):
    for i in list_data_a:
        for j in list_data_b:
            result = i+j
    return result
a = [1,2]
b = [3,4]
print(sum_data(a,b))
'''
#5
'''
try:
    for i in range(1,7):
        result = 7//i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")
'''
#6
'''
sentence = list("Hello Gachon")
while (len(sentence)+1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break
'''
#7
'''
alist = ["a","1","c"]
blist = ["b","2","d"]
for a,b in enumerate(zip(alist,blist)):
    #7
    #print(b[a])
    #8
    print(a/int(b[0]))
'''
#11
'''
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다")
guess_number(answer)
'''
#12
'''
for i in range(3):
    try:
        print(i,3//i)
    except ZeroDivisionError:
        print("Not divided by 0")
'''
#13
'''
f = open("i_have_a_dream.txt","r")
contents = f.read()
print(contents)
f.close()
'''
with open("i_have_a_dream.txt","r") as f:
    contents = f.read()
    print(contents)
























