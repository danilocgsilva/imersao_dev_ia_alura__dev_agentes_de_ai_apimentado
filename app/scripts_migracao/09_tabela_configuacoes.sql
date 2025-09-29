CREATE TABLE configuracoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arquivo VARCHAR(255) NOT NULL,
    ativo TINYINT(1) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
