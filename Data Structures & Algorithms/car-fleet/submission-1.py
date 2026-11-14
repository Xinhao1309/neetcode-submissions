class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[position[i], speed[i]] for i in range(len(position))]
        sorted_list = Solution.merge_sort(position_speed)

        time_of_arrival = []
        for i in range(len(sorted_list)):
            if i == 0:
                time_of_arrival.append((target  - sorted_list[i][0]) / sorted_list[i][1])
                continue
            else:
                time_of_arrival.append((target - sorted_list[i][0]) / sorted_list[i][1])
                if time_of_arrival[-1] <= time_of_arrival[-2]:
                    time_of_arrival.pop()
                
        return len(time_of_arrival)


    @staticmethod
    def merge_sort(input: list[list[int]]) -> list[list[int]]:
        if not input or len(input) == 1:
            return input
        
        input_length = len(input)

        sorted_left = Solution.merge_sort(input[0:input_length // 2])
        sorted_right = Solution.merge_sort(input[input_length // 2: input_length])
        
        left_pointer = 0
        rigth_pointer = 0
        res = []
        for i in range(input_length):
            if left_pointer >= len(sorted_left):
                res.append(sorted_right[rigth_pointer])
                rigth_pointer += 1
            elif rigth_pointer >= len(sorted_right):
                res.append(sorted_left[left_pointer])
                left_pointer += 1
            else:
                left_value = sorted_left[left_pointer][0]
                right_value = sorted_right[rigth_pointer][0]

                if left_value >= right_value:
                    res.append(sorted_left[left_pointer])
                    left_pointer += 1
                else:
                    res.append(sorted_right[rigth_pointer])
                    rigth_pointer += 1       

        return res       
