import requests
from bs4 import BeautifulSoup
import time


ativo = input("Digite o código do ativo (ex: mxrf11): ").lower()


headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:
    url = f"https://investidor10.com.br/fiis/{ativo}/"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            preco = soup.find("span", class_="value")

            if preco:
                print(f" Preço do {ativo.upper()}: {preco.text.strip()}")
            else:
                print(" Não encontrou o preço (layout pode ter mudado)")
        else:
            print(" Erro ao acessar o site")

    except Exception as e:
        print(f" Erro: {e}")

    print(" Atualizando em 60 segundos\n")
    time.sleep(60)