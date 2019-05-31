import shutil
import os

#shutil.move(r"C:\Users\Matriz\Documents\frames_vouga\qq\frame13.jpg", r"C:\Users\Matriz\Documents\frames_vouga\frame13.jpg")

#os.rename(source, destination)

# define the name of the directory to be created
nome = 3
path = "/Users/Matriz/Documents/rostos_vouga/qq2/know_faces/%d" % nome

try:  
    os.makedirs(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)
