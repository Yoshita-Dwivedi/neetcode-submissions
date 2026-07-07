class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       my_set = set()
       for i in nums:
        if i in my_set:
            return i
        my_set.add(i)

        