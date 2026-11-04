class Solution:
    
    def groupAnagrams(self , strs: list[str]) -> list[list[str]]:
        hm ={}
        for string in (strs):
            # sort the string 
            sorted_text = "".join(sorted(string))
            if sorted_text not in  hm:
                 hm[sorted_text] = []
            hm[sorted_text].append(string)
        return list(hm.values()) 