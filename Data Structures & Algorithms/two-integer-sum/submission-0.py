class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_to_index = {}
        for i in range(len(nums)):
            current = nums[i]
            inverse = target - current
            if inverse in n_to_index:
                j = n_to_index.get(inverse)
                return [min(i, j), max(i, j)]
            else:
                n_to_index[current] = i
        return [0, 0]