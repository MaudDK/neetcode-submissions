class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > stack[-1][0]:
                prevTemp, prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex
                
            stack.append([current_temp, i])
        
        return result




        