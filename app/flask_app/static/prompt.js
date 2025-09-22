const formulario = document.getElementById('formulario');
const resultados = document.getElementById('results');

const animacao_espera = {
    contador: 0,
    id_intervalo: null,
    
    start: function() {
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
    
    stop: function() {
        resultados.style.fontSize = null;

        if (this.id_intervalo) {
            clearInterval(this.id_intervalo);
            this.id_intervalo = null;
        }
    }
};

formulario.addEventListener('submit', async function (e) {
    e.preventDefault();

    const modelo = document.getElementById('modelo').value;
    const pergunta = document.getElementsByName('pergunta')[0].value;
    const prompt = document.getElementById('prompt').value;

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
                pergunta,
                prompt
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
