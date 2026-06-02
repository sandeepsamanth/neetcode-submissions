class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm={}

        for index,i in enumerate(nums):
            if target-i in hm:
                return [hm[target-i],index]
            else:
                hm[i]=index
        return []
        