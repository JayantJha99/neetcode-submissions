class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        curL,maxL=1,1
        nums.sort()
        prev=nums[0]
        for i in range(1,len(nums)):
            diff=nums[i]-prev
            if(diff==1):
                curL+=1
                maxL=max(maxL,curL)
            elif(diff==0):
                continue
            else:
                curL=1
            prev=nums[i]

        return maxL