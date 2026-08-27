# Exercício Prático — Rotas com Flask

## Objetivo

Neste exercício, você irá criar uma aplicação Flask com várias rotas simples.

O objetivo é praticar:

- criação de rotas com `@app.route()`;
- uso do método `GET`;
- parâmetros na URL;
- conversores como `<string:nome>` e `<int:numero>`;
- operações matemáticas;
- estruturas condicionais;
- retorno de informações para o usuário.

> **Importante:** tente resolver cada rota sozinho antes de pedir ajuda à IA ou consultar uma solução pronta.

---

## Preparação do projeto

Crie uma pasta para o exercício e, dentro dela, um arquivo chamado:

```text
app.py
```

Instale o Flask:

```bash
pip install flask
```

Comece sua aplicação com a estrutura básica:

```python
from flask import Flask

app = Flask(__name__)

# Crie suas rotas aqui

if __name__ == "__main__":
    app.run(debug=True)
```

Execute o programa:

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

# Rotas obrigatórias

Implemente as rotas abaixo na ordem apresentada.

## 1. Olá, mundo!

### Rota

```http
GET /
```

### Objetivo

Ao acessar a página inicial, exiba:

```text
Olá, mundo!
```

### Exemplo

```text
http://127.0.0.1:5000/
```

---

## 2. Cumprimento personalizado

### Rota

```http
GET /api/cumprimento/<string:nome>
```

### Objetivo

Receba um nome pela URL e devolva uma mensagem de cumprimento.

### Exemplo

Requisição:

```text
http://127.0.0.1:5000/api/cumprimento/Ana
```

Resposta esperada:

```text
Olá, Ana!
```

> No Flask, o conversor para texto é `string`, portanto usamos `<string:nome>`.

---

## 3. Soma de dois números

### Rota

```http
GET /api/soma/<int:num1>/<int:num2>
```

### Objetivo

Receba dois números inteiros, realize a soma e mostre o resultado.

### Exemplo

Requisição:

```text
http://127.0.0.1:5000/api/soma/10/5
```

Resposta esperada:

```text
A soma de 10 + 5 é 15.
```

---

## 4. Subtração de dois números

### Rota

```http
GET /api/subtracao/<int:num1>/<int:num2>
```

### Objetivo

Receba dois números inteiros e devolva o resultado da subtração:

```text
num1 - num2
```

### Exemplo

```text
/api/subtracao/20/7
```

Resultado esperado:

```text
A subtração de 20 - 7 é 13.
```

---

## 5. Dobro de um número

### Rota

```http
GET /api/dobro/<int:numero>
```

### Objetivo

Receba um número inteiro e devolva o dobro dele.

### Exemplo

```text
/api/dobro/8
```

Resposta esperada:

```text
O dobro de 8 é 16.
```

---

## 6. Par ou ímpar

### Rota

```http
GET /api/par-ou-impar/<int:numero>
```

### Objetivo

Receba um número inteiro e informe se ele é **par** ou **ímpar**.

### Exemplos

```text
/api/par-ou-impar/10
```

Resposta:

```text
10 é par.
```

```text
/api/par-ou-impar/7
```

Resposta:

```text
7 é ímpar.
```

### Dica

Pense em como o operador `%` pode ajudar nessa verificação.

---

## 7. Maior número

### Rota

```http
GET /api/maior/<int:num1>/<int:num2>
```

### Objetivo

Receba dois números e informe qual deles é o maior.

### Exemplo

```text
/api/maior/15/9
```

Resposta esperada:

```text
15 é o maior número.
```

### Atenção

O que deve acontecer se os dois números forem iguais?

Exemplo:

```text
/api/maior/10/10
```

Crie uma resposta adequada para esse caso.

---

## 8. Tabuada

### Rota

```http
GET /api/tabuada/<int:numero>
```

### Objetivo

Receba um número inteiro e gere sua tabuada de `1` até `10`.

Exemplo:

```text
/api/tabuada/5
```

A resposta deve apresentar:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

### Dica

Você pode utilizar um laço `for` para gerar os resultados.

---

# Checklist

Antes de considerar o exercício concluído, verifique se:

- [ ] A aplicação Flask inicia sem erros.
- [ ] A rota `/` funciona.
- [ ] As oito rotas foram implementadas.
- [ ] Os parâmetros da URL estão sendo recebidos corretamente.
- [ ] As rotas numéricas utilizam `<int:...>`.
- [ ] A rota de par ou ímpar utiliza uma condição.
- [ ] A rota de maior número trata números iguais.
- [ ] A tabuada apresenta resultados de 1 até 10.
- [ ] Você testou todas as rotas no navegador ou no REST Client.

---

# Desafio extra

Depois que todas as rotas estiverem funcionando, escolha **três rotas** e altere suas respostas para JSON.

Por exemplo, em vez de:

```text
A soma de 10 + 5 é 15.
```

pense em uma resposta semelhante a:

```json
{
  "num1": 10,
  "num2": 5,
  "resultado": 15
}
```

Pesquise como retornar um `dict` ou utilizar `jsonify()` no Flask.

---

## Regra do exercício

Antes de pesquisar uma solução completa, tente seguir esta sequência:

1. Identifique quais dados entram pela URL.
2. Pense no processamento necessário.
3. Defina qual deve ser a resposta.
4. Implemente a função da rota.
5. Teste com pelo menos dois valores diferentes.
6. Só então consulte documentação ou peça ajuda.
