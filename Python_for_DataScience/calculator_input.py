from calculator import *
user_input=input("사칙연산 프로그램: ").split(" ")
first_val, second_val = int(user_input[0]),int(user_input[2])
fourcal=user_input[1]
if fourcal == "+":
    result = sum_func(first_val, second_val)
if fourcal == "-":
    result = minus_func(first_val, second_val)
if fourcal == "/":
    result = devide_func(first_val, second_val)
else:
    result = multiply_func(first_val, second_val)

print("실행결과는: ",result)
