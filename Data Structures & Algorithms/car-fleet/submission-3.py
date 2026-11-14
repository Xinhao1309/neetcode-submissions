class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[position[i], speed[i]] for i in range(len(position))]
        sorted_list = sorted(position_speed, key=lambda pair: pair[0], reverse=True)

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
