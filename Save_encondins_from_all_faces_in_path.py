import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import shutil
import os
import pickle

enc_rosto = {}

# img = face_recognition.load_image_file(r'C:\Users\Matriz\Documents\rostos_vouga\210520193\ss1\frame388.jpg')

# r_encoding = face_recognition.face_encodings(img)
# r_encoding2 = r_encoding[0]
# print(r_encoding2)


#encontrei algum problema depois de recorta algumas faces e tentar analisa-las depois. Algumas fotos não sao reconhecidas
#esse scritp, tentará pegar as fotos que ja foram rechecadas, salvar os encondings e compara-las para saber quantas pessoas diferentes frequetaram.

#esta pasta são os rostos rechedados
#premissa desse scritp é que só há uma foto em cada arquivo. Nao há necessidade de contar as faces

path2 = r'C:\Users\Matriz\Documents\rostos_vouga\210520193\ss1'
ffiles = []
# r=root, d=directories, f = files
for fr, fd, ff in os.walk(path2):
    for ffile in ff:
        if '.jpg' in ffile:
            ffiles.append(os.path.join(fr, ffile))
    print(ff)

for rosto_averificar in ffiles:

    rosto_loop = face_recognition.load_image_file(rosto_averificar)
    # print("rosto loop é" ,rosto_loop)
    # print("rosto a verificar é " ,rosto_averificar)
    # #melhora capacidade de ler a imagem, aumentando seu tamanho
    #localizacoes_faces = face_recognition.face_locations(rosto_loop, number_of_times_to_upsample=2)
    encodings_rosto_averificar = face_recognition.face_encodings(rosto_loop)
  #  print("esse e o encodings_rosto_averificar", encodings_rosto_averificar)
    econding_rosto_verificado = encodings_rosto_averificar [0]
 #   print("econding_rosto_verificado", econding_rosto_verificado)
    enc_rosto[rosto_averificar] =econding_rosto_verificado
    #enc_rosto.append(econding_rosto_verificado)
    
print(enc_rosto)
print(len(enc_rosto))

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(enc_rosto, f)