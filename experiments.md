# Systemd Experiments and Observations

This document records the practical experiments performed during the Linux systemd assignment.

## Experiment 1: Type=simple

### Objective
Understand how systemd starts a service using `Type=simple`.

### Configuration

```ini
[Service]
Type=simple
```

### Observation

- systemd starts the application process.
- The service is considered started without waiting for an application readiness notification.

### Result

Successfully tested. The original `testpress-worker` service was restored to `Type=simple`.

---

## Experiment 2: Type=exec

### Objective
Understand the difference between `simple` and `exec`.

### Configuration

```ini
[Service]
Type=exec
```

### Observation

- systemd waits until the configured executable has been successfully executed.
- If executing the application fails, systemd can report the startup failure.

### Result

Successfully tested.

---

## Experiment 3: Type=notify

### Objective

Understand how systemd waits for an application to explicitly report readiness.

### Python application

File: `notify_app.py`

```python
import time
import subprocess

print("Application is starting...", flush=True)

time.sleep(5)

subprocess.run(["/usr/bin/systemd-notify", "READY=1"])

print("Application is ready!", flush=True)

while True:
    time.sleep(10)
```

### Service configuration

File: `/etc/systemd/system/test-notify.service`

```ini
[Unit]
Description=Test Notify Service
After=network.target

[Service]
Type=notify
ExecStart=/usr/bin/python3 /home/hp/linux_assignment/notify_app.py
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

### Test 1: Without readiness notification

Initially, the Python application did not send `READY=1`.

Command:

```bash
sudo systemctl start test-notify
```

Observation:

- Python application started successfully.
- Application printed its startup messages.
- systemd continued waiting for readiness.
- Service eventually failed with `Result: timeout`.

### Result

This demonstrated that `Type=notify` requires an explicit readiness notification.

### Test 2: With readiness notification

Modified the Python application to execute:

```python
subprocess.run(["/usr/bin/systemd-notify", "READY=1"])
```

This sends the readiness notification to systemd.

Before restarting, Python syntax was checked:

```bash
python3 -m py_compile notify_app.py
```

Restarted the service:

```bash
sudo systemctl restart test-notify
```

Checked the status:

```bash
systemctl status test-notify
```

Observed output:

```text
Application is starting...
Started test-notify.service
Application is ready!
```

Service status:

```text
Active: active (running)
```

### Result

Successfully tested. systemd received `READY=1` and marked the service as active.

---

## Comparison of Service Types

| Service Type | Startup Behavior |
|---|---|
| simple | Considered started when the process is started |
| exec | Waits for successful execution of the executable |
| notify | Waits for an explicit readiness notification |

## Final Conclusion

Through these experiments, I understood the differences between systemd service types.

- `simple` starts without waiting for application readiness.
- `exec` confirms successful execution of the configured executable.
- `notify` waits until the application sends a readiness notification using `READY=1`.

The original `testpress-worker` service remains configured as `Type=simple`.

The `test-notify` service was created separately for experimentation.
