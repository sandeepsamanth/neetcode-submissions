class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        i=0
        final_array=[]
        while i<len(nums):
            prod=1
            j=i
            while j <len(nums):
                prod*=nums[j]
                if prod<k:
                    final_array.append(nums[i:j+1])
                j+=1
            i+=1
        # print(final_array)

        return len(final_array)

        