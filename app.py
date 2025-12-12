from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=80, debug=False)

#host="0.0.0.0" → permite acesso de fora da própria máquina (senão só aceita localhost)
#port=80 → porta padrão do HTTP
#debug=False → nunca usar debug=True em produção (segurança!)