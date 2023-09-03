# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
a = input('Enter your first number')
if a.isdigit():
    print('successful')
else:
    print('Your Number Isnt Correct')
    c1 = input('Please Enter Your First Number Again')
    c1 == a

b = input('Enter your second number')
if b.isdigit():
    print('successful')
else:
    print('Your Number Isnt Correct')
    input('Please Enter Your First Number Again')


print(int(a) + int(b))
print(int(a) * int(b))
print(int(a) / int(b))
print(int(a) - int(b))
print('به ترتیب بالا')
print('اولی جمع')
print('دومی ضرب')
print('سومی تقسیم')
print('چهارمی تفریق')

# print('Please choose alternatives'
#             'zarb.a1'
#             'taghsim.b1'
#             'jam.c1'
#             'tafrigh.d1')
# a1 = (int(a) * int(b))
# b1 = (int(a) / int(b))
# c1 = (int(a) + int(b))
# d1 = (int(a) - int(b))