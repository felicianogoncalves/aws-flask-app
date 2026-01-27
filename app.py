from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}, 200
    
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

# host="0.0.0.0" → permite acesso externo (necessário para Docker/EC2)
# port=5000 → porta interna do container
# debug=False → nunca usar debug=True em produção
