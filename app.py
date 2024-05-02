from flask import Flask, render_template,jsonify,request
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
  token = request.form.get('floatingTextarea')
  result = api_loader(token)
  label1 = result[0][0]['label'].capitalize()
  label2 =  result[0][1]['label'].capitalize()
  label3 = result[0][2]['label'].capitalize()
  score1 = round((result[0][0]['score']*100),2)
  score2 = round((result[0][1]['score']*100),2)
  score3 = round((result[0][2]['score']*100),2)
  return render_template("index.html",result = result,s1=score1,s2=score2,s3=score3,sentence = token,l1=label1,l2=label2,l3=label3)

@app.route("/signin")
def signin():
  return render_template("signin.html")
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4080,debug=True)


