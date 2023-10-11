class Solution:
    def trap(self, height: List[int]) -> int:
        maxl =[0]
        maxr=[height[-1]]
        n = len(height)
        for i in range(1,n):
            maxl.append(max(height[:i]))
        right_max = height[-1]
        for i in range(n-2,-1,-1):
            if maxr[-1] <height[i+1]:
                maxr.append(height[-1])
                right_max = height[i+1]
            else:
                maxr.append(right_max)
        print("maxr ",maxr)
        op =0
        for i in range(n):
            if(min(maxr[i] , maxl[i]) -height[i] > 0):
                op+=min(maxr[i] , maxl[i]) -height[i]
        return op
    
