# longest palindromic substring

s = "babad"

str_lens = []
strs = []

if len(s) == 1:
    print(s)
elif len(s) == 0:
    print('')

for iletter in range(len(s)):
    new_str = s[iletter]

    remaining_str = s[iletter + 1: len(s)]

    for iletter2 in range(len(remaining_str)): # find the palindromes in this loop
        new_new_str = new_str + remaining_str[0:iletter2+1]
        # reverse string and then check if equal
        rev_str = new_new_str[::-1]
        if rev_str == new_new_str:
            str_lens.append(len(new_new_str))
            strs.append(new_new_str)


if str_lens:
    imax = str_lens.index(max(str_lens))
    print(strs[imax])

else:
    print(s[1])