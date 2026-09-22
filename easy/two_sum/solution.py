class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_already = {}

        for i, value in enumerate(nums):
            missing_value = target - value
            if missing_value in nums_already:
                return [nums_already[missing_value], i]

            nums_already[value] = i
        print(nums_already)

s = Solution()

print(s.two_sum([2, 7, 11, 15], 9))