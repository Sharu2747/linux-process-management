import time
import subprocess

print("Application is starting...", flush=True)

time.sleep(5)

subprocess.run(["/usr/bin/systemd-notify", "READY=1"])

print("Application is ready!", flush=True)

while True:
    time.sleep(10)
