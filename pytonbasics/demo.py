# print('Welcome')
# if(5>2):
#     print('5 is greater than 2')

#indentation
'''print('welcome')
if 5>2 :
    print('5>2')
    print('hello') '''

#variables
'''x=10
y='hello'
print(x)
print(y)
print('altos'+y)'''
#print('altos'+x)
 

#global var and local var

'''x='hello'
def dmo():
    print('welcome'+x)
dmo() 
print(x)'''

#x='hello'
'''def sam():
    x='welcome'
    print(x)
sam()    
print(x)'''

'''def sam():
    global x
    x='welcome'
    print(x)
sam()    
print(x)'''


#datatypes


#1. numeric

'''x=1 #int
y=2.5 #float
z=0+1j #complex

a=float(x)
print(a)
print(type(a))

b=int(y)
print(b)
print(type(b))

c=complex(x)
print(c)
print(type(c))'''


#2. string

'''x='hello'
print(x)'''
"""y='''hello,
welcome'''"""
'''print(y)
print(x[0])
print(x[1:3])
print(x[1:])
print(x[:3])
print(x[-1])
print(x[-3:-1])
print(len(x))'''

'''x='altos'
print('al' in x)'''

'''if('al' in x):
    print('true')'''
'''x='altos'
print('se' in x)'''
'''x='altos'
print('se'not in x)
if('se' in x):
    print('true')'''


#format method

'''age=2
name='Sam'
text='my name is {} and i am {}'
print(text.format(name,age))

age=2
name='Sam'
text='my name is {1} and i am {0} {1}'
print(text.format(age,name))'''

#3. List datatype

# a=[1,2,3,'a','b','c']
# print(a[3])
# print(a[-4:-1])

# a[2]=2
# print(a)

# for x in a:
#     print(x)

# for x in 'apple':
#     print(x)


# List items add, remove, delete list
# x=['apple','orange','grapes','pineapple']

# if 'apple' in x:
#     print('Yes its there..')

# x.append('banana')
# print(x)

# x.insert(1,'kiwi')
# print(x)

# x.remove('orange')
# print(x)
# x.pop()
# print(x)

# del x
# print(x)

# y=list(x)
# print(y)


# List copying
# list1=['a','b','c']
# list2=[1,2,3]

# for x in list2:
#     list1.append(x)
# print(list1)


# List constructor
# list=list((1,2,3,4))
# print(list)


# Conditional statements
# a=10
# b=15
# c=20
# if a>b:
#     print('a is greater than b')
# elif b>a:
#     print('b is greater than a')
# else:
#     print('a and b are equal')

# if a>b or c>a:
#     print('atleast any one is true')


# Loops

# while Loop
# i=1
# while i<5:
#     print(i)
#     i+=1

# break statement

# i=1
# while i<5:
#     print(i)
#     if i==3:
#         break;
#     i+=1

# continue statement
# i=1
# while i<5:
#     i+=1
#     if i==3:
#         continue;
#     print(i)

# for loop
# s='altos'
# for i in s:
#     print(i)

# fruits=['apple','banana','orange']
# for i in fruits:
#     print(i)
#     if i=='banana':
#         break

# for i in fruits:
#     if i=='banana':
#         continue
#     print(i)

# Range function
# for i in range(5):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# Nested for loop
# for i  in range(0,4):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print('\n')

# a=input('Enter input')


# 4. Tuple

# x=(1,2,3,4)
# print(x[1])
# y=list(x)
# y[1]=5 # type: ignore
# x= tuple(y)
# print(x)
# print(len(x))

# p = tuple((11,22,33,44))
# print(p)


# 5. Set
'''x={11,22,33,44}
y={'apple','orange','banana'}
print(y)
print('apple' not in y)
if 'apple' in y:
    print('item is there..')'''

'''fruits = {'apple','orange','grapes'}
fruits.add('banana')
print(fruits)
fruits.update(['kiwi','mango'])
print(fruits)
fruits.remove('mango')
x= fruits.pop()
print(x)
print(fruits)

y = set(('car','bike','bicycle'))
print(y)'''


#5. Dictionary

'''x = {'color':'red','year':2023}
# print(x)
y=x['color']
# print(y)
for i in x:
    print(x[i])

for i in x.values():
    print(i)

for i,j in x.items():
    print(i,j)

x['color'] = 'green'
print(x)

# x.popitem()
# print(x)

x['model']='xyz'
# print(x)

# x.pop('model')
# print(x)

# del x
# print(x)

y = dict(color='white',year = 2010)
print(y)'''


# Functions

'''def myFunction():
    print('This my function')

myFunction()

def myFunction2(fname,lname):
    print(fname+lname)

myFunction2('Muhamed', 'Shemeem')'''

'''def myFunction3(fname='shemeem'):
    print(fname)

myFunction3('Muhamed')
myFunction3()
myFunction3('appu')'''

'''def myFunction4(food):
    for x in food:
        print(x)
fruits = ['apple','orange','grapes']

myFunction4(fruits)'''

'''def myFunction5(x):
    return 5*x;
print(myFunction5(6))'''


# lambda Function

'''x = lambda a:a+10

print(x(20))'''

'''def myFunction6(y):
    return y*y*y;

print(myFunction6(3))

y = lambda a:a*a*a
print(y(3))'''

# Map and filter function 
'''fruits = ['apple','orange','grapes']
newList = list(map(lambda fruit:str.upper(fruit),fruits))
print(newList)

numbers = [1,2,3,4,5]
newNumberList = list(filter(lambda num : num > 3,numbers))
print(newNumberList)'''

# LIST COMPREHENSION
'''lis1 = []
for i in 'altos':
    lis1.append(i)
print(lis1)'''

'''lis2 = [letter for letter in 'altos']
print(lis2)

lis3 = list(map(lambda ch: ch, 'alotstechnologies'))
print(lis3)'''


# FILE HANDLING
'''f = open('demofile.txt','x')

f = open('demofile.txt','r')
print(f.read(3))
print(f.readline())'''

'''f = open('demofile.txt','a')
f.write('Hello, Welcome all...')
f.close()
f=open('demofile.txt','r')
print(f.read())'''

'''f = open('demofile.txt','w')
f.write('Welcome all..')
f.close()
f = open('demofile.txt','r')
print(f.read())'''

'''f = open('demofile1.txt','w')
f.write('Welcome all..')
f.close()
f = open('demofile.txt','r')
print(f.read())'''

# import os
# os.remove('demofile2.txt')
