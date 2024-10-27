import threading
import queue
import time

# Create a thread-safe queue
message_queue = queue.Queue()

# Function to produce messages
def produce_messages():
    for i in range(500):
        time.sleep(1)
        message_queue.put(f"Message {i}")
        print(f"Produced: {i}\n")

# Function to consume messages
def consume_messages():
    while True:
        message = message_queue.get()
        if message == "STOP":
            break
        print(f"Consumed: {message}")

# Create two threads
producer_thread = threading.Thread(target=produce_messages)
consumer_thread = threading.Thread(target=consume_messages)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish producing messages
producer_thread.join()

# Signal the consumer to stop after processing all messages
message_queue.put("STOP")

# Wait for the consumer to finish consuming messages
consumer_thread.join()