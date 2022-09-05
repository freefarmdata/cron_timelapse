## Cron Expression (https://crontab.cronhub.io/)

Every 15 minutes, between 05:00 AM and 11:59 PM
```
*/15 5-23 * * *
```

## Setup Guide

### Install Software

```
sudo apt update -y && sudo apt upgrade -y
sudo apt install git

cd ~ && git clone https://github.com/freefarmdata/cron_timelapse.git

cd ~/cron_timelapse && pip install -r requirements.txt
```

### Create Files

```
mkdir /etc/timelapse
touch /etc/timelapse/log.txt
```

### Setup Cron Job

```
EDITOR=nano sudo crontab -e
```

Find your python installation:
```
which python3
```

Copy in the line below:
```
*/15 5-23 * * * <output of "which python3"> /home/pi/cron_timelapse/main.py >> /etc/timelapse/log.txt 2>&1
```
