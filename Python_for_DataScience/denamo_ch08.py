#1
'''
mylist = ['apple','banana','grape']
result = list(enumerate(mylist))
print(result)
'''
#2
'''
cat_song = 'my cat has blue eyes, my cat is cute'
print({i:j for j,i in enumerate(cat_song.split())})
'''
#3
'''
colors = ['orange','pink','brown','black','white']
result = '&'.join(colors)
print(result)
'''
#4
'''
user_dict = {}
user_list = ["student",'superuser','professor','employee']
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)
'''
#6
'''
animal = ['Fox','Dog','Cat','Monkey','Horse','Panda','Owl']
print([ani for ani in animal if 'o' not in ani])
'''
#7
'''
name = "Hanbit University"
student = ['Hong','Gil','Dong']
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:]+split_name[1])
'''

#8
'''
kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score,math_score,eng_score]
print(midterm_score[0][2])
'''

#10
'''
week = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week,rainbow]
print(list_data[1][2])
'''

#11
'''
kor_score = [30,79,20,100,80]
math_score = [43,59,0,30,90]
eng_score = [49,72,48,67,15]
midterm_score = [kor_score,math_score,eng_score]
print("score:",midterm_score[2][1])
'''

#12
'''
alist = ['a','b','c']
blist = ['1','2','3']
abcd = []
for a,b in enumerate(zip(alist,blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
print(abcd)
'''

#14
'''
alphabet = ['a','b','c','d','e','f','g','h']
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2 ==0]
print(len(answer))
'''

#15
url = "cs50.gachon.ac.kr"
university_name = "Gachon University"
gachon_info = [(i+" "+j) for i,j in zip(university_name.split(" "),url.split("."))]
blank = 0
print(gachon_info[blank])















