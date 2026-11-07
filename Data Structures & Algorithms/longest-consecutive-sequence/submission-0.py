class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_set = set(nums)
        curr_max = 0
        for num in h_set:
            counter = 1
            if (num - 1) in h_set:
                continue
            else:
                while (num + 1) in h_set:
                    num += 1
                    counter += 1
            curr_max = max(curr_max, counter)

        return curr_max