#!/bin/bash

cd /Users/blake/Desktop/newsaggregator

#nohup python3 manage.py runserver --noreload &

#sleep 15

#wget -m -k -p -nH -P wnynews.com  http://127.0.0.1:8000/

#echo "Got it!"

#pkill -f runserver

time=$(date +%c)
git add .
git commit -m "fix date"
git push origin main
