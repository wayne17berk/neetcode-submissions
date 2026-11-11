class Solution:   # required wrapper class

    def hasDuplicate(self, a: List[int]) -> bool:
        aset=set(a)
        return False if len(aset)==len(a) else True