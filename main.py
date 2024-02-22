import requests

API_KEY = "c426dfa3ab9cd099ceb1a5b0bfc944ab"
cidade = input("Qual cidade quer saber a temperatura? ")
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic ["weather"][0]["description"]
temperatura = requisicao_dic["main"]["temp"] - 273.15
sensacao_termica = requisicao_dic["main"]["feels_like"] - 273.15
minima = requisicao_dic["main"]["temp_min"] - 273.15
maxima = requisicao_dic["main"]["temp_max"] - 273.15
print(f"{cidade}", f"{temperatura:.2f}°C", descricao)
print(f"Sensação térmica de {sensacao_termica:.2f}°C")
print(f"Mínima {minima:.2f}°C", f"Máxima {maxima:.2f}°C")
