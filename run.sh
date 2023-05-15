#!/bin/bash

/usr/bin/pkill -f runserver

cd /Users/blake/projects/newsaggregator

/usr/bin/nohup /opt/homebrew/bin/python3 manage.py runserver --noreload &

/bin/sleep 45

/opt/homebrew/bin/wget -m -k -p -nH -P docs  http://127.0.0.1:8000/

/usr/bin/pkill -f runserver

time=$(date +%c)
/usr/bin/git add .
/usr/bin/git commit -m "Headlines update: $time"
/usr/bin/git push origin main
