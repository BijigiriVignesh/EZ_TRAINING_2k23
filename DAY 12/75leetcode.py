class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count  = [0]*3
        for i in nums:
            count[i] +=1
        nums.clear()
        for i,num in enumerate(count):
            nums.extend([i]*num)
        print(nums)

