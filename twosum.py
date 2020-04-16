# Communication Steps

# - The Problem
#       Find the indexes of two numbers in a list of integers, that when added
#   together result in a certain prespecified sum.

# - Clarifiying Questions
#       The problem was stated clearly enough and requires no clarifying
#   questions.

# - Assumptions
#       The numbers will be in numeric format and be of either integer or float
#   types.

# - Think out loud
# -- Brainstorm Solutions
#        One solution would be to step through the list, using some kind of
#   loop to iterate through the values stored at each index, add them together,
#   then check if the sum matches the target value.
#       Another solution would be to subtract the value found at the first
#   index then loop through the remaining indexes to find a value that matches
#   the value calculated from the subtraction.

# -- Explain Rationale
#      A rationale is set of reasons or a logical basis for a course of action
#   or a particular belief. Any solution that solves the problem accurately has
#   value. A solution that solves it faster, using the least amount of storage
#   and processing power, is better.

# -- Discuss Tradeoffs
# -- Suggest Improvements



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # subtract the first number from target to simplify the search process
        x_num = target - nums[0]
        for i in range(1, len(nums)):
            # use range function to iterate through remaining list indexes
            if nums[i] == x_num:
                # if the value at list index matches x_num, return the indexes
                # of the two values
                return (0, i)
