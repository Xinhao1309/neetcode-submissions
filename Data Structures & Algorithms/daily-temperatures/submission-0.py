class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res