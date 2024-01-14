#1
'''
a = 1
b=9
print('a'+'b')
'''

#2
'''
fact = "Python is funny"
print(str(fact.count('n')+fact.find('n')+fact.rfind('n')))
'''

#3
'''
text = 'Gachon CS50 - programming with python'
text2 = "Human cs50 knowledge belongs to the world"
text.lower()
print(text[:5]+text[-1]+text[6]+text2.split()[0])
'''

#4
'''
class_name = 'introduction programming with python'
for i in class_name:
    if i =='python':
        i = i.upper()
print(class_name)
'''

#5
'''
a = '10'
b = '5-2'.split('-')[1]
print(a*3+b)
'''

#6
'''
name = "Hanbit"
a = name.find("H")
b = name.count("H")*4
c=len(name)*2+4
print("REMEMBER",str(a)+str(b)+str(c))
'''

#7
'''
a = "abcd e f g"
b=a.split()
c = (a[:3][0])
d = (b[:3][0][0])
print(c+d)
'''

#8
'''
number = 10
day=3
print("I eat %d oranges every day." %number)
number=10
day="three"
print("I eat %d oranges every %s days"%(number,day))
'''
#9
'''
result = "CODE2018"
print("{0},{1}".format(result[-1], result[-2]))
'''

#10
'''
str_a="this is"
str_b="Python"
print(str_a.title()+ " "+str_b.upper())
'''

#12
print("%6s"%('*'))
print("%7s"%('*'*3))
print("%8s"%('*'*5))
print("%9s"%('*'*7))
print("%10s"%('*'*9))
print("%10s"%('*'*11))
