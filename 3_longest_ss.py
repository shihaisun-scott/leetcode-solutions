# 3: longest substring without repeating characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s: str) -> int:
    max_str = ""
    for i,_ in enumerate(s):
        new_str = s[i:]
        cat_str = "" # concat the string
        for ii, char in enumerate(new_str):
            if char not in cat_str:
                cat_str += char
            else:
                break
        if len(cat_str) > len(max_str):
            max_str = cat_str
    return(len(max_str))


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))