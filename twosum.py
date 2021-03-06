# Communication Steps

# - The Problem
#       Find the indexes of two numbers in a list of integers, that when the
#   values are added together they result in a certain prespecified sum.

# - Clarifying Questions
#       The problem was stated clearly enough and requires no clarifying
#   questions.

# - Assumptions
#       The numbers will be in numeric format and be of either integer or float
#   types.
#       You may assume that each input would have exactly one solution, and you
#   may not use the same element twice.

# - Think out loud
# -- Brainstorm Solutions
#        One solution would be to step through the list, using some kind of
#   loop to iterate through the values stored at each index, add them together,
#   then check if the sum matches the target value.
#       Another solution would be to subtract the value found at the first
#   index then loop through the remaining indexes to find a value that matches
#   the value calculated from the subtraction.

# -- Explain Rationale
#      A rationale is set of reasons or a logical basis for a course of action.
#   Any solution that solves the problem accurately has value. A solution
#   that solves it faster, using the least amount of storage and processing
#   power, is better.

# -- Discuss Tradeoffs
#   Leetcode.com gives a recursive solution to this problem that does not make
# sense and increases the time space complexity. The trade off of not using a
# recursive approach is a faster process.

# -- Suggest Improvements
#   - Seek code review


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # test case:
        #   List = [3,2,4]
        #   target = 6

        for i in range(0, len(nums)):
            # loop through indexes for first compliment
            x_num = target - nums[i]
            # subtract the first number from target to calculate compliment
            for j in range(i + 1, len(nums)):
                # loop through remaining indexes for second compliment
                if nums[j] == x_num:
                    # if the value at list index matches x_num, return the
                    # indexes of the two values
                    return (i, j)
