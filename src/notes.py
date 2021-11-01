
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
