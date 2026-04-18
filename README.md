# Desafio: Trabalhador e Aposentadoria

Desafio que calcula elegibilidade para aposentadoria baseado em idade e tempo de contribuiÃ§Ã£o.

## ðŸŽ¯ DescriÃ§Ã£o

ExercÃ­cio de lÃ³gica que implementa regras de cÃ¡lculo de aposentadoria, considerando idade mÃ­nima, tempo de contribuiÃ§Ã£o e legislaÃ§Ã£o previdenciÃ¡ria.

## ðŸ› ï¸ Tecnologias Utilizadas

- **Python 3** - Linguagem de programaÃ§Ã£o

## ðŸš€ ExecuÃ§Ã£o

`ash
# Executar o desafio
python desafio_aposentadoria.py
`

## ðŸ“‹ Funcionalidades

- Cadastro de trabalhador
- CÃ¡lculo de tempo de contribuiÃ§Ã£o
- ValidaÃ§Ã£o de elegibilidade para aposentadoria
- Estimativa de benefÃ­cio
- RelatÃ³rio de status previdenciÃ¡rio

## ðŸ’¡ Exemplo

`python
trabalhador = Trabalhador("Maria", data_nascimento, tempo_contribuicao)
if trabalhador.pode_aposentar():
    print("ElegÃ­vel para aposentadoria")
else:
    anos_faltando = trabalhador.anos_ate_aposentadoria()
`

---
