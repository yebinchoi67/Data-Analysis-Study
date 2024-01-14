#1
'''
def test(t):
    t=20
    print("In Function:",t)
x=10
print("Before:",x)
test(x)
print("After:",x)
'''

#2
'''
def sotring_function(list_value):
    return list_value.sort()
print(sotring_function([5,4,3,2,1]))
'''

#3
'''
number="100"
def midterm(number):
    result=""
    if number.isdigit() is True:
        if number is 100:
            if number/10 ==1:
                result = True
    else:
        result = False
    return result
print(midterm(number))
'''

#4
'''
def is_yes(your_answer):
    if your_answer.upper() == "YES" or your_answer.upper()== "Y":
        result = your_answer.lower()
    
print(is_yes("Yes"))
'''

#5
'''
def add_and_mul(a,b,c):
    return b+a*c+b
print(add_and_mul(3,4,5) == 63)
'''

#6
'''
def args_test_3(one,two,*args,three):
    print(one+two+sum(args))
    print(args)
args_test_3(3,4,5,6,7)
'''

#7
'''
def rain(colors):
    colors.append("purple")
    colors = ["green","blue"]
    return colors
rainbow = ["red","orange"]
print(rain(rainbow))
'''

#8
'''
def function(value):
    print(value**3)
print(function(2))
'''

#9

def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit
fruit = "appl"
get_apple(fruit)
print(fruit)


#10
'''
def return_sentence(sentence,n):
    sentence += str(n)
    n -=1
    if n<0:
        return sentence
    else:
        return(return_sentence(sentence,n))
sentence = "I Love You"
print(return_sentence(sentence,5))
'''

#11
'''
def test(x,y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)
x = ["y"]
y = ["x"]
test(x,y)
print(y)
'''

#12
'''
def countdown(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")
        countdown(n-1)
countdown(3)
'''
#13
'''
def factorial_calculator(n):
    if n in (0,1):
        return 1
    else:
        return n*factorial_calculator(n-1)
print(factorial_calculator(5))
'''

#14
'''
def claculrate_rectangle_area(rectangle_x,rectangle_y):
    rectangle_x = 3
    rectangle_y=5
    result = rectangle_x*rectangle_y
    return result
rectangle_x = 2
rectangle_y = 4
'''

#15
'''
def exam_func():
    x=10
    print("Value :",x)
x=20
exam_func()
print("Value :",x)
'''

#16

country=["Korea","Japan","China"]
country.append("Remove")
print(country.remove("Remove"))








































































