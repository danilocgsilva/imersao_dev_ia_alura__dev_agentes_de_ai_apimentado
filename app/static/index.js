
const formulario = document.getElementById('formulario');
const resultados = document.getElementById('results');

function travar_formulario() {
    const elementos = formulario.elements;

    for (let i = 0; i < elementos.length; i++) {
        elementos[i].disabled = true;
        elementos[i].classList.add('opacity-50', 'cursor-not-allowed');
    }
}

function liberar_formulario() {
    const elementos = formulario.elements;

    for (let i = 0; i < elementos.length; i++) {
        elementos[i].disabled = false;
        elementos[i].classList.remove('opacity-50', 'cursor-not-allowed');
    }
}

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

document.getElementById('menu-toggle').addEventListener('click', function () {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
})

document.getElementById('formulario').addEventListener('submit', async function (e) {
    e.preventDefault();
    travar_formulario();

    const modelo = document.getElementById('modelo').value;
    const temperatura = document.getElementById('temperatura').value;
    const pergunta = document.getElementById('pergunta').value;

    if (!modelo || !temperatura || !pergunta) {
        alert('Todos os campos precisam ser preenchidos');
        return;
    }

    try {
        let texto_resposta = "";
        animacao_espera.start();

        const response = await fetch('/perguntar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ modelo, temperatura, pergunta })
        });
        
        const data = await response.json();

        animacao_espera.stop();

        texto_resposta = data.resposta;

        resultados.innerHTML = texto_resposta;
    } catch (error) {
        console.error('Error:', error);
        alert('Ocorreu um erro ao enviar o formulário.');
    } finally {
        liberar_formulario();
    }
});