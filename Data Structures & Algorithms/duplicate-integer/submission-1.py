class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated = {}

        for i in range(len(nums)):
            if nums[i] in repeated:
                return True
            else:
                repeated[nums[i]] = 1

        return False


