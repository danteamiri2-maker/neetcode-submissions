class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(x, v) for x, v in zip(position, speed)]
        cars.sort(reverse=True)

        time_stack = []
        for x, v in cars:
            time_stack.append((target - x) / v)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
        return len(time_stack)
            

        
