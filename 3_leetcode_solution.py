# longest substring without repeating characters

s = "aab"
print(len(s))
print(len(set(s)))

if len(set(s)) == len(s):
    print(len(set(s)))

str_lengths = [0] * len(s)
for i in range(len(s)):
    ss = s[i:len(s)]
    new_s = ""
    for ii in range(len(ss)):
        if ss[ii] in new_s:
            str_lengths[i] = ii
            break
        else:
            new_s += ss[ii]
            if len(new_s) == len(ss):
                str_lengths[i] = len(new_s)

print(max(str_lengths))