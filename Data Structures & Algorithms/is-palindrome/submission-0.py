class Solution:
    def isPalindrome(self, s: str) -> bool:

        i,j=0,len(s)-1
        while(i<j):
            fw,bw=s[i],s[j]
            if not fw.isalnum():
                i+=1
            elif not bw.isalnum():
                j-=1
            elif (fw.lower()!=bw.lower()):
                return False
            else:
                i,j=i+1,j-1

        return True