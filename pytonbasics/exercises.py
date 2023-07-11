# Python basics - Exercises

# 1. Count odd and even numbers in list datatype
# 2. To check a number is odd or even(user input)
# 3. To check a character is vowel or not(user input)
# 4. Calculate the multiplication and sum of the two numbers
# 5. Write a program to iterate the first ten numbers and in each iteration print the sum of current and previous number
# 6. Write a program to check whether the given number is palindrome or not.
# 7. Given a two list of numbers, write a program to create a new list should contain odd numbers from the first list and even numbers from the second list.


# 1. Count odd and even numbers in list datatype
'''l1 = [1, 3, 43, 54, 32, 52, 44, 5, 55, 63, 6]
oddCount = 0
evenCount = 0
for i in l1:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print('Number of Odd numbers in the list is :'+str(oddCount))
print('Number of even numbers in the list is :'+str(evenCount))'''

# 2. To check a number is odd or even(user input)
'''num = int(input('Enter a number'))
if num % 2 == 0:
    print(str(num)+' is an even number')
else:
    print(str(num)+' is an odd number')'''

# 3. To check a character is vowel or not(user input)
'''c = input('Enter a character')
if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or
        c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
    print(c+' is a vowel')
else:
    print(c + ' is a consonant')'''

# 4. Calculate the multiplication and sum of the two numbers
'''num1= int(input('Enter 2 numbers'))
num2=int(input())
print('Sum of the numbers :'+str(num1+num2))
print('Product of the numbers :'+str(num1*num2))'''

# 5. Write a program to iterate the first ten numbers and in each iteration print the sum of current and previous number

'''list1=[2,4,5,34,23,67,72,82,92,97,104,344,312]
prev=0
i=0
while(i<10):

    current = list1[int(i)]
    print('Iteration '+ str(i+1))
    print('Previous :'+str(prev))
    print('Current :'+str(current))
    print('Sum :'+str(prev+current)+'\n')

    prev = current
    # current = list1[i+1]
    i+=1;'''

# 6. Write a program to check whether the given number is palindrome or not.

'''num= int(input('Enter a number'))
temp = num;
rev=0;

while(temp>0):
    rem = temp%10
    rev= (rev*10)+rem
    temp = temp//10
if rev == num:
    print('Number is palindrome')
else:
    print('Number is not palindrome')'''

# 7. Given a two list of numbers, write a program to create a new list should contain odd numbers from the first list and even numbers from the second list.
'''l1=[2,34,5,2,45,3,1,55,64,23]
l2=[75,4,8,44,90,69,33,42,72]
l3=[]

for i in l1:
    if i % 2!=0:
        l3.append(i)
for i in l2:
    if i% 2==0:
        l3.append(i)
print(l3)'''

# Patterns Programs
#1
'''for i in range(0,4):
    for j in range(0,4):
        print('*',end=' ')
    print('\n')'''

#2
'''for i in range(4,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print('\n')'''

#3
'''rows = int(input('Enter number of rows'))
for i in range(0,rows):
    for j in range(0,i+1):
        print('*', end=' ')
    print('\n')

for i in range(rows,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print('\n')'''

#4
'''for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print('\n') '''

#5
'''k=1
for i in range(0,4):
    for j in range(0,i+1):
        print(k,end=' ')
        k+=1
    print('\n')'''

#6
'''asc=65
for i in range(0,4):
    for j in range(0,i+1):
        print(chr(asc),end=' ')
        asc+=1
    print('\n')'''

# User Input
# 1. Create a text file intro.txt in python and ask the user to write a single line of text as user input.
# 2. Create a text file myfile.txt in python and ask the user to write separate 3 lines of text with 3 inputs statement form the user.
# 3. Write a program to read the contents of both the files created in the above programs and merge the contents into merge.txt

'''def program1():
    f = open('intro.txt','w')
    text = input("Enter the text..")
    f.write(text)
    f.close()

program1()'''

'''def program2():
    f = open('myfile.txt','w')
    text1 = input('Enter first line..')
    text2 = input('Enter second line..')
    text3 = input('Enter third line..')

    f.write(text1+'\n')
    f.write(text2+'\n')
    f.write(text3+'\n')
    # f.writelines([text1,text2,text3])
    f.close()

program2()'''

def program3():
    fileData1 = fileData2 = ""
    f = open('intro.txt','r')
    fileData1 = f.read()
    f.close()
    f = open('myfile.txt','r')
    fileData2 = f.read()
    f.close()

    f = open('merge.txt','w')
    f.write(fileData1+'\n'+fileData2)

program3()