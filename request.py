import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Pclass':0, 'Age':12, 'SibSp':0, 'Fare':15})

print(r.json())