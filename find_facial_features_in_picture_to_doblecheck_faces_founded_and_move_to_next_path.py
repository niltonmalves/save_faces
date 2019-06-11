from PIL import Image, ImageDraw
import face_recognition
import os
import shutil

###tentar fazer um loop para re-checar se há rosto nesta foto previamente recortada

path = r'C:\Users\Matriz\Documents\teste_verif_rosto_em_pasta\posicao_inicial'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
        print(file)

for indice ,f   in enumerate(files):
    print(f)



    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(f)

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    if len(face_landmarks_list) > 0:
        
        # Create a PIL imagedraw object so we can draw on the picture
        # pil_image = Image.fromarray(image)
        # d = ImageDraw.Draw(pil_image)

        # for face_landmarks in face_landmarks_list:

            # # Print the location of each facial feature in this image
            # for facial_feature in face_landmarks.keys():
                # print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

            # # Let's trace out each facial feature in the image with a line!
            # for facial_feature in face_landmarks.keys():
                # d.line(face_landmarks[facial_feature], width=5)

        # # Show the picture
        # pil_image.show()
        shutil.move(f,r"C:\Users\Matriz\Documents\teste_verif_rosto_em_pasta\posicao_final")
    else:
        print("nao tinha rosto, mover para pasta de falha apos re-checagem")
        shutil.move(f,r"C:\Users\Matriz\Documents\teste_verif_rosto_em_pasta\rosto_com_falha_apos_recheck")
        next
        
#verifiquei que esse codigo ira travar quando a pasta de destino tem arquivo com mesmo nome
#para resolver podemos acrescentar um timestamp do rosto criado