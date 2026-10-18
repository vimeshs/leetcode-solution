class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range (n):
            for j in range (i+1,n):
                x=nums[i]
                y=nums[j]
                if x+y == target:
                    return [i,j]