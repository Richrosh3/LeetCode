"""
[MEDIUM]

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a
double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
[start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a
double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20,
but not including 20.

Constraints:
0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        booking = [start, end]

        if not self.calendar:
            self.calendar.append(booking)
            return True
        else:
            return self.binSortandInsert(booking)

    def binSortandInsert(self, booking):
        l, r = 0, len(self.calendar)
        start, end = booking

        while l < r:
            mid = (l + r) // 2

            if self.calendar[mid][0] <= start:
                l = mid + 1
            else:
                r = mid

        left = max(end, self.calendar[l - 1][1]) - min(start, self.calendar[l - 1][0]) < (
                    (end - start) + (self.calendar[l - 1][1] - self.calendar[l - 1][0]))

        if l >= len(self.calendar):
            right = False
        else:
            right = max(end, self.calendar[l][1]) - min(start, self.calendar[l][0]) < (
                        (end - start) + (self.calendar[l][1] - self.calendar[l][0]))

        overlaps = left or right

        if overlaps:
            return False
        else:
            self.calendar.insert(l, booking)
            return True

"""
Time Complexity: O(log(n))
Space Complexity: O(n)

Explanation: 
    Let's create a list as our calendar to keep track of the bookings. 
    We will sort this list as we insert bookings. To do this we will use binary sort. 
    
    If the calendar is empty, we add the first booking and return True. 
    If the calendar is not empty, we do a binary search on the calendar to find the position we may insert if there is
    no overlap. 
    Once we do the binary search, l will become the spot we are looking to insert to. 
    
    However, first we must check if the booking slot before and after does not overlap with the current booking. 
    To do this, we use a comparison of intervals, to see if there is an overlap. 
    If there are two intervals [a1,a2] and [b1,b2]. We can use the following to comparison to see if there is overlap. 
    if max(a2,b2) - min(a1-b1) < (a2-a1) + (b2-b2) then there is overlap. 
    We use this comparison for our current booking, but we must do it on the left and right intervals. If there is no 
    right interval, we can just say it is False.
    Once we get the result, if there is overlap we return False. Otherwise there is no overlap so we insert out booking
    at index l and return True. 
    
    Time complexity is O(log(n)) for each time we call book due to binary sort algorith, 
    Space complexity may be O(n) if no booking overlaps in the calendar.     
"""