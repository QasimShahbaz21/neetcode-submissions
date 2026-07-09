class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):

        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        left = 0
        right = len(numbers)-1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left = left + 1
            else:
                right = right - 1