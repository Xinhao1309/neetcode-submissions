class Solution:
    
    def groupAnagrams(self , strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in (strs):
            counter_array = [0] * 26

            for c in s:
                counter_array[ord(c) - ord("a")] += 1
            tp = tuple(counter_array)
            res[tp].append(s)
        return list(res.values())
