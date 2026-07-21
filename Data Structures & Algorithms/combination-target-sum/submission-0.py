class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        def dfs(index,target):

            if target == 0:
                result.append(subset.copy())
                return
            if target < 0:
                return
            if index >= len(nums):
                return
            
            subset.append(nums[index])
            dfs(index, target - nums[index])

            subset.pop()

            dfs(index + 1 , target)
        
        dfs(0,target)
        return result

        
        