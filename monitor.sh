
LOG_FILE="monitor.log"
while true
do
    pgrep -f "consumer.py" > /dev/null
    if [ $? -ne 0 ]
    then
        echo "$(date) - Consumer not running. Restarting..." >> $LOG_FILE
        python3 consumer.py &
    fi
    sleep 30
done