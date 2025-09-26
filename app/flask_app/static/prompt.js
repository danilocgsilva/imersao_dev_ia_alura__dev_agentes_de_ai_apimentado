const formulario = document.getElementById('formulario');
const resultados = document.getElementById('results');
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

controla_campos_pergunta();

const animacao_espera = {
    contador: 0,
    id_intervalo: null,

    start: function () {
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

        if (this.id_intervalo) {
            clearInterval(this.id_intervalo);
            this.id_intervalo = null;
        }
    }
};

seletor_pergunta.forEach(radio => {
    radio.addEventListener('change', function () {
        controla_campos_pergunta();
    });
})

formulario.addEventListener('submit', async function (e) {
    e.preventDefault();

    const modelo = document.getElementById('modelo').value;
    const pergunta_modelo = document.getElementsByName('pergunta_modelo')[0].value;
    const pergunta_aberta = document.getElementById('pergunta_aberta').value;
    const prompt = document.getElementById('prompt').value;
    const tipo_pergunta = document.querySelector('input[name="tipo_pergunta"]:checked').value

    try {
        let texto_resposta = "";
        animacao_espera.start();

        const response = await fetch('/enviar_prompt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                modelo,
                pergunta_modelo,
                prompt,
                tipo_pergunta,
                pergunta_aberta
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
})
