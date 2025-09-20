CREATE TABLE respostas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    resposta TEXT NOT NULL,
    data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura INT,
    modelo_utilizado VARCHAR(255),
    resposta_api_total TEXT NOT NULL,
    pergunta_id INT NOT NULL,
    FOREIGN KEY (pergunta_id) REFERENCES perguntas(id)
)