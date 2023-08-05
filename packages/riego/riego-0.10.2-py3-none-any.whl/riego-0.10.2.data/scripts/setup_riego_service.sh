#!/bin/sh

sudo bash -c "cat > /etc/systemd/system/riego.service" <<'EOT'
[Unit]
Description=Riego Rain-System
After=mnt-usb1.mount mosquitto.service

[Service]
Nice=-9
IOSchedulingClass=best-effort
IOSchedulingPriority=0
Environment="PYTHONUNBUFFERED=1"
Type=simple
User=riego
WorkingDirectory=/mnt/usb1/riego
ExecStart=/mnt/usb1/riego/.venv/bin/riego
Restart=always

[Install]
WantedBy=multi-user.target
EOT

systemctl daemon-reload
systemctl enable riego
systemctl restart riego
