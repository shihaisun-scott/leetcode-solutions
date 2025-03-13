# median

nums1 = [1,2]
nums2 = [3,4]

print(sorted(nums1 + nums2))

sorted_array = sorted(nums1 + nums2)
n = len(sorted_array)

middle = len(sorted_array) // 2

if n % 2 == 0: # if even
    median = (sorted_array[middle-1] + sorted_array[middle]) / 2
else: # if odd
    median = sorted_array[middle]

print(median)

