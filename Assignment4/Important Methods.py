#Q.1- Reverse the whole list using list methods.
list1 = ['hello','yellow','how','are','you']
print("list = ['hello','yellow','how','are','you']\n")
print('Reversing the string using string methods')

list1.reverse()
print(list1)

print('\n__________________')


#Q.2- Print all the uppercase letters from a string.
s="AaBbCc"
print('Old string :\t %s' % (s))

print(''.join(i for i in s if i.isupper()))
        


print('\n__________________')


#Q3 Split the user input on comma's and store the values in a list as integers.
s=input('Enter some city using commas\t')

# Separate on comma.
cities = s.split(",")

# Loop and print each city name.
for city in cities:
    print(city)
    
print('\nputting the separated values in string\n')
print(list(cities))


#___________________________________________
print('_____________________________________')

#Q.4- Check whether a string is palindromic or not.

str=input('enter a string to check for palindrome\t')
if(str == ''.join(reversed(str))):
    print('the string is a palindrome')
else:
    print('the string is not a palindrome')


f='hello'
print(reversed(f))


print('_____________________________________')
#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

import copy
a=['a','b','c','d']
b=copy.deepcopy(a)
print('Original List :\t', a)
print('Deepcopy Lsit :\t', b)

print('\nIf the Original object contains any reference to mutable object then the\nduplicate reference variables nwill be created pointing to a contained \nobject but no duplicate object gets created is called shallow copying')


