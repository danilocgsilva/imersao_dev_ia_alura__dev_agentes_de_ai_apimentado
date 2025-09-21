document.getElementById('menu-toggle').addEventListener('click', function () {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
})
document.getElementById('formulario').addEventListener('submit', async function (e) {
    e.preventDefault();

    const modelo = document.getElementById('modelo').value;
    const temperatura = document.getElementById('temperatura').value;
    const pergunta = document.getElementById('pergunta').value;

    if (!modelo || !temperatura || !pergunta) {
        alert('Todos os campos precisam ser preenchidos');
        return;
    }

    try {
        let texto_resposta = "";
        const response = await fetch('/perguntar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ modelo, temperatura, pergunta })
        });
        const data = await response.json();

        texto_resposta = data.resposta;

        document.getElementById('results').innerHTML = texto_resposta;
    } catch (error) {
        console.error('Error:', error);
        alert('Ocorreu um erro ao enviar o formulário.');
    }
});