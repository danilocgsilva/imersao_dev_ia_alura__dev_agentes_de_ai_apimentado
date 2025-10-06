#!/bin/bash

cd app
pip install -r requirements.txt --break-system-packages
python3 -m comando --comando migrar
python3 -m comando --comando registrar_modelos_disponiveis
python3 -m flask --app flask_app.main:web_framework run --host=0.0.0.0 --debug
