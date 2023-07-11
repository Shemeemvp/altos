#6
asc=65
for i in range(0,4):
    for j in range(0,i+1):
        print(chr(asc),end=' ')
        asc+=1
    print('\n')