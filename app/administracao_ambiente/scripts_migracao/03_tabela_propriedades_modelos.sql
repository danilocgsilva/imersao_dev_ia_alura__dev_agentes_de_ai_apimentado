CREATE TABLE modelos_meta_dados(
    id INT AUTO_INCREMENT PRIMARY KEY,
    campo VARCHAR(255) NOT NULL,
    tipo_valor VARCHAR(32) NOT NULL,
    valor TEXT NOT NULL,
    modelo_id INT NOT NULL,
    FOREIGN KEY (modelo_id) REFERENCES modelos(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;