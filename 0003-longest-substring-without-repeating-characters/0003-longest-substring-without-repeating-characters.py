class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        l=0
        count=0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[l])
                l+=1
            ans.add(s[i])
            count=max(count,i-l+1)
        return count
            