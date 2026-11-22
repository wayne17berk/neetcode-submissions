class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l].isalnum() and s[r].isalnum(): 
                if s[l].lower()!=s[r].lower():
                    return False
                else:
                    r-=1
                    l+=1
            elif not s[r].isalnum() and s[l].isalnum():
                r-=1
            elif not s[l].isalnum() and s[r].isalnum(): 
                l+=1
            else:
                r-=1
                l+=1
        return True