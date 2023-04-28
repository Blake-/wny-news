#!/bin/bash

cd /Users/blake/Desktop/newsaggregator

nohup python3 manage.py runserver --noreload &

sleep 15

wget -E -H -k -K -p http://127.0.0.1:8000/

echo "Done"

pkill -f runserver
