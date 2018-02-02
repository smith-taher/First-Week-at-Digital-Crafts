n = int(raw_input("Enter a number to start from between 1 to 10: "))
m = int(raw_input("Enter a number end on from 1 to 10: "))
if n > m:
    print "The number to end on must be greater than the starting number!"

for i in range(n, m + 1):
    print(i)