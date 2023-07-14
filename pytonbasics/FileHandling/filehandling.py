# 1. Create a text file intro.txt in python and ask the user to write a single line of text as user input.
# 2. Create a text file myfile.txt in python and ask the user to write separate 3 lines of text with 3 inputs statement form the user.
# 3. Write a program to read the contents of both the files created in the above programs and merge the contents into merge.txt

"""def program1():
    f = open('intro.txt','w')
    text = input("Enter the text..")
    f.write(text)
    f.close()

program1()"""

"""def program2():
    f = open('myfile.txt','w')
    text1 = input('Enter first line..')
    text2 = input('Enter second line..')
    text3 = input('Enter third line..')

    f.write(text1+'\n')
    f.write(text2+'\n')
    f.write(text3+'\n')
    # f.writelines([text1,text2,text3])
    f.close()

program2()"""


def program3():
    fileData1 = fileData2 = ""
    f = open("intro.txt", "r")
    fileData1 = f.read()
    f.close()
    f = open("myfile.txt", "r")
    fileData2 = f.read()
    f.close()

    f = open("merge.txt", "w")
    f.write(fileData1 + "\n" + fileData2)


program3()