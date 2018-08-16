
# ===================
# 14_Iterators.py
# ===================

# ITERATOR

# functions ==> iter, next, range

# Iterator is an object that represents a stream of data
# It returns the data in the stream one object at a time
# Any object that supports iteration is called iterable.
# We have seen two iterable objects so far. Strings and lists

# We can use a for loop to iterate through all the characters in the string
# What's happening is that there is an iterator that is created from
# the string. And the for loop uses that iterator to return each item
# on the string. And when there are no more items, the iterator returns
# and error and the for loop terminates.
# Note that the for loop handles the error and that is why you don't
# see the error when you run the code.

string = "1234567890"
for char in string:
    print(char)

print("="*20)


# We can create an iterator from this same string to see how it works
# We will use the iterator function: iter()
# The results of this gives you <str_iterator object at 0x037C73F0>
# This is the object representation and memory allocation where it is.

string = "1234567890"
myIterator = iter(string)
print(myIterator)

print("="*20)

# To actually see the result, we use next() function
# next() goes through the string one element at a time.

string = "1234567890"
myIterator = iter(string)
print(myIterator)
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# print(next(myIterator)) # This gives error StopIteration because there is no more items in string

print("="*20)


# The for loop iterates through the string as shown and when the
# string ends and it encounters an error, it terminates the loop
# These two commands give same results. This is because the first
# one implicitly creates an iterator from string

string = "1234567890"
for char in string: # Iterator implicitly created by python
    print(char)

print()
for char in iter(string): # Iterator manually created
    print(char)

print("="*20)


# Iterator challenge
# Create a list of items (strings of numbers)
# Then create an iterator using iter() function

# Use a for loop to loop n times, where n is the number if items in the list
# Each time round the loop, use next() on your list to print the next item

# Hint: use len() function rather than count number of items in list

# Example of using iterators on numbers

string = "0123456789"
stringIterator = iter(string)
for char in range(len(string)):
        print(next(stringIterator))

print("="*20)
# Example of using iterators on lists of strings

string = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
stringIterator = iter(string)
for char in range(len(string)):
    print(next(stringIterator))

print("="*20)
# An easier way of running above command without iterators is

string = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i in string:
    print(i)

