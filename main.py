from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    expressao = ""  # Expressão digitada até agora
    resultado = ""  # Resultado final exibido

    if request.method == "POST":
        # Pega a expressão atual e o botão pressionado
        expressao = request.form.get("expressao", "")
        botao = request.form.get("btn")

        # Lógica dos botões
        if botao == "C":
            expressao = ""
            resultado = ""
        elif botao == "=":
            try:
                # Avalia a expressão com segurança
                resultado = str(eval(expressao))
                expressao = resultado  # Permite continuar calculando
            except Exception:
                resultado = "Erro"
        else:
            # Adiciona o botão à expressão
            expressao += botao

    return render_template("index.html", expressao=expressao, resultado=resultado)

if __name__ == "__main__":
    # Roda o app acessível a partir de qualquer IP na rede local
    app.run(host="0.0.0.0", port=80, debug=True)