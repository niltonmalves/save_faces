import face_recognition
import os
import shutil
#este script sera para pegar o arquivo da imagem que contem apenas 1 rosto e compra-los com todos os outros rostos.
#tem algum erro na logica desses loops que algumas criacoes de pastas e transferencias estao erradas

files = []
path = r'C:\Users\Matriz\Documents\teste_verif_rosto_em_pasta\posicao_final'

for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

            path = r'C:\Users\Matriz\Documents\teste_verif_rosto_em_pasta\posicao_final'
            files = []
            # r=root, d=directories, f = files

            for r, d, f in os.walk(path):
                print("este é r:",r)
                print("este é d:",d)
                print("este é f:",f)
                for file in f:
                    if '.jpg' in file:
                        files.append(os.path.join(r, file))
                    print(file)



            print("este é f:",f)
            print("este é files:",files)     
            print("este é file:",file)

            biden_image = face_recognition.load_image_file(files[0])
            lista_temp =[]
            lista_temp.append(files[0])
            print("lista_temp", lista_temp)
            del(files[0])

            print("este é o files, depois deletar", files)



            for indice, rt in enumerate(files):
                
                print("este e o rt:",rt)
                # Load the jpg files into numpy arrays
                
                unknown_image = face_recognition.load_image_file(rt)

                # Get the face encodings for each face in each image file
                # Since there could be more than one face in each image, it returns a list of encodings.
                # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
                try:
                    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
                    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
                except IndexError:
                    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
                    quit()

                known_faces = [
                    biden_face_encoding
                    
                ]
                # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
                results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

                # print("este é o :known_faces",known_faces )
                # print("este é o : biden_face_encoding",  biden_face_encoding)
                # print("este é o :biden_image",biden_image )
                # print("este é o :unknown_image",unknown_image )
                print("este é o results:", results)
                if results[0]:
                    print("Ok")
                    
                    path2 = "/Users/Matriz/Documents/teste_verif_rosto_em_pasta/posicao_final/rostos_catalogados/xx%d" % indice
                    try:
                        os.makedirs(path2)
                    except OSError:
                        print ("Creation of the directory %s failed" % path2)
                    else:
                        print ("Successfully created the directory %s" % path2)
                    shutil.move(rt, path2)
                else:
                    print("not ok")
                    
            shutil.move(lista_temp[0],path2)

            print("este é o files depois do loop:", files)
            
