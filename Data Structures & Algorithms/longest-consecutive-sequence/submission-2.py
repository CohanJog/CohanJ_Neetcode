class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = sorted(set(nums))

        longest = 1
        count = 1

        for i in range(len(ans) - 1):
            if ans[i] + 1 == ans[i + 1]:
                count += 1
                longest = max(longest, count)
            else:
                count = 1

        return longest