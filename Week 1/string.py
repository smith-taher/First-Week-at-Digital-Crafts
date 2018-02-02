uppercase = "hello world!"
print uppercase.upper()

cap = "hello world!"
print cap.capitalize()

rev = "hello world!"
print rev[:: - 1]

string = raw_input('Enter some text: ')
string = string.upper()
for char in string:
	if char == 'A':
		string = string.replace('A','4')
	elif char == 'B':
		string = string.replace('B','8')
	elif char == 'E':
		string = string.replace('E','3')
	elif char == 'L':
		string = string.replace('L','1')
	elif char == 'O':
		string = string.replace('O','0')
	elif char == 'S': 
		string = string.replace('S','5')
	elif char == 'T':
		string = string.replace('T','7')
	else:
		pass
print string


word = raw_input('Enter a word: ')
vowels = ['a', 'e', 'i', 'o', 'u']
for char in word:
    if char == 'aa':
        word = word.replace('aa','aaaaa')
    elif char == 'ee':
        word = word.replace('ee','eeeee')
    elif char == 'ii':
        word = word.replace('ii','iiiii')
    elif char == 'oo':
        word = word.replace('oo','ooooo')
    elif char == 'uu':
        word = word.replace('uu','uuuuu')
    else:
        pass
print word
