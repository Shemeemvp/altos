# 7. Given a two list of numbers, write a program to create a new list should contain odd numbers from the first list and even numbers from the second list.
l1=[2,34,5,2,45,3,1,55,64,23]
l2=[75,4,8,44,90,69,33,42,72]
l3=[]

for i in l1:
    if i % 2!=0:
        l3.append(i)
for i in l2:
    if i% 2==0:
        l3.append(i)
print(l3)