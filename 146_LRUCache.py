"""
[MEDIUM]

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
NeetCode Solution
"""
# creating doubly linked list nodes
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    # initialize capacity, dict, and nodes
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map keys to nodes

        # Left = least recently used, Right = most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # removing a node by pointing prev and next pointers to each other
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # inserting a node at the end of the list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete the least recently used from dict
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

"""
Time Complexity: O(1) for put and get
Space Complexity: O(n) bc of linked list and dict

Explanation: 
    https://www.youtube.com/watch?v=7ABFKPK2hD4&t=2s
"""


"""
My Solution
"""
class My_LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.LRU = []

    def get(self, key: int) -> int:
        res = self.cache.get(key)

        if res is None:
            return -1
        else:
            self.LRU.remove(key)
            self.LRU.append(key)
            return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.LRU.remove(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.pop(self.LRU.pop(0))

        self.LRU.append(key)

"""
Time Complexity: O(n) for put, O(n) for get
Space Complexity: O(n) for cache, O(n) for LRU

Explanation: 
    Let's work as we go through the problem. 
    When someone instantiates a LRUCache object, the capacity needs to be set. We do that in the __init__ 
    
    A person would then put an key value pair into the cache. For this it makes sense to utilize a dict. So in __init__
    we add a dict to the object called cache. It is important for us to make sure that capacity isn't being broken. If 
    it is, then we need to get rid of the Least Recently used value from the dict. To do this, I though a queue would be 
    greate because the first item in the list would always be our least recently used value. So we add a queue to the __init__
    called LRU. If a key is already in the cache, we need to remove it from the LRU first since it has now become the most
    recent. Then we update the value for the key in the LRU dict. If the capacity has been broken, we pop the first value
    in the queue, and remove it from the dictionary. Lastly we append the current key to the end of the queue. 
    
    For get, all we have to do is call the get function on the dictionary. We store the value and compare to see if it is
    None. If None, we return -1, otherwise we return res which contains the value. But we must not forget to get rid of
    the key from the LRU queue and re-add the key to the end of the queue. So we do that before returning res. 
    
    Time Complexity for both put and get are O(n) in the worst case. Because set's do not maintain order, we had to use 
    a list to keep track of order. This means that a .remove() on the list uses O(n) time to find the key.
    
    Space Complexity is O(n) for the cache and the LRU queue. Worst case would be if n unique key values were added to the 
    dict and the capacity was equal to n, which means the queue would be filled with n keys.
"""