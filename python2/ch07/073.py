# import os
# currentdir = os.path.dirname(__file__) + '/'
# # print(curdir)

# ls = ['北京', '上海', '广州', '深圳', '武汉']
# f = open(currentdir + 'city.csv', 'w', encoding='utf-8')
# # f.write(','.join(ls))
# f.write(','.join(ls) + '\n')
# f.close()


import os
currentdir = os.path.dirname(__file__) + '/'
f = open(currentdir + 'city.csv', 'r', encoding='utf-8')
ls = f.read().strip('\n').split(',')
f.close()
print(ls)

