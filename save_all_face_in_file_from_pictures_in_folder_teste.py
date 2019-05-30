from PIL import Image
import face_recognition
import cv2
import random

#quantidade de frames à verificar
frm = 600

for i in range(1, frm):
    # Load the jpg file into a numpy array

    wed = r"C:\Users\Matriz\Documents\frames_vouga\qq2\frame (%d).jpg" % i
    print("pagina", i)
    image = face_recognition.load_image_file(wed)
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    counte=1

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]        
        pil_image = Image.fromarray(face_image)            
        pil_image.show()       
        image_to_write = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
        paginas =len(face_locations)
        for count in range(0, len(face_locations)):
            
            cv2.imwrite(r"C:\Users\Matriz\Documents\rostos_vouga\qq2\frame%d.jpg" % counte , image_to_write )
            for xy in range(10000):
                counte = random.randint(1,1000)
    print("Novo loop, abrindo novo frame")      
  #  frm = frm + paginas
