from flask import Flask, url_for, render_template

# inicialização (no topo)
app = Flask(__name__)

#rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilerme", "membro_ativo": True},
        {"nome": "Joao", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False},     
    ]
    
    return render_template("index.html", titulo = titulo, usuarios = usuarios)

@app.route("/sobre")
def pagina_sobre():
    return "sobre"



#execução (no fim)
app.run(debug=True)