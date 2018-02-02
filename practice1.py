# temperature = 65

# if temperature < 50:
   # print 'brr'
# else:
   # print 'not cold'

# print 'im done'


#array or list
#seats_assignments = [
   # "Moses",
   # "Ken",
   # "Terry",
   # "David",
   # "Nick",
   # "Itzik",
   # "Haehee",
   # "Illia"
#] 

#print seats_assignments[3] 
#will print David because starts counting at 0

#seats_assignments.append('Janelle')
#adds names to the list

#seats_assignments.remove('Illia')
#removes name from list

#seats_assignments.pop(0)
#removes name from list by index number


yesterday_seats_assignments = [
    "Moses",
    "Ken",
    "Terry",
    "David",
    "Nick",
    "Itzik",
    "Haehee",
    "Illia"
] 

today_seat_assignments = [
    "Nick",
    "Ashley",
    "Ken",
    "Joel",
    "Aaron",
    "Jaehee",
    "Moses",
    "Chris",
]

#if today_seat_assignments[0] == yesterday_seats_assignments[0]:
    #print "Hey, %s can't sit here!" % today_seat_assignments

# while loop
#current_seat_were_on = 0 #commonly use i for index value
#seat_count = len(today_seat_assignments)
# check if the current seat we're examining is the same
#while current_seat_were_on < seat_count:
    #print today_seat_assignments[current_seat_were_on]
    #curret_seat_were_on = current_seat_were_on + 1

#print "We're done!"

#i = 0
#seat_count = = lean(today_seat_assignments)
#while i < seat_count:
    #if today_seat_assignments[i] == yesterday_seats_assignments[i]
       # print today_seat_assignments[current_seat_were_on]
   # i += 1

#when you use for loop don't need i
#indices = [0,1,2,3,4,5,6,7]
#indices = range(0, len(today_seat_assignments) #up to not including 8
#for current_seat in today_seat_assignments:
   # if today_seat_assignments[i] == yesterday_seats_assignments[i]
   # print current_seat

for i in range(0, len(today_seat_assignments)):
    if today_seat_assignments[i] == yesterday_seats_assignments[i]:
        print "Hey, %s can't sit here!" % today_seat_assignments
    else:
        print "You're fine to seat here."

#Lists can change in size - called Mutable
#names = ['Jonathan', 'Martin']
#names.append('Lee')

#Immutable = lists that cannot be changed
# (x,y) for example is Toobowl

#dictionary or associated array
#Red => Nick
#Green => Ashley

seats_assignments = {
    "red": "Nick",
    "green": "Ashley"
}
seats_assignments('red')

#Functions - create a reuseable chunk of code
#Sum
def sum(numbers):
    total = numbers[0]
    for number in numbers[1:]:
        total += number
    return total
print sum(['apple', 'milk', 'bread'])
print sum([2, 5, 8])

#Multiply Vectors
vector1 = [4, -7, -10, 5]
vector2 = [2, 3, -3, 5]

def multiply(a, b)
multiplied = []
for i in range(len(a)):
    multiplied.append(a[i] * b[i])
return multiplied

vector1 = [4, -7, -10, 5]
vector2 = [2, 3, -3, 5]
print multiply(vector1, vector2)

Publishing code
Github
Git - VCS (version control system)
- also called repository
   V1 (pompom) - version 
   use ls -la to find hidden files
   .git is a folder
   create package

git add functions.py list_functions_solutions.py seating.py solutions.py
git commit -m 'Version 1 of my Python solutions'

git add - staged or prepares wrapping
git commit -m - puts bow on it

git status - tells us if anything has changed from previous version
git dif - tells us what has changed in the files
git add list_solutions.py tells git that you have made changes
git commit - updates the repository for now version 2
    -m in the commit allows you to add 'notes/memo'
git log shows all previous commits
git checkout - use code of version want to restore current version to
git checkout master - will bring you back to most recent commit

