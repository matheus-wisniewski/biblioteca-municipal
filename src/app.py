from flask import Flask, jsonify
# import requests

app = Flask(__name__) # Cria a instância da aplicação

@app.route("/") # Cria a rota raiz do projeto que é GET por padrão.
def hello_world():
    return 'Hello World!'

@app.route("/api/")
def api_hello_world():
    return jsonify({'mensagem': 'Hello World!'})

# @app.route("/api/teste")
# def teste_api():
#     url = 'https://thronesapi.com/api/v2/Characters/3'
#     r = requests.get(url)
#     return r.content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
