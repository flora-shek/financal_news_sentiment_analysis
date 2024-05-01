from flask import Flask, render_template,jsonify
from api import api_loader
from example import text
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template(
        "index.html")

@app.route("/api/<financial_text>")
def api(financial_text):
  f_txt = api_loader(financial_text)
  return jsonify(f_txt)
  
@app.route("/example/<example>")
def examples(example):
  if example=="1":
    return render_template("index.html",text = text[0])
  elif example == "2":
     return render_template("index.html",text = text[1])
  else:
    return render_template("index.html",text = text[2])
@app.route("/result",methods=['post'])
def result():
  token = request.form.get('')
  
  return render_template("index.html")
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4080,debug=True)


