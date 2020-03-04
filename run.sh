#!/bin/sh

exec gunicorn -b :5000 --reload --access-logfile - --error-logfile - application:app
