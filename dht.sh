#!/bin/bash

HOSTNAME="${COLLECTD_HOSTNAME:-localhost}"
INTERVAL="${COLLECTD_INTERVAL:-60}"

while sleep "$INTERVAL"; do
    VALUE=$(sudo /usr/local/vbin/dht.py)
    TEMP=$(echo ${VALUE} | awk -F'#' '{ print $1 }')
    HUM=$(echo ${VALUE} | awk -F'#' '{ print $2 }')
    DFP=$(/bin/df -h / | /usr/bin/tail -1 | /usr/bin/awk '{print substr($5,1,length($5)-1)}')
    echo "PUTVAL \"$HOSTNAME/exec/temperature\" interval=$INTERVAL N:$TEMP"
    echo "PUTVAL \"$HOSTNAME/exec/humidity\" interval=$INTERVAL N:$HUM"
    echo "PUTVAL \"$HOSTNAME/exec-diskspace/percent-diskspace\" interval=$INTERVAL N:$DFP"
done
