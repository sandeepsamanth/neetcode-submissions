class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm_1={}
        for i in s1:
            hm_1[i]=hm_1.get(i,0)+1

        left=0
        hm_2={}
        for right in range(len(s2)):
            hm_2[s2[right]]=hm_2.get(s2[right],0)+1

            if s2[right] in hm_1 and hm_2[s2[right]]<=hm_1[s2[right]]:
                if hm_1==hm_2:
                    return True
            else:
                if hm_2[s2[left]]==1:
                    del hm_2[s2[left]]
                else:
                    hm_2[s2[left]]-=1
                
                left+=1
        return False



