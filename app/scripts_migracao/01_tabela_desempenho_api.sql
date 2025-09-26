
CREATE TABLE desempenho_api (
    id INT AUTO_INCREMENT PRIMARY KEY,
    inicio_busca TIMESTAMP,
    fim_busca TIMESTAMP,
    tempo_transcorrido TIMESTAMP,
    comando VARCHAR(255),
    retorno_serializado TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
