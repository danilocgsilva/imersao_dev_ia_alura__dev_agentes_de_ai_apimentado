CREATE TABLE modelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    ordem INT NOT NULL DEFAULT 1,
    busca_id INT NOT NULL,
    FOREIGN KEY (busca_id) REFERENCES busca_api(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;