class Solution:
    def isValid(self, s:str) -> bool:
        # map={")":"(","]":"[","}":"{"}
        # stack=[]
        # for i in s:
        #     if i in map:
        #         if stack and map[i]==stack[-1]:
        #             stack.pop()            
        #         else:
        #             return False
        #     else: 
        #         stack.append(i)
        # return True if not stack else False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''