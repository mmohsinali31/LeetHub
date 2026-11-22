class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1={}
        c2={}
        for i in s:
            c1[i]=c1.get(i,0)+1
        for j in t:
            c2[j]=c2.get(j,0)+1
        return c1==c2