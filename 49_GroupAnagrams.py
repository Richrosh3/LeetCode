"""
[MEDIUM]

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.



Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class NeetCodeSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

"""
Time Complexity: O(n*m)
Space Complexity: O(n)

    Anagrams will have same number of letters as each other. So we can use a list that keeps track of number of letters 
    as the key to our list of words that are anagrams. You can't technically have a list as a key, so you just wrap it as 
    a tuple to dodge that error. 
    Since we go through the list of words, then go through each letter in every word to keep track of the letter frequencies, 
    the time complexity will become O(n*m); where n is the length of strs and m is the length of the average word. 
    The space complexity is just O(n) because we create a key for every possible anagram. The count array will always have
    a length of 26, so that space is constant. Technically, the space complexity should be O(26*n), but that just simplifies
    down to O(n). 
    
    *** In theory this solution should be faster, and require less memory than my solution below. But on LeetCode my solution
    is faster, and utilizes less memory >:D ***
"""


class mySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agramMap = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in agramMap:
                agramMap[sortedWord] = [word]
            else:
                agramMap[sortedWord].append(word)

        return agramMap.values()

"""
Time Complexity: O(n*mlog(m))
Space Complexity: O(n)

Explanation: 
    Two words can be determined to be anagrams if their list of sorted letters are equivalent. To see if multiple words 
    are anagrams of each other in the list, we can create a dictionary to keep track of which words have the same sorted 
    letters. Once we finish going through the words, we can just return the dictionary values. 
    
    The time complexity each time we use sorted(), is O(mlog(m)). (Let m be the size of the words)
    Since we sort n words (n is size of strs), the overall time complexity is O(n*mlog(m)). 
    The space complexity will just be O(n) since we just have to store n sorted words as keys in the dictionary.
"""