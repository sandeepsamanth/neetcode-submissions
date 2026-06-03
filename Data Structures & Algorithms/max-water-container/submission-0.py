class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r=0,len(heights)-1

        max_temp=0
        while l<r:
            temp=min(heights[l],heights[r])*(r-l)
            max_temp=max(max_temp,temp)

            if l<r:
                l+=1
            else:
                r-=1
        return max_temp
        