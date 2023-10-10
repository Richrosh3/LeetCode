"""
[MEDIUM]

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the
rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it
unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can
visit all the rooms, or false otherwise.


Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


Constraints:
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        obtained_keys = set()

        def dfs(room_key):
            if room_key in obtained_keys:
                return
            obtained_keys.add(room_key)

            for key in rooms[room_key]:
                dfs(key)

        dfs(0)

        return len(obtained_keys) == len(rooms)


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    If you think of this as more of a graph of connected rooms rather than a linked list of connected room, it makes way
    more sense. 
    
    Once you realize it's a graph problem, dfs seems like the obvious solution. 
    We declared our set of keys "obtained_keys". 
    Then we create our dfs function with a parameter of room_key. If the room_key is in the set, we immediately return.
    If it is not in the set, we add it to the set, then call dfs on every key that is in room_room[key]
    Now we can just call dfs on the initial key that is given, 0. 
    Finally, to tell if we were able to go into every room, we just have to check if the number of keys in obtained_keys 
    is the same as the number of rooms. 
    
    Time complexity is O(n) because we visit every room in rooms. 
    Space complexity is O(n) because obtained_keys will get up to n keys. 
"""