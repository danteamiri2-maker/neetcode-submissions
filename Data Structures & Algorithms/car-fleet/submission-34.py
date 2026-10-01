class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        time_stack = []
        for x, v in cars:
            t = (target - x) / v

            time_stack.append(t)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
        return len(time_stack)
            

        
