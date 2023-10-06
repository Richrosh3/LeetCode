"""
[EASY/MEDIUM]

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1
"""


class NeetCodeSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # the value that determines how big our number is and how to get the left most digit
        div = 1

        # continually increases the div to find how big the number is
        while x >= 10*div:
            div = 10 * div

        while x:
            # gets value in the ones place
            right = x % 10
            # gets value in left most place
            left = x // div

            if right != left:
                return False

            # get rid of left and right most value
            # Ex: 123321 --> 2332
            x = (x % div) // 10
            # decrease divider by 2 places bc we chopped of 2 places in the number
            div = div / 100

        return True


"""
* Let n = # place values inside of x
Time Complexity: O(n/2)
Space Complexity: O(1)

Explanation: 
    The EASY solution is to change x from an integer to a string and check if it is a palindrome that way. 
    
    The MEDIUM solution requires a bit more math operations to check both sides of a number. 
    First, the description states if x is negative we return False which is covered by our first if statement. 
    Next we initialize a divider and increase it a factor of 10 each time until x < div. This allows us to determine
    the largest place value in x. For example for a number like 123321, the largest place value would be 100,000. So div
    would be 100,000. 
    Now that we have div, we will manipulate x in the while loop until x is not 0. 
    We obtain our right most digit (1's place value) by using mod 10. 
    We obtain our left most digit (largest place value) by using floor division on div. 
    Now we compare the two digits and if they are not the same, we will return False. 
    If they are the same, we have to check the next digits. 
    To do this, we use (x % div) to get rid of the left most digit and // 10 to get rid of the right most digit. 
    Like I said in the comments, with (x % div) // 10, 123321 becomes 2332. 
    Last thing to do in the while loop is decrease div by a factor of 100. This is because we got rid of two place values
    in the previous step, so dividing by 100 will account for that. 
    As soon as we break out of the while loop, we can determine that x was a palindrome and return True. 
    
    Time Complexity is O(n/2) because worst case is that x is a palindrome so we have to check the left and right digits 
    n/2 times to determine if it is a palindrome. 
    
    Space Complexity is O(1) because no data structures were utilized. 
"""