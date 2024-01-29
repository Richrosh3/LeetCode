"""
[EASY]

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            sum_ = digits[i] + carry
            digits[i] = sum_ % 10
            carry = sum_ // 10

        if carry:
            digits.insert(0, 1)

        return digits


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We only have to add one to the last digit, but that last position may need to be carried over into several other 
    spots within the digits array. 
    
    First we check to see if the last digit + 1 < 10. If yes, then we can just increment the last digit and return digits. 
    If no, then we can start our carry off as 1 since we know that a carry will be needed because the previous if statement
    was not fulfilled. Now we enter a for loop starting from the last digit and decrementing downwards towards to the first
    index. We add digits[i] and carry to keep track of the current sum. Now digits[i] becomes the sum % 10 to give us the
    new digit. If there is a carry, sum//10 will give us 1; otherwise 0. After we finish the for loop, a carry may still
    be present, this means we need to insert a 1 in the 0th position. Finally, we can return digits. 
    
    Time Complexity is O(n) as we visit each element within the array once. 
    Space Complexity is O(1) because we used the digits array to modify values in place. 
"""