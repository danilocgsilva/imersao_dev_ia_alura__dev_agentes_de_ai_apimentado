# Exercício Imersão DEV Alura - Agentes de IA com Gemini

* [Carta de intenções](#carta-de-intenções)
* [Subindo ambiente](#subindo-o-ambiente)
* [Recursos](#recursos)

## Carta de intenções

A Imersão DEV Agentes de IA da Alura, iniciada no dia 08 de Setembro de 2025, tinha como objetivo mostrar as tecnicas vigentes para a criação de agentes de AI para profissionais de qualquer nível e qualquer carreira.

Participei seguindo o passo-a-passo, mas como já um profissional há diversos anos na carreira de desenvolvedor, decidi refazer os passos da imersão de forma *apimentadata*.

Seguem os temperos:

### ESTOU PROIBIDO DE USAR O GOOGLE COLAB

Depender de serviçose de terceiros para prover as soluções é algo que me incomoda um pouco. Entendo que se basear em um provedor de serviço externo é uma estratégia para agilizar processos pela grande conveniência que eles entregam, mas convenhamos que as pessoas utilizam os serviço de terceiro pela comodidade. E daí vem o problema: o provider lock-in, mudanças de políticas de acesso, limites de requisições, reajustes de preços e até a indisponibilidade do serviço por qualquer motivo que seja são problemas em potencial que uma pessoa passa ao decidir depender de provedor externo. Fora que a disciplina de manter a sua própria infraestrutura facilita no momento de disponibilizar a solução em qualquer outro provedor disponível, e novamente, não estar dependente apenas daquilo que é oferecido dentro do Google.

Entendo que como parte a proposta é utilizar o serviço do google pela sua api para ter acesso aos modelos, e neste caso, ainda estaremos dependentes do serviço do Google. Mas até isso podemos superar, já que a possibilidade de utilizar modelos rodando localmente também será explorado.

### Utilização de Docker

Em substituição do Google Colab, utilizarei um ambiente de desenvolvimento *containerizado*. Os problemas relacionados à instalação e interdependência de pacotes que existem ao cuidar da sua própria infraestrutura ensinarão disponibilizar a solução em qualquer nuvem ou mesmo em servidores on-promise.

### Interface web

Durante a Imersão, fica inconveniente testar e registrar testes e parametrizações que eventualmente o estudante queira testar.

Disponibilizar uma interface web facilita e deixa a experiência do aprendizado muito mais prazeirosa.

A interface web oferecerá mecanismos de histórico de questões, alteração do modelo a ser utilizado, possibilidade de alterar a utilização de agentes no modo completamente offline (sem depender da api e, consequentemente, de uma chave de acesso do Google), alteração de parâmetros como a temperature, e alteração dos dados para o RAG, com a possibilidade de adicionar e remover pdfs que tenham os dados a serem cosumidos pelo RAG.

### Flask

Servidor web simples, que utiliza Python. Deste modo, tem-se mais aderêcia e simplicidade ao interagir com o código criado para os agentes.

Apesar da simplicidade da proposta da imersão, o cuidado de oferecer uma interface web com todos os controles e conveniência necessário será um ótimo exercício de código limpo e padrão de projeto.

### Jinja como view

Recurso com boa aderência do Flask para o desenvolvimento das das interaces web.

### Tailwind

O framework CSS que é conhecido por facilitar muito e facilitar ao prover classes de modo a fazer o desenvolvedor não precisar criar folhas de estilos e conseguir servir templates visualmente agradáveis.

### Banco de dados relacional

A gerência e conversa com um banco de dados relacional será fundamental para guardar preferências de usuário, o histórico de perguntas e mesmo os logs para monitorar o desempenho da aplicação e da API utilizada.

### Para além do Google Gemini - mas se mantendo nos recursos gratuitos

Ferramentas como Chats de outros providers (Deepseek e ChatGPT) já estão muito comumente utilizadas no meu fluxo de desenvolvimento. Como assitente de codificação, utilizo o Amazon Q, já que diferentemente do CoPilot, até então não me foi imposto nenhum limite de uso, mesmo na versão gratuita.

## Subindo o ambiente

### Variáveis de ambiente

É importante copiar o arquivo `.env.exemplo` para um outro arquivo chamado `.env`, substituindo as informações necessárias. Destaque para a variável `CHAVE_API_GOOGLE`, que é preciso ser gerada no Google, caso contrário não será possível acessar a api do Google.

### Compilando o ambiente

Execute o seguinte comando:
```
docker compose up -d --build
```

Depois, será necessário construir migrar o banco de dados. Execute:

```
docker exec -it imersao_alura_agentes_ia_ambiente python3 comando.py --comando migrar
```

Ou, pode entrar no container e o comando é mais simples:
```
python3 comando.py --comando migrar
```

### Log

Por padrão, a aplicação mantém um arquivo na raiz chamado `app.log`. As atividades realizadas costuma escrever nesse arquivo para permitir o monitoramento.

## Recursos

### Comandos

Algumas ações são possíveis a partir de comandos que podem ser executados pelo terminal.

Para executar um comando fora do container, execute o seguinte:

```
docker exec -it imersao_alura_agentes_ia_ambiente python3 comando.py --comando <o_seu_comando>
```

Dentro do container, os comandos podem ser executados da seguinte forma:
```
python3 comando.py --comando <o_seu_comando>
```

**Listando os comandos disponíveis**

```
docker exec -it imersao_alura_agentes_ia_ambiente python3 comando.py --comando ajuda
```

E uma lista de comandos possíveis será aprensentado.

**Fazendo uma pergunta**

```
docker exec -it imersao_alura_agentes_ia_ambiente python3 comando.py --comando perguntar --pergunta "Qual a capital da França?"
```

**Verificando os modelos disponíveis pelo Google**

```
docker exec -it imersao_alura_agentes_ia_ambiente python3 comando.py --comando registrar_modelos_disponiveis
```

Este comando aciona a api do Google para listar os modelos disponíveis e salva no banco de dados relacional na tabela `modelos`, e detalhes dos modelos ficam armazenados na tabela `modelos_meta_dados`.


