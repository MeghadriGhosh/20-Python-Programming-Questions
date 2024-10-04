#   LRU Cache Implementation
#   Implement an LRU (Least Recently Used) cache using Python’s collections.OrderedDict or a custom implementation.


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # Initialize an OrderedDict
        self.capacity = capacity  # Set the capacity of the cache

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Return -1 if key is not found
        else:
            # Move the accessed item to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value associated with the key

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end (most recently used)
            self.cache.move_to_end(key)
        self.cache[key] = value  # Insert the key-value pair

        if len(self.cache) > self.capacity:
            # Remove the first (least recently used) item
            self.cache.popitem(last=False)

# Example usage:
lru_cache = LRUCache(3)  # Create an LRU Cache with capacity 3
lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)

print(lru_cache.get(1))  # Output: 1 (accessed key 1)
lru_cache.put(4, 4)      # Evicts key 2 (least recently used)
print(lru_cache.get(2))  # Output: -1 (not found)
lru_cache.put(5, 5)      # Evicts key 3 (least recently used)
print(lru_cache.get(3))  # Output: -1 (not found)
print(lru_cache.get(4))  # Output: 4
print(lru_cache.get(5))  # Output: 5
