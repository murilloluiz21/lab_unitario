### PROJETO LAB FINAL

### Foi criado um laboratório de Desenvolvimento da Faculdade, onde são realizados experimentos, práticas e implementações utilizando diversas tecnologias modernas no ínicio do semestre e foi se aprimorando a cada nova atividade com a finalidade de termos uma base melhor de como funcíona o github em prática.

### Tecnologias utilizadas

# Python 
*Criação de APIs e scripts.*
*Testes unitários com pytest.*
*Manipulação de arquivos JSON, YAML e outros formatos.*

*EXEMPLO:*
pyTest

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "API is running"}

def test_login(client):
    response = client.post('/login')
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected_no_token(client):
    response = client.get('/protected')
    assert response.status_code == 401

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_carregar_mensagem():
    assert carregar_mensagem() == "Hello, Lab!"

### Node.js & NPM
*Execução de scripts.*
*Uso de bibliotecas externas.*
*Suporte para automação e integração.*

*EXEMPLO:*
NPM
{
  "swagger": "2.0",
  "info": {
    "title": "InovaTech API",
    "version": "1.0",
    "description": "Documentação da API do laboratório de criação de APIs"
  },

## YAML / YML
*Configurações de pipelines CI/CD.*
*Arquivos de configuração (GitHub Actions, Docker Compose, etc).*

*EXEMPLO:*
Yaml
name: Python CI
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run pytest
        run: pytest -q

### Swagger / OpenAPI
*Documentação de endpoints.*
*Testes e validação de rotas de APIs.*

*EXEMPLO:*
Swagger
{
  "swagger": "2.0",
  "info": {
    "title": "InovaTech API",
    "version": "1.0",
    "description": "Documentação da API do laboratório de criação de APIs"
  },

### JSON
*Configurações do sistema.*
*Troca de dados entre APIs.*

*EXEMPLO:*
Json
def test_config_json_valido():
    with open("config.json", "r") as f:
        data = json.load(f)

    # Verifica chaves
    assert "version" in data
    assert "enabled" in data
    assert "name" in data

### ESTRUTURA DO PROEJTO
*O PROJETO TEM PARTICIPAÇÃO DE PASTAS COMO:*

 projeto-lab
 src # Código-fonte principal
 tests # Testes unitários
 static # Arquivos estáticos (HTML, CSS, JS)
 .github/workflows # Pipelines em YML
 requirements.txt # Dependências Python
 package.json # Dependências Node.js
 swagger.yaml # Documentação da API
 README.md # Documentação

### FUNCIONALIDADES IMPLEMENTADAS:

# Alguns dos recursos comumente trabalhados no laboratório:
# Desenvolvimento de APIs com Python.
# Criação e execução de testes automatizados.
# Configuração de Workflows com GitHub Actions.
# Validação de arquivos JSON e YAML.
# Uso de Swagger para documentar APIs.
# Automatização de processos com Node.js.

# WORKFLOWS EM GITACTIONS

# A automação ocorre através de workflows em .github/workflows, normalmente com:
name: Python CI
on: [push]


jobs:
test:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Instalar dependências
run: pip install -r requirements.txt
- name: Rodar testes
run: pytest -q

## Documentação da API (Swagger)

## A API pode ser documentada utilizando swagger.yaml ou openapi.json. Para visualizar:
*Use uma ferramenta como:*
Swagger Editor
Swagger UI
Insomnia
Postman

# DEPENDENCIAS E INSTALAÇÃO

*Instalar dependências Python:*
pip install -r requirements.txt

*Instalar dependências Node:*
npm install

## CONCLUSÃO

*Este laboratório serve como ambiente de aprendizado para integração de tecnologias modernas, práticas de código limpo, testes automatizados e documentação de APIs. O objetivo é preparar o aluno para cenários reais de desenvolvimento.*