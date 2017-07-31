#! /bin/sh

case "$1" in
 start)
  echo "Starting listen-for-shutdown.py"
  /home/pi/startup/listen-for-shutdown.py &
  ;;
 stop)
  echo "Stopping listen-for-shutdown.py"
  pkill -f /home/pi/startup/listen-for-shutdown.py
  ;;
 *)
  echo "Usage: /home/pi/startup/shutdown.sh {start|stop}"
  exit 1
  ;;
esac

exit 0
