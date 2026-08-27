from flask import Flask, jsonify

app = Flask(__name__)  # Criando app (nossa api)

cursos = [
    {
        "id": 1,
        "nome": "Python",
        "area": "programacao",
        "carga_horaria": 40,
        "ativo": True,
    },
    {
        "id": 2,
        "nome": "Inglês",
        "area": "linguas",
        "carga_horaria": 30,
        "ativo": True,
    },
    {
        "id": 3,
        "nome": "Matemática",
        "area": "ciencias",
        "carga_horaria": 40,
        "ativo": True,
    },
]

@app.get("/")  # Caminho endereço
def inicio():
    return "Hello, World!"


@app.get("/api/status")
def status():
    return jsonify({
        "status": "online",
        "mensagem": "A API está funcionando."
    })


@app.get("/api/cursos")
def get_cursos():
    return jsonify(cursos)

@app.get("/api/cursos/<int:id>")
def get_curso(id):
    for curso in cursos:  # Percorro os cursos, o curso do momento fica na variável "curso"
        if curso["id"] == id:
            return jsonify(curso)

    return jsonify({"mensagem": "Curso não encontrado."}), 404
app.run(debug=True, use_reloader=False)  # Roda a nossa API