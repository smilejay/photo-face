#!/bin/bash
pid_file=/var/run/gunicorn.pid
if [ -f $pid_file ]; then
    pid=$(cat $pid_file)
    kill -9 $pid
fi
gunicorn photo_face.wsgi -c gunicorn.cfg
