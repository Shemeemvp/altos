# 5. Write a program to iterate the first ten numbers and in each iteration print the sum of current and previous number

list1=[2,4,5,34,23,67,72,82,92,97,104,344,312]
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
    i+=1;