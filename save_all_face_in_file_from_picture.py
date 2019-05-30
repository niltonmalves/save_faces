from PIL import Image
import face_recognition
import cv2


# Load the jpg file into a numpy array
#image = face_recognition.load_image_file("pessoas.jpg")
#image = face_recognition.load_image_file(r"C:\Users\Matriz\Documents\face_recognition-master\examples\Nova pasta\frame2368.jpg")
wed = r"C:\Users\Matriz\Documents\frames_from_obama_youtube_mp4\frame51.jpg"
image = face_recognition.load_image_file(wed)
# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    
    pil_image = Image.fromarray(face_image)
#img = cv2.imread("pessoas.jpg")
    
    pil_image.show()
   #image.save()
    image_to_write = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
    #pil_image.new(RGB, 1, color=0)

    for count in range(0, len(face_locations)):
    #while count < len(face_locations):
        cv2.imwrite(r"C:\Users\Matriz\Documents\face_recognition-master\examples\Nova pasta\rostos\frame%d.jpg" % count , image_to_write )
       # cv2.imwrite("frame%d.jpg" , image_to_write )
        #print(face_image)
        #print(face_location)
        #print(face_locations)
        #count = count + 1
        #print(pil_image)

