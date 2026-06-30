class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for index, value in enumerate(nums):
            if value not in seen:
                seen[value] = index
            else:
                return True
        return False