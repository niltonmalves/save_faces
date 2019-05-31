import shutil
import os
import cv2
from PIL import Image
import face_recognition
import random

#cria lista com nome dos arquivos dos frames da pasta que irá retirar os rostos
#problema desse scritp é que a nomenclatura que consegui colocar nos arquivos esta muito estranha.
#poderia tentar uma nomenclatura que pudesse indicar quando foi feita a foto para poder localiza-lo

#path = r'C:\Users\Matriz\Documents\frames_vouga\210520192'
path = r'C:\Users\Matriz\Documents\frames_vouga\teste_salvarRostosDeTodosFramesEmPasta\frames_originais'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
for f in reversed(files):
    print(f)

#quantidade de frames à verificar
#frm = len(f)

#for i in range(1, frm):
    # Load the jpg file into a numpy array

#    wed = r"C:\Users\Matriz\Documents\frames_vouga\qq2\frame (%d).jpg" % i
#    print("pagina", i)
    image = face_recognition.load_image_file(f)
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    counte=random.randint(1,1000)

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
#        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]        
##        pil_image = Image.fromarray(face_image)            
##        pil_image.show()       
        image_to_write = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
##        paginas =len(face_locations)
        for count in range(0, len(face_locations)):
            #cv2.imwrite(r"C:\Users\Matriz\Documents\rostos_vouga\210520192\fr%dame%d.jpg" % (counte, count ) , image_to_write )
            cv2.imwrite(r"C:\Users\Matriz\Documents\frames_vouga\teste_salvarRostosDeTodosFramesEmPasta\rostos_dos_frames\fr%dame%d.jpg" % (counte, count ) , image_to_write )
            for xy in range(10000):
                counte = random.randint(1,1000)
    if face_locations:
        #shutil.move(f, r"C:\Users\Matriz\Documents\frames_vouga\frames_com_rostos_encontrados")
        shutil.move(f, r"C:\Users\Matriz\Documents\frames_vouga\teste_salvarRostosDeTodosFramesEmPasta\frames_com_rostos_encontrados")
    print("Novo loop, abrindo novo frame")      
  #  frm = frm + paginas
