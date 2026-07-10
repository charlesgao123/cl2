# myfile = open('myfile.txt', 'w')
# myfile.write('Hello text file\n')
# myfile.write('goodbye text file\n')
# myfile.close()

# myfile = open('myfile.txt')
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
# myfile.close()
# print('done')

# myfile = open('myfile.txt')
# print(myfile.readlines())
# myfile.close()

# open('myfile.txt').read()

# print(open('myfile.txt').read())

# for line in open('myfile.txt'):
#     print(line, end='')
# open('myfile.txt').close()
# print('done')


# import os
# currentdir = os.path.dirname(__file__) + '\\'
# print(currentdir)

# currentdir = "E:\\sourcecode\\cl2\\python\\ch07\\"
currentdir = "E:/sourcecode/cl2/python/ch07/"
# currentdir = ''
myfile = open(currentdir + 'myfile.txt')
for line in myfile:
    print(line, end='')
myfile.close()
print('done')
