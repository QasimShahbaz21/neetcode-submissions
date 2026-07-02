class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) #[1,1,1,1]
        left_product = 1
        for i in range(len(nums)): #0, 1, 2
            result[i] = left_product #result =  1 //[1,1,1,1],[1,1,1,1], [1,1,2,1]
            left_product = left_product * nums[i] #left_product = 1 *1, 1*2 =2,8

        right_product=1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * right_product 
            right_product = right_product * nums[i]
        
        return result

            
            