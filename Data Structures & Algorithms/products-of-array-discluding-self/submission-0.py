class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        big_product = 1
        res = []
        null_counter = 0
        for num in nums:
            if num != 0:
                big_product *= num
            else:
                null_counter += 1
                if null_counter > 1:
                    return [0] * len(nums)

        for num in nums:
            if num == 0:
                res.append(big_product)

            else:
                if null_counter > 0:
                    res.append(0)
                else:
                    res.append(int(big_product / num))
                    
            
        
        return res