"""
[MEDIUM]

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        shortest = min(strs, key=len)
        i = 0

        for letter in shortest:
            for word in strs:
                if i == len(shortest) or letter != word[i]:
                    return ans
            ans += letter
            i += 1

        return ans

"""
Let X = length of shortest word

Time Complexity: O(X)
Space Complexity: O(1)

Explanation: 
    The shortest word in the list is the longest possible common prefix. 
    We look at every letter in the shortest word and compare it to all the strings in the list. We append every letter that 
    is found to be common amongst all the words. If our index i becomes larger than the length of the shortest word, or if
    a word's letter is not the same as the current shortest words letter, we immediately return ans. Otherwise, we go through 
    the full list, which means that the shortest word was our longest common prefix and we return ans. 
    
    Time complexity is O(length of shortest word).
    Space complexity is O(1) because only constant variables were used. 
"""