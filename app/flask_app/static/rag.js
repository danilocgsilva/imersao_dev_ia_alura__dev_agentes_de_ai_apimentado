let lista_botoes_acoes = document.querySelectorAll('.action-btn');
const resultados = document.getElementById('results');

function Formulario() {
    this.formulario = document.getElementById('formulario');
    this.inicializar =  function () {
        this._pergunta = "";
        this.formulario.addEventListener('submit', async function (e) {
            e.preventDefault();

            const modelo = document.getElementById('modelo').value;
            this._pergunta = document.getElementsByName('pergunta_modelo')[0].value;

            if (!modelo || !this._pergunta) {
                alert('Todos os campos precisam ser preenchidos');
                return;
            }

            try {
                let texto_resposta = "";

                const response = await fetch('/enviar_pergunta_rag', {
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

atribuir_acoes_listagem_arquivos_rag();
const formulario = new Formulario();

