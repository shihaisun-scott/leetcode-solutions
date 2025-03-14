# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List
import numpy as np

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sorted_array = sorted(nums1 + nums2)
    arr_len = len(sorted_array)
    imedian = arr_len // 2
    if arr_len % 2 == 0: # if even
        median = (sorted_array[imedian] + sorted_array[imedian+1]) / 2
    else:
        median = sorted_array[imedian]
    return(median)
    
    

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))