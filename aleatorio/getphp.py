import requests

req = requests.get("http://localhost/Aula/exer4.php")

print(req.text)
