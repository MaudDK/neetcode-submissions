class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        suffix = [0] * n
        maximum = -1

        for i in range(len(arr) - 1, -1, -1):
            suffix[i] = maximum
            maximum = max(arr[i], maximum)
        
        return suffix
            

        