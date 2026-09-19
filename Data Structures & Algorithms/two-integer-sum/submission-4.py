class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(nums):
            req=target-num
            if req in freq.keys():
                return [freq[req],i]
            freq[num]=i

        return [-1,-1]