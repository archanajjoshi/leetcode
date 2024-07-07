class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_of_input = len(nums)
        for i in range(length_of_input):
            for j in range(i+1, length_of_input):
                if target == nums[i] + nums[j]:
                    return [i,j]
