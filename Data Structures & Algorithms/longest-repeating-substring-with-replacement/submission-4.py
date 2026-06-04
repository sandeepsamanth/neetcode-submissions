class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # x , y.   3-2>2

        max_count=0
        left=0
        max_freq=0

        hm={}

        for right in range(len(s)):
            hm[s[right]] = hm.get(s[right], 0) + 1

            max_freq = max(max_freq, hm[s[right]])
            

            while (right-left+1)-max_freq>k:
                left+=1
                if hm[s[left]] == 1:
                    del hm[s[left]]
                else:
                    hm[s[left]] -= 1
            
            print(hm,right-left+1,max_freq,max_count)
            
            max_count=max(max_count,right-left+1)
        
        return max_count

            
        