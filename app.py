from flask import Flask, render_template,jsonify
from api import api_loader
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template(
        "index.html")

@app.route("/api/<financial_text>")
def api(financial_text):
  f_txt = api_loader(financial_text)
  return jsonify(f_txt)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4080,debug=True)