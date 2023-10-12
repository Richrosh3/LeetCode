"""
[MEDIUM]

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class NeetCodeSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]


"""
* let n = len(s) and m = # of words in wordDict
Time Complexity: O(n*m)
Space Complexity: O(n)

Explanation: 
    https://www.youtube.com/watch?v=Sx9NNgInc3A
    
    This one I don't think I can explain in detail that well. Watch NeetCode video above for more detailed explanation. 
    But the general idea is starting from the end, we look for a substring s[i:len(word)] that is in the wordDict. If 
    that substring is in the wordDict, then we set our dp table True at index i. This allows us to longer look for words 
    that start at index i. We keep going until we reach dp[0] where we should have found all words in our string that can 
    also be found in wordDict. 
    
    Time complexity is O(n*m) because we go through each index of s and then look at each word in wordDict for every index. 
    Space complexity is always O(len(s) + 1) --> O(len(s)) --> O(n). 
"""