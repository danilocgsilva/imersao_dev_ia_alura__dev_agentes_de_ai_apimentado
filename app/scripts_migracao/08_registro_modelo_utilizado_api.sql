CREATE TABLE modelo_chamada_api (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255) NOT NULL,
    desempenho_api_id INT,
    FOREIGN KEY (desempenho_api_id) REFERENCES desempenho_api(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
