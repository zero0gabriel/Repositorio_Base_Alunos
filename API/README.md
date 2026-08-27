Durante esta aula, o contrato inicial será:


| Método | Rota | Finalidade |
|---|---|---|
| `GET` | `/` | mensagem inicial |
| `GET` | `/api/status` | verificar a aplicação |
| `GET` | `/api/cursos` | listar cursos |
| `GET` | `/api/cursos/<id>` | consultar um curso específico |


A rota de listagem também aceitará filtros opcionais:


```text
/api/cursos?area=programacao&ativo=true
```