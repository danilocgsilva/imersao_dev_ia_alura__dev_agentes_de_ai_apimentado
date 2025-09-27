
CREATE TABLE desempenho_api (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contexto VARCHAR(255) NOT NULL,
    inicio_busca DOUBLE(21,6),
    fim_busca DOUBLE(21,6),
    tempo_transcorrido DOUBLE(19,6),
    comando VARCHAR(255),
    retorno_serializado TEXT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
