#!/bin/bash
cd /home/bitnami/name-checker/
ps aufx | grep 'app.py' | grep 'python' > /dev/null 2>&1
if [ $? ==  0 ]
then
    echo "Still running"
else
    echo "FAILED, restarting"
    authbind --deep /opt/bitnami/python/bin/python bin/app.py 80 > /home/bitnami/log.txt 2>&1 &
fi
