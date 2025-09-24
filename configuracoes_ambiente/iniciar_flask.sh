#!/bin/bash

cd /app
python3 -m flask --app flask_app.main:web_framework run --host=0.0.0.0 --debug
