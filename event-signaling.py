import threading
import queue

def worker_thread(queue, event):
    while not event.is_set():
        try:
            task = queue.get(timeout=1)
            print(f"Worker thread processing: {task}")
            # Perform task processing here
        except Exception:
            print("Queue is empty. Waiting...")
    print("Worker thread exiting...")

def main():
    # Create a queue to store tasks
    task_queue = queue.Queue()

    # Create a thread event to signal the workers
    stop_event = threading.Event()

    # Create and start worker threads
    num_workers = 5
    threads = []
    for _ in range(num_workers):
        thread = threading.Thread(target=worker_thread, args=(task_queue, stop_event))
        thread.start()
        threads.append(thread)

    # Simulate task generation
    for i in range(10):
        task_queue.put(f"Task {i}")

    # After a certain time, signal the workers to stop
    import time
    time.sleep(5)
    stop_event.set()

    # Wait for all worker threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()