#tirar foto com telegram
from requests import post,get
from os import system
import datetime
import time
time.sleep(90)

# parâmetros iniciais do Telegram
chave = "1349821924:AAGaRakV1dCylqSAr3LER2xsyEY30FhZ05U"
#lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
id_da_conversa = "1153727310"
endereco_base = "https://api.telegram.org/bot" + chave

proximo_id_de_update = 0
def tira_foto():
    endereco = endereco_base + "/sendPhoto"
    dados = {"chat_id": id_da_conversa} 
    agora=datetime.datetime.now()
    hora= agora.strftime("%D_%H:%M:%S")
    i=0
    while(i<3):
      i = i + 1
      system(f"fswebcam --resolution 640x480  fotos{i}_{agora.day}{agora.month}{agora.year}{agora.strftime('%H%M%S')}.jpg")
      arquivo = {"photo": open(f"fotos{i}_{agora.day}{agora.month}{agora.year}{agora.strftime('%H%M%S')}.jpg", "rb")} 
      resposta = post(endereco, data=dados, files=arquivo)
while True:
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update} 
    resposta = get(endereco, json=dados) 
    dicionario_da_resposta = resposta.json()
    for resultado in dicionario_da_resposta["result"]: 
      mensagem = resultado["message"]
      if "text" in mensagem:
          if mensagem['text']== 'Tfoto':
             tira_foto()
             print(mensagem)
      proximo_id_de_update = resultado["update_id"] + 1 
    