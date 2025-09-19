CREATE TABLE respostas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    resposta TEXT NOT NULL,
    data_busca TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pergunta_id INT NOT NULL,
    FOREIGN KEY (pergunta_id) REFERENCES perguntas(id)
)