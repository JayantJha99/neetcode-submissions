class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s,cnt_t={},{}
        for ch in s:
            if ch not in cnt_s:
                cnt_s[ch]=1
            else:
                cnt_s[ch]+=1
        
        for ch in t:
            if ch not in cnt_t:
                cnt_t[ch]=1
            else:
                cnt_t[ch]+=1

        return cnt_s==cnt_t

        