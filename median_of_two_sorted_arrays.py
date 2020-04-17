# leetcode.com Problem 4

# The Problem
#   Find the median of two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

# Clarifying Questions
#   Is the median supposed to be derived from the combination of both lists or
# from each list seperately?
#   Why should the complexity be O(log (m+n)) when it can be O(n)?

# Assumptions
#   You may assume nums1 and nums2 cannot be both empty.

# Think out loud
# - Brainstorm Solutions
#   - This looks like it should be pretty easy to solve. Just add the two lists
# together, find the midpoint by dividing the overall length by two. If it
# divides evenly, also find the index previous to the midpoint. Add the
# values found at the midpoint and the index previous to midpoint together then
# divide by two to calculate the median. Otherwise return the value at the
# midpoint as the median.

# -- Explain Rationale
#      A rationale is set of reasons or a logical basis for a course of action.
#   Any solution that solves the problem accurately has value. A solution
#   that solves it faster, using the least amount of storage and processing
#   power, is better.

# -- Suggest Improvements
#   When ran on the leetcode site, the regular division to calculate the
# median of an even numbered array does not function correctly. Seek outside
# input to possibly spot what the issue could be.


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        all_nums = nums1 + nums2
        int_count = len(all_nums)
        print('int_count:', int_count)
        all_nums.sort()
        print('all_nums:', all_nums)
        if int_count % 2 == 0:
            median1 = all_nums[int_count//2]
            print('median1:', median1)
            other_index = (int_count//2)-1
            median2 = all_nums[other_index]
            print('calculated index of second median:', other_index)
            print('median2:', median2)
            median = float((median1 + median2)/2)
            print('median of even set:', median)
        else:
            median = all_nums[int_count//2]
        return median
