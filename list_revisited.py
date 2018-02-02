#Sum  -  working
# def sum(numbers):
#     total = numbers[0]
#     for number in numbers[1:]:
#         total += number
#     return total
# print sum(['apple', 'milk', 'bread'])
# print sum([2, 5, 8])

#Largest Number - working
# def highestNumber(l):
#     myMax = l[0]
#     for num in l:
#         if myMax < num:
#             myMax = num
#     return myMax
# print highestNumber([77,48,19,17,93,90])
# print highestNumber([102,48,19,17,101,90])

#Smallest Number - working
# def smallestNumber(l):
#     myMin = l[0]
#     for num in l:
#         if myMin > num:
#             myMin = num
#     return myMin
# print smallestNumber([77,48,19,17,93,90])
# print smallestNumber([102,48,19,2,101,90])

#Even Numbers - working
# def evenNumber(l):
#     evenNumber = []
#     for num in l:
#         if num % 2 == 0:
#             evenNumber.append(num)    
#     return evenNumber
# print evenNumber([1, 2, 3, 4, 5, 6, 7, 7])
# print evenNumber([10, 12, 11, 13, 15, 28])

#Positive Numbers - working
# def positives(l):
#     myPos = []
#     for num in l:
#         if num > 0:
#             myPos.append(num)
#     return myPos  
# print positives([-1, 2, 5, -8])

#Positive Numbers 2 -  working
# numbers = [4, -7, -10, 5]
# positives = []
# for number in numbers:
#     if number > 0:    
#         positives.append(number)
# print positives

#Multiply a List - working
# def multiply(i,factor):
#     multiplied = []
#     for num in i:
#         value = num * factor
#         multiplied.append(value)
#     return multiplied
# print multiply([1, 5, 10, 15], 3)


#Multiply a Function - working
def multiply(a, b):
    multiplied = []
    for i in range(len(a)):
        multiplied.append(a[i] * b[i])
    return multiplied
vector1 = [4, -7, -10, 5]
vector2 = [2, 3, -3, 5]
print multiply(vector1, vector2)

