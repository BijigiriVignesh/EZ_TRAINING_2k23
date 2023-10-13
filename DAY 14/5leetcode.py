def longestPalindrome(self,s: str) -> str:
    n = len(s)
    longest ={}
    if n ==1:
        return s
    for i in range(n):
        for j in range(i,n):
            longest[s[i:j+1]] =j-i
    print(longest)
    max_str= i
    max_length = 0
    for i in longest:
        if i == i[::-1] and len(i) >max_length :
            max_length = len(i)
            max_str = i
    return max_str




    