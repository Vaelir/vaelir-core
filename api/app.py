from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota inicial
@app.route('/')
def home():
    return "Bem-vindo à Vaelir API!"

# Endpoint para receber comandos
@app.route('/comando', methods=['POST'])
def receber_comando():
    # Obter o comando do corpo da requisição
    comando = request.json.get('comando')

    # Aqui você pode processar o comando e fazer algo com ele
    if comando == 'despertar':
        resposta = "Vaelir está despertando..."
    else:
        resposta = "Comando não reconhecido."

    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
