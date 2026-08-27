# 🎬 Projeto de Banco de Dados - Análise de Filmes

## 📋 Descrição do Projeto
Este projeto consiste na criação e manipulação de um banco de dados SQLite contendo informações sobre filmes, diretores, gêneros e avaliações. Os alunos foram contratados para implementar e analisar os dados cinematográficos.

## 🗄️ Estrutura do Banco de Dados

### Tabela `filmes`
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| id | INTEGER | Chave primária (auto increment) |
| titulo | TEXT | Título do filme |
| genero | TEXT | Gênero cinematográfico |
| ano_lancamento | INTEGER | Ano de lançamento |
| duracao_minutos | INTEGER | Duração em minutos |
| diretor | TEXT | Nome do diretor |
| nota_imdb | REAL | Avaliação no IMDb |

## 🎯 Objetivos do Projeto

Os alunos devem criar queries SQL para responder às seguintes perguntas de negócio:

### 📊 Análises Solicitadas

1. **Filmes do Christopher Nolan**
2. **Filmes do James Gunn** 
3. **Filmes de ação lançados em 2016**
4. **Filmes do Batman e seus diretores**
5. **Filmes de terror e drama (1980-2002)**
6. **Quantidade de filmes lançados em 1999**
7. **Quantidade de filmes do Quentin Tarantino**
8. **Filmes do James Cameron e seus gêneros**
9. **Adicionar filme favorito do aluno**
10. **Adicionar filme que o professor odeia**
11. **Deletar filme que o professor detesta**

## 💾 Scripts SQL

### Criação da Tabela
```sql
CREATE TABLE filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT,
    ano_lancamento INTEGER,
    duracao_minutos INTEGER,
    diretor TEXT,
    nota_imdb REAL
);
```

### Inserção de Dados
```sql
-- Exemplo de inserção (100 filmes incluídos no projeto)
INSERT INTO filmes (titulo, genero, ano_lancamento, duracao_minutos, diretor, nota_imdb) VALUES
('O Poderoso Chefão', 'Drama', 1972, 175, 'Francis Ford Coppola', 9.2),
('Matrix', 'Ficção Científica', 1999, 136, 'Lana Wachowski', 8.7),
-- ... (demais filmes)
```



## 🛠️ Tecnologias Utilizadas

- **SQLite** - Banco de dados
- **DB Browser for SQLite** - Interface gráfica
- **SQL** - Linguagem de consulta

## 📈 Habilidades Desenvolvidas

- ✅ Criação e manipulação de tabelas SQL
- ✅ Inserção de dados em massa
- ✅ Consultas SELECT com filtros complexos
- ✅ Operadores LIKE, BETWEEN, IN
- ✅ Funções agregadas (COUNT)
- ✅ Operações DELETE e INSERT
- ✅ Análise de dados cinematográficos

