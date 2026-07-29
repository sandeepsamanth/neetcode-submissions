class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)

        longest = 0 
        if len(nums)>0:
            longest=1
        for num in num_set:

            if num-1 in num_set:
                j=1
                while num-1 in num_set:
                    j+=1
                    longest=max(longest,j)
                    num=num-1
        return longest






        