# zigzag conversion
import numpy as np

s = "PAYPALISHIRING"
s = "AB"

nrows = 1

# calculate number of cols first
ncols = (len(s) // 2) + 1

matrix = np.full((nrows, ncols), '', dtype = '<U1')

count = 0
count2 = 0
while s:
    tmp_s = np.full((nrows,1), '', dtype = '<U1')
    if count == 0 or count % (nrows-1) == 0:
        tmp = list(s[:nrows])
        if len(tmp) == nrows:
            tmp_s = tmp
        else:
            for ii in range(len(tmp)):
                tmp_s[ii] = tmp[ii]
            tmp_s = tmp_s.flatten()
        s = s[nrows:]
    else:
        tmp_s[-count - 1] = s[0]
        tmp_s = tmp_s.flatten()
        s = s[1:]

    matrix[:,count2] = list(tmp_s)
    count += 1
    count2 += 1
    if count == nrows - 1:
        count = 0
    
print(matrix)


# now loop through each row to get the final string
matrix[:]

new_s = matrix.flatten()
new_s = new_s[new_s != '']
new_s = ''.join(new_s)

print(new_s)