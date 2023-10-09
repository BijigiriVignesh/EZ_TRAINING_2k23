def palendrome(s):
    left = 0
    right = len(s)-1
    while(left  < right):
        if s[left] != s[right]:
            left +=1
            right -=1
        if s[left:right+1] == s[left:right+1][::-1]:
            return True
    return False
print(palendrome("cabac"))
