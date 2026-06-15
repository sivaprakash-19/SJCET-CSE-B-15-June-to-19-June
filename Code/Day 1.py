def a() :
    print("Inside a")
def inner() :
    a() 
    print("Inside inner")
def outer() :
    inner() 
    print("Inside outer")
    a()
outer()
print("Inside main")
inner()

'''
# Number pattern
n = int(input("Enter n : "))
k = (2 * n) - 1
for i in range(k) : 
    for j in range(k) :
        top = i
        left = j
        right = k - 1 - j
        down = k - 1 - i
        x = min(top, left, down, right)
        print(n - x, end = " ")
    print()
'''

'''
# Number pattern
end = (2 * n) - 1
for i in range(n) :
    num = (2 * i) + 1
    for j in range(n) :
        print(num, end = " ")
        num += 2
        if num > end :
            num = 1
    print()
'''

'''
# Diamond pattern
# First half
for i in range(1, n + 1) :
    # Spaces -> n - i 
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i ) :
        print("*", end = " ")
    print() 
# Second half
for i in range(n - 1, 0, -1) :
    # Spaces -> n - i 
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i ) :
        print("*", end = " ")
    print()
'''

# for i in range(1, n) :
#     if i % 3 != 0 and i % 5 != 0 :
#         print(i, end = " ")

# if n % 3 == 0 and n % 5 == 0 :
#     print("Divisible by 3 and 5")
# elif n % 5 == 0 : 
#     print("Divisible by 5") 
# elif n % 3 == 0 :
#     print("Divisible by 3")
# else :
#     print("Not Divisible by 3 and 5")
# print(n, type(n))


# name = input("Enter name : ")
# dept = input("Enter dept : ")
# age = int(input("Enter age : "))
# print("Name : ", name, " Dept : ", dept, " Age : ", age)

# n = int(input("Enter n : "))
# print(n, type(n))

"""
n = 10
print(n, type(n))
n = 23.8
print(n, type(n))
"""