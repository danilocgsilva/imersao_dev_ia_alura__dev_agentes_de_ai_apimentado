CREATE TABLE modelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    ordem INT NOT NULL DEFAULT 1,
    desempenho_id INT NOT NULL,
    FOREIGN KEY (desempenho_id) REFERENCES desempenho_api(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;