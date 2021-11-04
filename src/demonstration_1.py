"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Understand:
- input: is an array of integers
- output: the index (a number)
- compares and sums numbers, there is a left and right side
- smallest number is -1/largest is n - 1

Plan:
- array search problem
- loop through or map through it
- check if current value is pivot by checking if numbers on either side match by sum
- if equal, return index, if not -1

Edge Cases:
- less than one item in array/empty array
- negative numbers
- length

"""
def pivot_index(nums):
    # for i in range(len(nums)):
    #     left = sum(nums[:i])
    #     right = sum(nums[i + 1:])
    #     if left == right:
    #         return i
    # return -1
    # for i in range(len(nums)): #O(n^2)
    #     if sum(nums[:i]) == sum(nums[i + 1:]):
    #         return i
    # return -1
    left = 0
    right = sum(nums) # O(n)
    for i in range(len(nums)):
        right -= nums[i]
        if right == left: #O(1) ignore
            return i # O(1) ignore
        left += nums[i] # O(1) ignore
    return -1
    # this is just O(n)


print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1]))
print(pivot_index([0, 1, 0]))
print(pivot_index([1, 5, 3, 3, 3]))

