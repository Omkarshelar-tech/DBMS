import threading
import time
from queue import Queue

# Shared buffer of max size 5
buffer = Queue(maxsize=5)

# Producer thread function
def producer():
    for i in range(10):
        buffer.put(f"Item-{i}")
        print(f"Produced: Item-{i}")
        time.sleep(1)

# Consumer thread function
def consumer():
    for i in range(10):
        print(f"Consumed: {buffer.get()}")
        time.sleep(2)


# Create threads
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

# Start threads
p.start()
c.start()

# Wait for both to finish
p.join()
c.join()
