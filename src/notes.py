
# Arrays and Strings
# Arrays store same types of data
# Elements can be fixed/dynamic
# Lists are build using Arrays
# Strongly typed languages like Swift are more strict
# Python is flexible

# arrays in Python are automatically dynamic/under the hood
#  C arrays are usually fixed

# Lookup O(1)
# Append O(n), amortized O(1) - allocate a new array if size is 
# too large/small
# insert/delete O(n)
# JavaScript directly allows array as dynamic only

# in-place
# manipulate the current list (e.g append, insert, reverse)
# positives: save memory
# cons: other references to list may not be aware of changes

# out-of-place:
# create a new manipulated list (e.g. slicing, sorted, reversed)
# positives: a new copy avoids side effects
# cons: additional memory
# in-place version of reversed is arrayName.reversed()

# if you are trying to achieve performance based program
# it makes sense to use in-place operations
# usually when you are building a program you don't need to worry
# about constraints

# Strings:
# very similar to a list of characters
# shares a lot of methods with lists (slicing, index, count, sorted)
# strings are immutable without making a copy

# 3 tests cases:
# Pivot Index
# [1, 3, 4, 5, 2, 1] = 4
# [1, 5, 3, 6, 3, 1] = -1
# [5, 5, 5, 5, 5, 5] = -1

# Immutable/Mutables
# RAM Computers use it all the time to store variables
# it stores it within RAM and when it is called, it retrieves it
# num2 = num will reference the same place in memory
# however, if you assign it to a different value, it will change it
# anytime you change the value, it will delete the old reference and create a new one
# this is immutable values/variables, they are easy to work with... integers, string
# this isn't true for everything
# arr = [1, 2, 3]
# arr2 = arr
# both reference same box, however, if you append something to it, it changes both
# mutable variables ... arrays, class instance, objects
# creating a new array every time is expensive in space
# you have to keep track of where you assign things
# a dictionary is ... mutable
# there's a difference between appending and assigning
# appending will change the original array, assigning will not
# there are no methods that modifies a string

# Arrays: (What they are in memory)
# Static Array -- we don't deal with these too much
# access -- print(arr[0])
# constant runtime to access items in array O(1)
# however, if you want to append it's O(n)
# 
# 
