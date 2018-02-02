#Exercise 1 
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
#print Elizabeth's phone number
print phonebook_dict['Elizabeth']
#add Kareem and her phone number to the dictionary
phonebook_dict['Kareem'] = '938-489-1234'
print phonebook_dict
#delect Alice and her phone number from the dictionary
del phonebook_dict['Alice']
print phonebook_dict
#change Bob's phone number
phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict
#print all names and numbers
for key, value in dict.items(phonebook_dict):
    print key, value

#Exercise 2 = Nested Dictionaries
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#1. Get email address from Ramit
print ramit['email']
#2. Get 1st of Ramit's interests
print ramit['interests'][0]
#3. Get email address from Jasmine
print ramit['friends'][0]['email']
#4. Get Jan's second interest
print ramit['friends'][1]['interests'][1]

#Exercise 3 - Letter Summary
letters = raw_input("Enter a sentence: ")
def char_frequency(letters):
    dict = {}
    for n in letters:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print char_frequency(letters)

#Exercise 4 - Word Summary
words = raw_input("Enter some words: ")
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print word_count(words)







