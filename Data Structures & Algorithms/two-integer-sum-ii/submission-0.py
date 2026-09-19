class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        res=[]
        while(i!=j):
            curSum=numbers[i]+numbers[j]
            if curSum==target:
                res=[i+1, j+1]
                break
            elif curSum<target:
                i+=1
            else:
                j-=1

        return res