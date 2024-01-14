#2
'''
list_1 = [0,3,1,7,5,0,5,8,0,4]
def quiz_2(list_data):
    a = set(list_data)
    return (list(a)[1:5])
print(quiz_2(list_1))
'''
#4
'''
country_code={"America":1,"Korea":82,"China":86,"Japan":81}
print(country_code.values())
print(country_code)
print(country_code.keys())
print(85 in country_code.values())
print("Korea" in country_code.keys())
'''
#5
'''
a=0
midterm_set = set([1,5,7,4,3,2,1,1,2,3])
for i in midterm_set:
    a=a+i
print(a)
'''
#6
'''
def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data
    else:
        return "Flase"
list_data = ['a',1,'gachonn','2016.0']
element = float(2016)
result = delete_a_list_element(list_data,element)
print(result)
'''
#7
'''
def add_number(original_list):
    original_list += [1]
mylist = [1,2,3,4]
add_number(mylist)
print(mylist)
print(set(mylist))
'''
#8
'''
a = [3,"apple",2016,4]
b=a.pop(0)
c=a.pop(1)
print(b+c)
'''
#9
'''
def week_seven(sentence1):
    cells = set(sentence1.replace(' ','').lower())
    return cells
sentence_a = "The quick brown fox jumps over the lazy dog"
sentence_b = "I love you"
print(len(week_seven(sentence_a)-week_seven(sentence_b)))
print(week_seven(sentence_a))
print(week_seven(sentence_b))
'''
#10
'''
tuple_1=(1,2,3)
tuple_2=(4,5,6)
def quiz_1(data1,data2):
    result = []
    for i in (tuple_1+tuple_2):
        result.append(i)
    return (result)
quiz_1(tuple_1,tuple_2)
'''
#11
'''
dict_1={2:1,4:2,6:3,8:4,10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
    dict_2[dict_values[i]]=dict_keys[i]
print(dict_2)
print(dict_2[2])
'''
#12
'''
animal = ['cat','snake','monkey','ant','spider']
legs = [4,0,2,4,8]
animal_legs_dict = {}
for i in range(len(animal)):
    animal_legs_dict[legs[i]]=animal[i]
print(animal_legs_dict)
animal_legs_dict['ant']=6
print(animal_legs_dict)
'''
#13
'''
t=(1,2,3)
print(t+t)
print(t*2)
print(t,t)
'''

#14
'''
Mydict={'1':1,'2':2}
Copy = Mydict
Mydict['1'] = 5
result = Mydict['1']+Copy['1']
print(result)
'''

#15
'''
sentence = list("You Love Me?")
result = ''
for i in range(len(sentence)):
    if i %3 == 0:
        result += sentence.pop()
    else:
        result += sentence.pop(0)
print(result)
'''
#16
'''
number = [5,6,7,8,9,1,2,3,4]
result=[]
result.append(number.pop(0))
result.append(number.pop())
result.append(number.pop(1))
result.append(number.pop())
result.append(number.pop(0))
print(number)
print(result)
print(number[0]+result[-1])
'''
#17
'''
a = list(range(10))
print(a)
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3,a[-1])
print(a)
a.pop()
print(a)
'''
#18
'''
box = [1,'red',3,(),[],None]
print(len(box))
'''
#19
'''
data_1 = {'one':(1,2,3,4,5,6),'two':[1,2,3,4,5,6],'three':{'four':4,'five':5}}
for k in ['one','two','three']:
    try:
        print(data_1[k][:1])
    except TypeError:
        print("error")
for k in ['one','two','three']:
    try:
        data_1[k][-1] = "a"
        print(data_1[k][-1])
        print(data_1)
    except TypeError:
        print("error")
        '''
#20
'''
class_category = ["A","B","C","D"]
student_category = ["Sam","Sarah","Jane","Johe"]
class_student_cate = {}
for i in range(len(class_category)):
    class_student_cate[class_category[i]]=student_category[i]
print(class_student_cate)
 '''             
















































































































