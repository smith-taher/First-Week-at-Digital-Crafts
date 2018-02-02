#Sum
numbers = [4, 7, 10, 5]
sum = 0
for number in numbers:
    sum = sum + number # or us sum += number
print sum

#Largest Number
numbers = [4, 7, 10, 5]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print largest

#Smallest Number
numbers = [4, 7, 10, 5]
smallest = numbers[0]
for number in numbers:
    if number > smallest:
        smallest = number
print smallest

#Even Numbers
numbers = [4, 7, 10, 5]
for number in numbers:
    if number % 2 == 0:    
print number

#Positive Numbers
numbers = [4, -7, -10, 5]
positives = []
for number in numbers:
    if number > 0:    
        positives.append(number)
print positives

#Multiply List
numbers = [4, -7, -10, 5]
factor = 3
multiplied = []
for number in numbers:
    multiplied.append(numbers * factor)
print multiplied

#Multiply Vectors
vector1 = [4, -7, -10, 5]
vector2 = [2, 3, -3, 5]
multiplied = []
for i in range(len(vector1)):
    multiplied.append(vector1[i] * vector2[i])
print multiplied

#Matrix Addition
matrix1 = [
    [2, -2]
    [5, 3]
]
matrix2 = [
    [5, 2]
    [1, 0]
]
height = len(matrix1)
width = len(matrix1[0])
result = []
for i in range(0, height):
    result.append([])
        for j in range(0, width):
            result[1].append(None)
for i in range(0, height)
    result.append([])
    for j in range(0, width)
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]
        cell = cell1 + cell2

        result[i].append(cell)
print result

#Matrix addition2 - same as before
matrix1 = [
    [2, -2]
    [5, 3]
]
matrix2 = [
    [5, 2]
    [1, 0]
]
height = len(matrix1)
width = len(matrix1[0])
result = []

for i in range(0, height)
    result.append([])
    for j in range(0, width)
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]
        cell = cell1 + cell2

        result[i].append(cell)
print result

#De-dup
things = ['apple', 'cheese', 'milk', 'cheese', 'bread', 'cheese']
dedubed = []
for thing in things:
    if thing not in dedubed:
        dedubed.append(things)
print deduped