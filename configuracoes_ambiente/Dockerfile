FROM debian:bookworm-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install \
    curl \
    git \
    python3 \
    python3-pip \
    mariadb-client \
    -y
RUN pip install --upgrade pip-tools --break-system-packages

RUN curl -sL https://deb.nodesource.com/setup_24.x | bash - 
RUN apt-get install -y nodejs

COPY instalar_dependencias_e_iniciar.sh /instalar_dependencias_e_iniciar.sh
RUN chmod +x /instalar_dependencias_e_iniciar.sh

CMD ["sleep", "1000"]
