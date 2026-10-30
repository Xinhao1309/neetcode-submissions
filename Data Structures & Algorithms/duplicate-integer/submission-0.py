class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for number in nums:
            if map.get(number) is not None:
                return True
            map[number] = 1
        return False


