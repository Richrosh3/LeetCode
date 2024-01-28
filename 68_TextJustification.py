"""
[HARD]

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be
left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        while words:
            # PART 0
            i = 0
            curr_sentence_size = 0
            curr_space_size = 0
            sentence = ""

            # PART 1
            while i < len(words) and curr_sentence_size + curr_space_size + len(words[i]) <= maxWidth:
                curr_sentence_size += len(words[i])
                if curr_sentence_size + curr_space_size + 1 <= maxWidth:
                    curr_space_size += 1

                i += 1

            # PART 2
            diff = maxWidth - curr_sentence_size
            if (i - 1) > 0:
                spaces = diff // (i - 1)
                remainder = diff % (i - 1)
            else:
                spaces = 1
                remainder = 0

            # PART 3
            if words[i:]:
                for idx in range(0, i):
                    sentence += words[idx]
                    if maxWidth - len(sentence):
                        sentence += " " * spaces
                    if remainder:
                        sentence += " "
                        remainder -= 1
            else:
                for idx in range(0, i):
                    sentence += words[idx]
                    if maxWidth - len(sentence):
                        sentence += " "

            # PART 4
            while len(sentence) < maxWidth:
                sentence += " "

            # PART 5
            ans.append(sentence)
            words = words[i:]

        return ans


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    This is a hard problem due to the sheer amount of steps and edge cases needed to be considered to complete it. I 
    split this problem into 6 steps, to simplify the thought process as I completed the problem. 
    
    Before we start, we will create an empty array ans to store our answers, and we will start a while loop with the
    condition that words has content in it. 
    
    # PART 0
    This is the initial setup for every iteration of the loop. i keeps track of the current word, current_sentence_size
    holds the size of the possible sentence and curr_space_size holds the size of the possible spaces. sentence is used
    later on, but it is still necessary to reset it to an empty string at the start of each loop. 
    
    # PART 1
    Here we are seeing if we can add a word to the current sentence without exceeding the maxWidth. It is important here
    that we check to see if i < len(words). Let's say words only contains one word. If i exceeds 1, then the loop breaks.
    To keep track of the current sentence, we are checking to see if the current sentence size + the current space size
    + the length of the current possible word is less than or equal to maxWidth. If so, we add the word to sentence, 
    check to see if we can add an extra space and then increment i to move on to the next word. 
    
    # PART 2
    Now it is time to determine the size of the spaces between words. diff is the # of extra spaces that need to be 
    inserted to hit the maxWidth quota. (i-1) is the index of the last word we just placed into the sentence. If (i-1) 
    is greater than 0, that means we had more than 1 word inserted. Spaces will be evenly distributed by the difference
    of spaces integer divided by the number of words in the sentence. remainder of spaces is determined if there is extra
    space that did not evenly distribute after the division. If (i-1) < 0, that means we only had one word so only one 
    space needs to be inserted and there will be no remainder. 
    
    # PART 3
    The actual insertion of words and spaces to form a sentence is in this section. 
    words[i:] checks to see if there is any further words in the list. We do this because the last sentence has to add
    padding only to the last word. 
    If the current sentence is not the last sentence, then for every word we add to the sentence, we must check if 
    maxWidth - len(sentence) is greater than 0. If so, we " " * spaces to the sentence. If there is a remainder of 
    spaces left, we add that to the sentence as well and decrement remainder.
    If the current sentence is the last sentence, then we only have to add the words and keep one space between each word
    if there maxWidth - len(sentence) > 0. 
    
    # PART 4
    If a sentence still does not meet the maxWidth quota, we pad the sentence with extra spaces until it does. 
    
    # PART 5
    Lastly, we append the current sentence to the ans array and get rid of the used words by shortening the words array
    with words[i:]
    
    Once words becomes empty, the while loop will break and we can just return ans. 
    
    Time Complexity is O(n). Although there are multiple nested loops within the code, each loop processes a word only 
    once. 
    
    Space Complexity is also O(n). Each sentence being added to the ans array is dependent on the size of each word. So
    in the worst case, ans will have n elements. 
"""