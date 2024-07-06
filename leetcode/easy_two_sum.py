class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_of_input = len(nums)
        for i in range(length_of_input):
            for j in range(i+1, length_of_input):
                if target == nums[i] + nums[j]:
                    return [i,j]

```Given an integer x, return true if x is a
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?```
