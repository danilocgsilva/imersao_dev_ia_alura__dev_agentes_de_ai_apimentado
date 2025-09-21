CREATE TABLE respostas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    resposta TEXT NOT NULL,
    data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura DECIMAL(6,4),
    modelo_utilizado VARCHAR(255),
    data_inicio_pergunta_milissegundos DECIMAL(19,6),
    data_final_pergunta_milissegundos DECIMAL(19,6),
    diferenca_milissegundos DECIMAL(19,6),
    resposta_api_total TEXT NOT NULL,
    pergunta_id INT NOT NULL,
    FOREIGN KEY (pergunta_id) REFERENCES perguntas(id)
)