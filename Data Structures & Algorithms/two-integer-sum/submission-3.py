class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        indices={}
        indices[nums[0]]=0
        for i in range(1,len(nums)):
            num2=target-nums[i]
            if num2 in indices.keys():
                ans.extend([indices[num2],i])
            indices[nums[i]]=i
            
        return ans
