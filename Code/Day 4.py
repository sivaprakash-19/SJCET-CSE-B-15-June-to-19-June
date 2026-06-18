
# ---- 2D MATRIX ----

# Getting input for a matrix with different number of cols in different rows 
matrix = []
rows = int(input("Enter rows : "))
for i in range(rows) :
    print("Enter elements at ", i, " row : ", end = " ")
    nums = list(map(int, input().split()))
    matrix.append(nums)

'''
# Getting input for a matrix with same number of cols for all rows
matrix = []
rows = int(input("Enter rows : "))
cols = int(input("Enter cols : "))
for i in range(rows) :
    nums = []
    for j in range(cols) :
        print("Enter element at ", i, j, " : ", end = " ")
        num = int(input())
        nums.append(num)
    matrix.append(nums)
'''
# Iterating through matrix using elements
for row in matrix :
    for i in row :
        print(i, end = " ")
    print() 

# Iterating through matrix using index
'''
for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        print(matrix[i][j], end = " ")
    print()
'''

# matrix = [
#     [1, 2, 3], 
#     [10, 20]
# ] 
# print(matrix[0], type(matrix[0]))

# ---- 2D MATRIX ----











'''
def callStack(n) :
    if n == 0 :
        return
    print(n, end = " ")
    callStack(n - 1)

def fact(n) :
    if n == 1 :
        return n
    return n * fact(n - 1)

def fibb(n) :
    if n == 0 or n == 1 :
        return n 
    return fibb(n - 1) + fibb(n - 2)

def firstOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1 
    print("i is : ", i)
    if nums[i] == element :
        return i
    return firstOccurrence(nums, element, i + 1)

def lastOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1 
    if nums[i] != element :
        return lastOccurrence(nums, element, i + 1)
    else :
        ans = lastOccurrence(nums, element, i + 1)
        if ans == -1 :
            return i
        else :
            return ans
        
def tower(n, source, helper, destination) :
    if n == 1 :
       print(source , destination)
       return  
    tower(n - 1, source, destination, helper)
    print(source , destination)
    tower(n - 1, helper, source, destination)
'''


# n = 3
# tower(n, 'S', 'H', 'D')
# nums = [10, 30, 40, 30]
# print(lastOccurrence(nums, 30, 0))
# print(firstOccurrence(nums, 30, 0))
# n = 40
# print(fibb(n))
# print(fact(n))
# callStack(n)