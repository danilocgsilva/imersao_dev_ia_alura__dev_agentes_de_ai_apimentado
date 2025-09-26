let lista_botoes_acoes = document.querySelectorAll('.action-btn');
const resultados = document.getElementById('results');
const botao_perguntar = document.getElementById('botao_perguntar');
const seletor_pergunta = document.getElementsByName('tipo_pergunta');

function buscar_valor_radio() {
    for (const radio of seletor_pergunta) {
        if (radio.checked) {
            return radio.value;
        }
    }
}

function controla_campos_pergunta() {
    const campo_pergunta_modelo = document.getElementById('pergunta_modelo');
    const campo_pergunta_aberta = document.getElementById('pergunta_aberta_wrapper');

    let selectedValue = buscar_valor_radio();

    if (selectedValue === "pergunta_modelo") {
        campo_pergunta_modelo.classList.remove("hidden")
        campo_pergunta_aberta.classList.add("hidden")
    } else if (selectedValue === "pergunta_aberta") {
        campo_pergunta_modelo.classList.add("hidden")
        campo_pergunta_aberta.classList.remove("hidden")
    } else {
        campo_pergunta_modelo.classList.add("hidden")
        campo_pergunta_aberta.classList.add("hidden")
    }
}

const animacao_espera = {
    contador: 0,
    id_intervalo: null,

    start: function () {
        botao_perguntar.classList.add("disabled:bg-gray-400");
        botao_perguntar.classList.add("disabled:hover:bg-gray-400");
        botao_perguntar.classList.add("disabled:cursor-not-allowed");
        botao_perguntar.classList.add("disabled:opacity-75");
        botao_perguntar.disabled = true;
        
        resultados.style.fontSize = "200%";

        this.contador = 0;
        let innerHtmlConteudo = "Respondendo.";
        resultados.innerHTML = innerHtmlConteudo;

        if (this.id_intervalo) {
            clearInterval(this.id_intervalo);
        }

        this.id_intervalo = setInterval(() => {
            if (typeof resultados !== 'undefined' && resultados) {
                resultados.innerHTML = innerHtmlConteudo + ".".repeat(this.contador % 8);
                this.contador++;
            }
        }, 400);
    },

    stop: function () {
        resultados.style.fontSize = null;
        botao_perguntar.classList.remove("disabled:bg-gray-400");
        botao_perguntar.classList.remove("disabled:hover:bg-gray-400");
        botao_perguntar.classList.remove("disabled:cursor-not-allowed");
        botao_perguntar.classList.remove("disabled:opacity-75");
        botao_perguntar.disabled = false;

        if (this.id_intervalo) {
            clearInterval(this.id_intervalo);
            this.id_intervalo = null;
        }
    }
};

function Formulario() {
    this.formulario = document.getElementById('formulario');
    this.inicializar =  function () {
        this._pergunta = "";
        this.formulario.addEventListener('submit', async function (e) {
            e.preventDefault();

            const modelo = document.getElementById('modelo').value;

            if (buscar_valor_radio() === "pergunta_modelo") {
                this._pergunta = document.getElementsByName('pergunta_modelo')[0].value;
            } else if (buscar_valor_radio() === "pergunta_aberta") {
                this._pergunta = document.getElementById('pergunta_aberta').value;
            }

            if (!modelo || !this._pergunta) {
                alert('Todos os campos precisam ser preenchidos');
                return;
            }

            animacao_espera.start();
            try {
                let texto_resposta = "";

                const response = await fetch('/rag_enviar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        modelo,
                        pergunta: this._pergunta
                    })
                });

                const data = await response.json();
                texto_resposta = data.resposta;
                resultados.innerHTML = texto_resposta;
            } catch (error) {
                console.error('Error:', error);
                alert('Ocorreu um erro ao enviar o formulário.');
            } finally {
                animacao_espera.stop();
            }
        });
    }
    this.inicializar();
}

function atribuir_acoes_listagem_arquivos_rag() {
    lista_botoes_acoes.forEach(button => {
        button.addEventListener('click', function () {
            const action = this.title;
            const fileName = this.closest('.entry-item').querySelector('.text-gray-900').textContent;

            if (action === 'Delete') {
                if (confirm(`Are you sure you want to delete "${fileName}"?`)) {
                    this.closest('.entry-item').style.opacity = '0.5';
                    setTimeout(() => {
                        this.closest('.entry-item').remove();
                    }, 300);
                }
            } else if (action === 'Disable' || action === 'Enable') {
                if (action === 'Disable') {
                    this.title = 'Enable';
                    this.innerHTML = '<i class="fas fa-check-circle"></i>';
                    this.closest('.entry-item').style.opacity = '0.6';
                } else {
                    this.title = 'Disable';
                    this.innerHTML = '<i class="fas fa-ban"></i>';
                    this.closest('.entry-item').style.opacity = '1';
                }
            } else if (action === 'Download') {
                alert(`Downloading "${fileName}"...`);
            }
        });
    });
}

controla_campos_pergunta();
atribuir_acoes_listagem_arquivos_rag();
const formulario = new Formulario();
seletor_pergunta.forEach(radio => {
    radio.addEventListener('change', function() {
        controla_campos_pergunta();
    });
})
