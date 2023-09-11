"""
[MEDIUM]

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        ans = ""

        for k, v in romans.items():
            while num - k >= 0:
                num -= k
                ans += v

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We create a dictionary of all possible values to their roman numerals, including the pair instance such as "CM". It
    is important that we make the list of keys in descending order. 
    Then we iterate through the our key/value pairs and check if we can subtract the key from num. Since we are going in 
    descending order, the biggest possible value to be subtracted from num will be seen first. This allows us to get a
    value of "IV" instead of "IIII". We keep subtracting from num until num - k becomes less than 0. As we do this, we 
    append the roman numeral value to the ans string. 
    After iterating through all key/value pairs, we will have our answer so we can just return ans. 
    
    Time complexity is O(1) because we go through the dictionary once. 
    Space complexity is also O(1) for the 13 key/value pairs in the dictionary. 
"""






















