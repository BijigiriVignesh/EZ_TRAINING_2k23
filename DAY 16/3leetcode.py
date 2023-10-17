class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n =len(s)
        maxi =0
        st =""
        while(j<n):
            if not st or  s[j] not in st:
                st+= s[j]
                j+=1
                maxi = max(maxi,j-i)
            elif s[j] in st:
                st = st[1:]
                i+=1
        return maxi if maxi else len(st)



    