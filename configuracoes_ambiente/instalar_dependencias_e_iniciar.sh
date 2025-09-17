#!/bin/bash

cd app
pip install -r requirements.txt --break-system-packages
flask run --host=0.0.0.0 --debug
