#!/bin/bash
# Copy project.service unit file to system folder
sudo cp /opt/programming_planet/shell_files/app.service /etc/systemd/system/
#sudo cp /var/misc-ml/bulk_mail_service/shell/api.service /etc/systemd/system/
# Load ALL system unit files into memory
sudo systemctl daemon-reload
# Make the service start during boot [without extension enable]
sudo systemctl enable app
#sudo systemctl enable api