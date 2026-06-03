class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0

        max_arr=1
        final_arr=1
        nums.sort()
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                max_arr+=1
            else:
                max_arr=1
            final_arr=max(max_arr,final_arr)
        
        return final_arr+1
            
        

        