class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final_array=[]
        hm={}

        for i in strs:
            k=sorted(i)
            # print(k,"----")
            temp_i="".join(k)

            if temp_i not in hm:
                hm[temp_i]=[i]
            else:
                 hm[temp_i].append(i)

        for key,value in hm.items():
            final_array.append(value)

        return final_array

        