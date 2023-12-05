# check nginx status
echo "Checking Nginx server status..."
nginx_status=$(systemctl is-active nginx)
if [ "$nginx_status" = "active" ]; then
    echo "Nginx is running."
else
    echo "Nginx is not running."
fi

# check CPU usage
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)" | \
           awk '{print "CPU Usage: " $2 + $4 + $6 "%"}'

# check RAM usage
echo "RAM Usage:"
free -h | awk '/^Mem:/ {print "Used: " $3 " / Total: " $2}'
