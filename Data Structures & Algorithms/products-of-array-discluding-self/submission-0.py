class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        set = [1] * (len(nums))
        num = 1
        zero_counter = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                num = num * nums[i]
            else:
                zero_counter += 1

        if zero_counter >= 2:
            return [0] * len(nums)

        for i in range(len(nums)):
            if zero_counter == 1:
                if nums[i] == 0:
                    set[i] = num
                else:
                    set[i] = 0
            else:
                set[i] = num // nums[i]
                
        return set