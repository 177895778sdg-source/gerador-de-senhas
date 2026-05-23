import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def gerarsenha(tamanho, usar_maiusculas, usar_minusculas, usar_especiais, usar_numero):
    caracteres = ""
    
    if usar_especiais:
        caracteres += "!@#$%&*()_+-=[]}{|;:,.<>?"
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numero:
        caracteres += string.digits
        
    if not caracteres:
        return "Selecione ao menos uma opção!"

    return "".join(random.choice(caracteres) for _ in range(tamanho))


@app.route("/", methods=["GET", "POST"])
def index():
    senha_gerada = None

    if request.method == "POST":
        maiusculas = "maiusculas" in request.form
        minusculas = "minusculas" in request.form
        especiais = "caracteresespeciais" in request.form
        numeros = "numeros" in request.form
        
        
        try:
            tamanho = int(request.form.get("tamanho", 12))
        except (ValueError, TypeError):
            tamanho = 12

        senha_gerada = gerarsenha(tamanho, maiusculas, minusculas, especiais, numeros)
        
    return render_template("index.html", senha=senha_gerada)

if __name__ == "__main__":
    app.run(debug=True)
