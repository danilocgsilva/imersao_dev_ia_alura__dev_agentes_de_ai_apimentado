const formulario = document.getElementById('formulario');
const resultados = document.getElementById('results');

formulario.addEventListener('submit', async function (e) {
    e.preventDefault();

    const modelo = document.getElementById('modelo').value;
    const pergunta = document.getElementsByName('pergunta')[0].value;
    const prompt = document.getElementById('prompt').value;

    try {
        let texto_resposta = "";

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
    }
})
