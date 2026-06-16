
# ----- DICTIONARY ----- 

nums = {
    100 : 4, 
    20 : 5, 
    50 : 8
}

if 10 in nums :
    print(nums[10])
else :
    print('Not present')

# print(nums[500])    # Prints value for a key, if key is not present -> Throws KeyError. T.C -> O(1)



# nums[50] = 70   # Adds the element into dict, if element is present -> Update value. T.C -> O(1)

print(nums, type(nums))


# ----- DICTIONARY -----

# ----- SET ----- 

# nums = {10, 50, 47, 89, 100}

# nums.discard(809) # Removes element in set, if element not present -> Ignore. T.C -> O(1)

# nums.remove(809) # Removes element in set, if element not present -> Throws KeyError. T.C -> O(1)

# Checks if element is present in Set. T.C -> O(1)
# if 50 in nums :
#     print("Present")
# else :
#     print("Not present")
# nums.add(10) # If element is not present -> Adds the element into set. Else -> ignore. T.C -> O(1)
# print(nums, type(nums))

# ----- SET ----- 



# print(5 | 4)


# Reverse an integer
'''
num = int(input("Enter number : "))
reversed = 0 
while num > 0 :
    digit = num % 10 
    reversed = (reversed * 10) + digit
    num //= 10
print(reversed)
'''

# Find sum of digits 
'''
num = int(input("Enter number : "))
sum = 0
while num > 0 :
    digit = num % 10 
    sum += digit 
    num //= 10
print(sum)
'''

'''
# Find the second largest in a list 
nums = [2]
largest = nums[0] 
secondLargest = 0
for i in nums :
    if i > largest :
        secondLargest  = largest
        largest = i 
    elif i > secondLargest and i != largest :
        secondLargest = i 
print(secondLargest)
'''

# nums.reverse() # Reverse the list. 

# nums.sort() # Sorts the list. T.C -> O(n logn)

# print(nums.pop()) # Removes the last element and returns it, if list is empty -> Throws IndexError. T.C -> O(1)

# print(nums)

# print(nums.index(100)) # Returns the first occurrence of element, if element not present -> Throws ValueError. T.C -> O(n)

# print(nums.count(100)) # Returns the number of occurrences of element. Returns int. T.C -> O(n)

# nums = input().split()

# print(nums, type(nums))
# print(type(nums[0]))

# nums = list(map(int, input("Enter elements : ").split("ab")))
# print(nums)

"""
input() -> gets input as String
input().split() -> converts into a list of strings, sep -> " "
map(int, input().split()) -> Iterate through each element and converts into a INT 
list(...) -> Converts into a list -> Returns a list

"""

# n = int(input("Enter no of elements : "))
# for i in range(n) :
#     print("Enter element at ", i, " : ", end = "")
#     num = int(input())
#     nums.append(num)


# print(nums[-1]) # -1 -> last element

# nums.insert(100, 90)  # Inserts element at index, if index is not valid -> Insert at last. T.C -> O(n)

# nums.append(40) # Appends element to the last. T.C -> O

# For each -> Accessing elements in list via index
# for i in range(len(nums)) :
#     print(i, " : ", nums[i])

# For each -> Accessing elements in list
# for i in nums :
#     print(i, end = " ")
