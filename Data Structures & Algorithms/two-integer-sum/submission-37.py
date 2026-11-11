class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        res=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[target-nums[i]]=i
            else:
                res.append(seen[nums[i]])
                res.append(i)
        return res