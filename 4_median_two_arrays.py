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

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_array = nums1 + nums2
    # get order of rankings
    rank = [0]*len(merged_array)
    for i, num1 in enumerate(merged_array):
        other_nums = merged_array[i+1:] + merged_array[0:i]
        for num2 in other_nums:
            if num1 > num2:
                rank[i] += 1
    # get median, but check if odd or even first
    if len(merged_array) % 2 == 0:
        imedian = [len(merged_array)//2, len(merged_array)//2+1]
        median_nums = list()
        for i,_ in enumerate(rank):
            if i in rank:
                median_nums.append(merged_array[rank[i]])
        median = sum(median_nums) / len(median_nums)
    else:
        imedian = len(merged_array) // 2
        for i,_ in enumerate(rank):
            if i == imedian:
                median = merged_array[rank[i]]    
    return(median)
    
    

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))