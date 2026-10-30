import time
import signal
import sys
import os

def shutdown(signum, frame):
    print("\nWorker shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

interval = int(os.getenv("HEARTBEAT_INTERVAL", "5"))
crash_after = int(os.getenv("CRASH_AFTER", "0"))

print("Worker started")
print(f"Heartbeat interval: {interval} seconds")

start_time = time.time()

while True:

    if crash_after > 0 and time.time() - start_time >= crash_after:
      print("Simulating worker crash!")
      sys.exit(1)
    
    print("Heartbeat: Worker is alive")
    time.sleep(interval)