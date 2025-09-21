#!/bin/bash

# flask run --host=0.0.0.0 --debug
# python3 -m flask --app app run --host=0.0.0.0 --debug
cd /app
python3 -m flask --app flask_app.main:web_framework run --host=0.0.0.0 --debug
