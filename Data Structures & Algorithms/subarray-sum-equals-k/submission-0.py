class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hm={0:1}
        presum=0
        max_count=0

        for i in nums:
            presum+=i

            if presum-k in hm:
                max_count+= hm[presum - k]
            
            hm[presum]=hm.get(presum,0)+1
        return max_count
        