import requests
import os
API_URL = "https://api-inference.huggingface.co/models/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
api_key = os.environ['api_key']
headers = {"Authorization": api_key}
print(headers)
def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()


def api_loader(financial_text):
  dict = {"inputs":financial_text}
  txt = query(dict)
  return txt
  