class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #Include it
            subset.append(nums[i])
            dfs(i + 1)

            #Dont Include it
            subset.pop()
            dfs(i + 1)
        

        dfs(0)
        return res

        

            



        
        