class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique_set=set()
        left=0
        maximum=0

        for right in range(len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left+=1
            unique_set.add(s[right])
            maximum=max(maximum,right-left+1)
        return maximum

                
                


        