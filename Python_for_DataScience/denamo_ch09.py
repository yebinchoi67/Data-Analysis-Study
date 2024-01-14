from functools import reduce
#1
'''
def f(x,y):
    return x**y
fx = lambda x,y : x**y
print(f(2,4))
print(fx(2,4))
'''

#2
'''
ex = [1,2,3,4,5]
f = lambda x : x**2
print(list(map(f,ex)))
'''

#3
'''
list1 = [1,2,3,4,5]
print(reduce(lambda x,y:x*y , list1))
'''


#7?????

vector1 = [1,2]
vector2 = [3,4,]
vector3 = [1,7]
vector = [vector1,vector2,vector3]
print(all([len(vector[0]) == len(v) for v in vector]))


#8
'''
def scalar_vector_product(scalar,list_a):
    return [scalar*value for value in list_a]
print(scalar_vector_product(5,[1,2,3,4]))
'''

#9
'''
def matrix_addition(matrix_a, *matrix_b):
    return [[sum(row) for row in zip(*t)] for t in zip(matrix_a,*matrix_b)]

matrix_y = [[2,5],[2,1]]
matrix_x = [[2,4],[5,3]]
matrix_z = [[1,1],[11,1]]
print(matrix_addition(matrix_y,matrix_x,matrix_z))
'''

#10
'''
def vector_subtraction(vector_a,*vector_b):
   return [-sum(v) + 2*v[0] for v in zip(vector_a,*vector_b)]

print(vector_subtraction([1,3],[2,4]))
print(vector_subtraction([1,5],[10,4],[4,7]))
'''























