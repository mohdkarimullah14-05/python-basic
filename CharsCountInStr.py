s = input('Enter something : ').strip()
lc = {}
for i in range(0,len(s)):
    if s[i] in lc.keys():
        lc[s[i]] += 1
    else:
        lc[s[i]] = 1


print('Characters count in the string : ',lc)