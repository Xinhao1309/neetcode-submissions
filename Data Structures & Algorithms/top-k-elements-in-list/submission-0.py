

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap for counting
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        sorted_items = sorted(hm.items(),
                      key=lambda item: item[1],
                      reverse=True)
        res = []
        for i in range (k):
            item = sorted_items[i]
            res.append(item[0])
        return res

