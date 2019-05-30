import os
import cv2
import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import shutil


#pegar os rostos e comparar se tem algum igual dessa lista
#tendo rosto repetido, criar e colocar em pasta separada.
path = r'C:\Users\Matriz\Documents\rostos_vouga\ss\210520193'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

for indice ,f   in enumerate(files):
    print(f)

    encodings = face_recognition.face_encodings(f)
    if len(encodings) > 0:
        
    

        pasta = "/Users/Matriz/Documents/rostos_vouga/qq2/know_faces/xx%d" % indice
        try:
            os.makedirs(pasta)
        except OSError:
            print ("Creation of the directory %s failed" % pasta)
        else:
            print ("Successfully created the directory %s" % pasta)

        
        obama_image = face_recognition.load_image_file(f)
        
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        
            
            
        known_face_encodings = [obama_face_encoding]

        known_face_names = ["cliente%d" % indice]
        print(indice)
        for un in reversed(files):
            print('loop procurando rosto', un)
                    # Load an image with an unknown face
            unknown_image = face_recognition.load_image_file(un)
                    # Find all the faces and face encodings in the unknown image
            face_locations = face_recognition.face_locations(unknown_image)
            face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                        # If a match was found in known_face_encodings, just use the first one.
                        # if True in matches:
                        #     first_match_index = matches.index(True)
                        #     name = known_face_names[first_match_index]

                        # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                            #recorta o arquivo da pasta de desconhecido e cola na pasta de conhecidos
                            
                    shutil.move(un,pasta)

                

    else:
       print("No faces found in the image!")
       next


