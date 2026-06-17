# 🐍 Desafio: Cadastro de Trabalhador e Aposentadoria em Python

Repositório dedicado ao desenvolvimento de um sistema em Python para cadastrar dados de um trabalhador e calcular, com base na idade de contratação e no tempo de contribuição, com quantos anos ele poderá dar entrada em sua aposentadoria.

---

## 🚀 Tecnologias Utilizadas

* **Python 3** (Lógica estruturada, manipulação de coleções e operações de data)
* **Visual Studio Code** ou IDE de preferência

---

## 📂 Estrutura do Repositório

O projeto conta com uma organização direta e profissional:

* **`desafio_trabalhador_aposentadoria.py`**: Script contendo o fluxo completo de interação, processamento e apresentação das regras do trabalhador.
* **`README.md`**: Documentação de apresentação do projeto.

---

## 🎮 Funcionamento do Sistema

O programa realiza a leitura sequencial e o tratamento dos seguintes dados:
1. **Dados Pessoais**: Nome, Ano de Nascimento (usado para calcular a Idade Atual) e o número da Carteira de Trabalho (CTPS).
2. **Condicional de Emprego**: Se a CTPS for informada (diferente de zero), o sistema solicita:
   * Ano de Contratação.
   * Salário atual.
3. **Métrica Previdenciária**: Utilizando como base um tempo padrão de contribuição (comumente 35 anos no modelo clássico deste desafio de lógica), o algoritmo calcula e adiciona de forma exata com que idade o cidadão irá se aposentar.
4. **Exibição**: Todos os dados coletados e calculados são impressos de forma organizada no terminal.

---

## 🧠 Conceitos Praticados e Aprendizados

A elaboração deste projeto proporcionou a fixação de fundamentos de arquitetura de dados e regras de negócio:

* **Dicionários (`dict`)**: Uso dessa estrutura essencial para armazenar os dados do trabalhador de forma mapeada via chaves e valores (`'nome'`, `'idade'`, `'ctps'`).
* **Manipulação e Cálculo com Datas**: Obtenção do ano corrente e subtração do ano de nascimento para gerar a idade real e estimativas futuras de tempo.
* **Estruturas Condicionais**: Validação se o indivíduo possui ou não registro de trabalho ativo para ramificar as perguntas exibidas no terminal.
* **Lógica de Governança de Dados**: Organização de informações cadastrais para que o resultado final reflita de forma fidedigna os dados do segurado analiticamente.

---
Desenvolvido com 💻 focado na construção de scripts lógicos e análise de dados cadastrais com Python!
