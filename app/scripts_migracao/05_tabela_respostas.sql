CREATE TABLE respostas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    resposta TEXT NOT NULL,
    data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_inicio_pergunta_milissegundos DECIMAL(19,6),
    data_final_pergunta_milissegundos DECIMAL(19,6),
    diferenca_milissegundos DECIMAL(19,6),
    pergunta_id INT NOT NULL,
    FOREIGN KEY (pergunta_id) REFERENCES perguntas(id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;