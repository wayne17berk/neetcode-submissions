class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        if len(s1)>len(s2): return False

        c1=[0]*26
        c2=[0]*26
        matches=0
        for i in range(len(s1)):
            c1[ord(s1[i])-ord('a')]+=1
            c2[ord(s2[i])-ord('a')]+=1
        matches+= sum(c1[s]==c2[s] for s in range(26))
        l=0
        for r in range(len(s1), len(s2)):
            if matches==26: return True

            leftindex=ord(s2[l])-ord('a')
            c2[leftindex]-=1
            if c1[leftindex]==c2[leftindex]:
                matches+=1
            elif c1[leftindex]-1 ==c2[leftindex]:
                matches-=1
            l+=1
            rightindex=ord(s2[r])-ord('a')
            c2[rightindex]+=1
            if c1[rightindex]==c2[rightindex]:
                matches+=1
            elif c1[rightindex]+1 ==c2[rightindex]:
                matches-=1
        return matches==26
            
