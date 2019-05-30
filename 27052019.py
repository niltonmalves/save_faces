import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import shutil
import os

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.
# Load a sample picture and learn how to recognize it.

path2 = r'C:\Users\Matriz\Documents\rostos_vouga\21052019'

ffiles = []
# r=root, d=directories, f = files
for fr, fd, ff in os.walk(path2):
    for ffile in ff:
        if '.jpg' in ffile:
            ffiles.append(os.path.join(fr, ffile))
    print(ff)
    
    for rosto_averificar in ffiles:
          
        rosto_loop = face_recognition.load_image_file(rosto_averificar)
        print("este é rosto_loop", rosto_loop)
        print("este é rosto_averificar", rosto_averificar)
        localizacoes_faces = face_recognition.face_locations(rosto_loop, number_of_times_to_upsample=2)
        print("esse é o localizacoes_faces", localizacoes_faces)
        encodings_rosto_averificar = face_recognition.face_encodings(rosto_loop, known_face_locations=localizacoes_faces)
        print("esse é o encodings_rosto_averificar", encodings_rosto_averificar)

        if len(encodings_rosto_averificar) == 0:
            #no face found in the image
            print("sem rostos na imagem no primeiro loop")
            shutil.move(rosto_averificar,r'C:\Users\Matriz\Documents\rostos_vouga\sem_rosto')
        else:
            print("fazendo busca")
            
            
             



            #obama_image = face_recognition.load_image_file(rosto_averificar)
            #obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
            known_face_encodings = [
                encodings_rosto_averificar
            ]
            known_face_names = [
                "cliente5"
            ]
            shutil.move(rosto_averificar,r'C:\Users\Matriz\Documents\rostos_vouga\tt')
        # Create arrays of known face encodings and their names

        #criar lista com todos os aquivos da pasta a ser examinada

        #pegar os rostos e comparar se tem algum igual dessa lista
        #tendo rosto repetido, criar e colocar em pasta separada.
            path = r'C:\Users\Matriz\Documents\rostos_vouga\21052019'

            files = []
            # r=root, d=directories, f = files
            for r, d, f in os.walk(path):
                for file in f:
                    if '.jpg' in file:
                        files.append(os.path.join(r, file))
                print(f)


            # fazer loop na lista de arquivos de rostos




                for rosto_desconhecido in files:
                    
                    


                    # Store configuration file values
                    # Keep presets
                    # Load an image with an unknown face
                    unknown_image = face_recognition.load_image_file(rosto_desconhecido) 

                    # Find all the faces and face encodings in the unknown image
                    face_locations = face_recognition.face_locations(unknown_image)
                    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
                    print(encodings_rosto_averificar)
                    print(face_encodings)

                 #   matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
#                    if matches:
#                        shutil.move(rosto_desconhecido,r"C:\Users\Matriz\Documents\rostos_vouga\210520193\ss1")
 #                   else:
 #                       print("rosto não é igual")
                        


                    # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
                    # See http://pillow.readthedocs.io/ for more about PIL/Pillow
                    #  pil_image = Image.fromarray(unknown_image)
                    # Create a Pillow ImageDraw Draw instance to draw with
                    #  draw = ImageDraw.Draw(pil_image)

                    # Loop through each face found in the unknown image
                    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                        
                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        #matches = face_recognition.compare_faces(encodings_rosto_averificar, face_encoding)

                        

                        name = "Unknown"

                        # If a match was found in known_face_encodings, just use the first one.
                        # if True in matches:
                        #     first_match_index = matches.index(True)
                        #     name = known_face_names[first_match_index]

                        # Or instead, use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches:

                        #if matches[best_match_index]:
                         #   name = known_face_names[best_match_index]
                            #recorta o arquivo da pasta de desconhecido e cola na pasta de conhecidos
                            
                            shutil.move(rosto_desconhecido,r"C:\Users\Matriz\Documents\rostos_vouga\210520193\ss1")

                        # Draw a box around the face using the Pillow module
                    #     draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

                        # Draw a label with a name below the face
                    #    text_width, text_height = draw.textsize(name)
                     #   draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
                     #   draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


                    # Remove the drawing library from memory as per the Pillow docs
                    # del draw

                    # Display the resulting image
                    # pil_image.show()

                    # You can also save a copy of the new image to disk if you want by uncommenting this line
                    # pil_image.save("image_with_boxes.jpg")
         #else:
          #   print("No faces found in the image!")
           #  next()
        
