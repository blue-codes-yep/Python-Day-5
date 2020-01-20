# Dictionary Exercises - 1

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # Print's Elizabeth's number
# print(phonebook_dict['Elizabeth'])

# # Add's Kareem to the dictionary
# phonebook_dict['Kareem'] = '938-489-1234'



# # Deleting Alice's number
# del phonebook_dict ['Alice']

# # Change to Bob's number
# phonebook_dict['Bob'] = '968-345-2345'

# print(phonebook_dict)

# -- 

# Exercise 2: Nested Dictionaries

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# This one was EZ PZ

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])

# --

# Letter Summary -- 

# Asks for user inputs, and then prints a dictonary how many times 
# each letter was used.

# user_input = input("Enter a sentence for a histogram: ")

# empty_dic = {}
# for x in user_input:
#     if x in empty_dic:
#         empty_dic[x] += 1
#     else:
#         empty_dic[x] = 1

# print(empty_dic)

# -- 


# user_input = input("Enter a sentence for a histogram: ")

# # .split splits a string into a list where each word becomes a list item.
# # In this case it takes the user's input and splits the sentence into a list.

# a_list = user_input.split()
# empty_dic = {}

# for x in a_list:
#     if x in empty_dic:
#         empty_dic[x] += 1
#     else:
#         empty_dic[x] = 1

# print(empty_dic)


