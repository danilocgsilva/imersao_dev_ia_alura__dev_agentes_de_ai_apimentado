#!/bin/bash

docker compose up -d --build
docker exec -i imersao_alura_agentes_ia_ambiente bash <<EOL
pip install -r requirements.txt --break-system-packages
flask run --host=0.0.0.0 --debug
EOL
