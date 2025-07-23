from flask import Flask

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Mariana Braga Domingues - Estudante de Engenharia da Computação"

if __name__ == '__main__': # somente o main pode executar o app/ ou a essa função
    app.run(debug=True) # renderiza sempre que houver atualização
    
