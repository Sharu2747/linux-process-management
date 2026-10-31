# Linux Systemd Service Assignment

## Project Overview

This project demonstrates how to create, configure, manage and monitor a Python background worker using Linux systemd.

The main service is `testpress-worker`.

## Technologies Used

- Linux (Ubuntu)
- Python 3
- systemd
- systemctl
- journalctl
- Bash

## Project Structure

```text
linux_assignment/
├── app.py
├── worker.env
├── notify_app.py
├── README.md
└── experiments.md
```

## Main Service Configuration

Service name: `testpress-worker`

Application path:

```text
/opt/testpress-worker/app.py
```

Service configuration highlights:

- Type=simple
- User=testpress
- Group=testpress
- Restart=on-failure
- RestartSec=5
- CPUQuota=20%
- MemoryMax=100M
- StartLimitIntervalSec=60
- StartLimitBurst=3

Environment variables are loaded using:

```ini
EnvironmentFile=/opt/testpress-worker/worker.env
```

## Service Management Commands

Check service status:

```bash
sudo systemctl status testpress-worker
```

Start service:

```bash
sudo systemctl start testpress-worker
```

Stop service:

```bash
sudo systemctl stop testpress-worker
```

Restart service:

```bash
sudo systemctl restart testpress-worker
```

Reload systemd configuration:

```bash
sudo systemctl daemon-reload
```

View service logs:

```bash
sudo journalctl -u testpress-worker
```

Follow live logs:

```bash
sudo journalctl -u testpress-worker -f
```

Check service type:

```bash
systemctl show testpress-worker -p Type
```

## Features Implemented

1. Python background worker.
2. Heartbeat logging.
3. Graceful shutdown using SIGINT and SIGTERM.
4. Environment variable configuration.
5. Automatic restart after failure.
6. Non-root service execution.
7. CPU and memory resource limits.
8. Restart rate limiting.
9. Logging through journald.
10. Practical testing of systemd service types.

## Testing

The following tests were performed:

- Service startup and shutdown.
- Journal logging verification.
- Non-root user execution.
- Application crash and automatic restart.
- SIGTERM graceful shutdown.
- Environment variable configuration.
- CPU and memory limits.
- Restart limit testing.
- Comparison of `simple`, `exec` and `notify` service types.

## Conclusion

This assignment provided practical experience in managing Python background applications using systemd, handling failures, monitoring logs, controlling resources and understanding service startup behavior.
