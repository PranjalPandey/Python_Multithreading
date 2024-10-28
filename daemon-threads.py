import threading
import time

# Function to run as a daemon thread
def daemon_task():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True  # Set the thread as daemon

# Start the daemon thread
daemon_thread.start()

# Main thread continues execution
time.sleep(5)
print("Main thread is done.")