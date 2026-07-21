
# s = adddata(5, 6)

# def adddata(x, y):
#     global z
#     z = x + y
#     return z

# s = adddata(5, 6)
# print(s)
# print(z)

def func(ls=[]):
    ls.append(1)
    return ls

a = func()
b = func()

print(a)
print(b)