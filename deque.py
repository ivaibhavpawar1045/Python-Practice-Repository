"""
Problem:  Python simulation using a queue (buffer) and batch processing to handle 
          high-speed incoming likes (5,500 likes in 18 seconds ≈ 305 likes/second) without overloading a database

Platform : SelfStudy

Difficulty: hard

"""


buffer = []
total_likes = 0

# Simulate 5,500 likes arriving in 18 seconds (~306/sec)
for user_id in range(1, 5501):
    buffer.append(user_id)  # Buffer incoming like in memory

    # Save to database in batches of 500 instead of 5,500 separate writes
    if len(buffer) == 500:
        total_likes += len(buffer)
        buffer.clear()

print(f"Handled {total_likes} likes in 18 seconds!")