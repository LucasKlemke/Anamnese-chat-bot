# Anamnese Chat Bot

Bem-vindo ao projeto Anamnese Chat Bot! Este projeto é uma implementação em Python para interagir com a LLM gemini, responsável por realizar uma anamnese médica com base em um roteiro de anamnese ensinado a estudantes de universidades.

## Descrição

O Anamnese Chat Bot é um projeto desenvolvido em Python que utiliza a LLM Gemini para realizar anamneses médicas de forma automatizada. A anamnese é um processo essencial na prática médica, onde o profissional de saúde coleta informações detalhadas sobre o paciente para entender melhor suas condições de saúde e histórico médico.

## Estórias de Usuário

### Estória 1: Como usuário, quero iniciar uma conversa com a IA para realizar uma anamnese médica.
- **Critérios de Aceitação**:
  - O usuário pode iniciar uma conversa.
  - A IA segue o roteiro de anamnese médica.

### Estória 2: Como desenvolvedor, quero configurar a API key e o modelo da IA através de variáveis de ambiente.
- **Critérios de Aceitação**:
  - As variáveis `GEMINI_API_KEY` e `GEMINI_MODEL` são carregadas do arquivo `.env`.

## Fluxo de Trabalho no Git

1. **Branch Principal**: `main`
2. **Branches de Funcionalidade**: Para cada nova funcionalidade, crie uma branch a partir da `main` com o nome `feature/nome-da-funcionalidade`.
3. **Branches de Correção**: Para correções de bugs, crie uma branch a partir da `main` com o nome `fix/nome-da-correção`.
4. **Pull Requests**: Todas as branches devem ser integradas à `main` através de pull requests. As pull requests devem ser revisadas por pelo menos um outro desenvolvedor antes de serem mescladas.

## Itens de Configuração

- **Código Fonte**: Todos os arquivos `.py` no repositório.
- **Dependências**: Listadas no arquivo `requirements.txt`.
- **Variáveis de Ambiente**: Definidas no arquivo `.env`.
- **Documentação**: Arquivos `README.md` e `LICENSE`.

## Estratégia para Tags e Liberação de Releases

- **Tags**: Utilize tags semânticas no formato `vX.Y.Z`, onde `X` é a versão principal, `Y` é a versão secundária e `Z` é a versão de patch.
- **Releases**: Para cada nova versão estável, crie uma release no GitHub. Inclua notas de release detalhando as mudanças, novas funcionalidades e correções de bugs.

## Instalação

Para instalar a biblioteca, você pode usar o pip:

```sh
pip install -r requirements.txt
```

## Uso

Aqui está um exemplo básico de como usar a biblioteca:

```python
from gemini import GeminiClient

client = GeminiClient()
response = client.request('gemini://example.com')

print(response.content)
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.