def palendrome(s,i,j):
    if i > j:
        return True
    return s[i] == s[j] and palendrome(s,i+1,j-1)
s= "abbb"
print(palendrome(s,0,len(s)-1))

