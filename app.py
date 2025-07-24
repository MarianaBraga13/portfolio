from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__': # somente o main pode executar o app/ ou a essa função
    app.run(debug=True) # renderiza sempre que houver atualização
    
