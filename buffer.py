"""
Problem:  Python program implementing a circular buffer

Platform : SelfStudy

Difficulty: hard

"""

from collections import deque

# Create a fixed-size buffer with capacity 3
buffer = deque(maxlen=3)

# Add items to the buffer
for item in [10, 20, 30, 40, 50]:
    buffer.append(item)
    print(f"Added {item} -> Buffer: {list(buffer)}")