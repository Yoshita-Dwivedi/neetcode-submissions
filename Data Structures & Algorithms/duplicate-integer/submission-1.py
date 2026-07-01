class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False
                