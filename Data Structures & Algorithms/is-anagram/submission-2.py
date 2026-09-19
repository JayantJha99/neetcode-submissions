class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_1,cnt_2=Counter(s),Counter(t)
        if cnt_1!=cnt_2:
            return False
        return True