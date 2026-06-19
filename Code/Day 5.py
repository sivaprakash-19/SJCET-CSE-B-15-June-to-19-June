# ---- STRINGS ----

s = 'Good morning Have a nice day.'

print(s.replace('day', "days")) # Returns a string, after replacing the sub string with new string. T.C -> O(n)

# print(s.upper()) # Returns a string with uppercase letters. T.C -> O(n)

# print(s.lower()) # Returns a string with lowercase letters. T.C -> O(n)

# print(s.strip()) # Returns a string with trailing spaces removed on both sides. T.C -> O(n)

# print(s.rstrip()) # Returns a string with trailing spaces removed on right side. T.C -> O(n)

# print(s.lstrip()) # Returns a string with trailing spaces removed on left side. T.C -> O(n)

# words = s.split('!') # Returns a list of strings, separated on white space by default. T.C -> O(n)
# print(words, type(words))



print(s)

# print(s[::-1]) # Reverse the string. 

# print(s.isalnum()) # Returns a bool, if string is having only alphabets and numbers. T.C -> O(n)

# print(s.isalpha()) # Returns a bool, if string is having only alphabets. T.C -> O(n)

# print(s.index('Goe')) # Returns the first occurrence of the substring, if not present -> Throws ValueError. T.C -> O(n)

# print(s.count('o')) # Return the number of occurrences of substring. T.C -> O(n)

# Checks if given substring is present or not. T.C -> O(n)
# if 'He' in s[2 : ] :
#     print("Present")
# else :
#     print("Not present")

# Iterating through string, using elements
'''
for c in s :
    print(c)
'''

# Iterating through string, using index
'''
for i in range(len(s)) :
    print(i, s[i])
'''

# print(s[4 : ]) # Returns the substring from start to the end of string -> start -> inclusive

# print(s[ : 5]) # Returns the substring. end -> exclusive

# print(s[0 : 5]) # Returns the substring -> start -> inclusive, end -> exclusive

# print(s[1]) # Return the element at a specific index in string, if index is not valid -> Throws IndexError

# print(len(s))   # Return the length of string

# print(s, type(s))
# s1 = 'abcd' 
# print(s1, type(s1))
# print(s == s1)

# ---- STRINGS ----