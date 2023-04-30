#!/bin/bash

cd /Users/blake/Desktop/newsaggregator

/usr/bin/nohup /opt/homebrew/bin/python3 manage.py runserver --noreload &

/bin/sleep 25

/opt/homebrew/bin/wget -m -k -p -nH -P wnynews.com  http://127.0.0.1:8000/

/usr/bin/pkill pkill -f runserver

time=$(date +%c)
/usr/bin/git add .
/usr/bin/git commit -m "News update: $time"
/usr/bin/git push origin main
