# Communication Steps

# - The Problem

# - Clarifiying Questions

# - Assumptions

# - Think out loud
# -- Brainstorm Solutions
# -- Explain Rationale
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
