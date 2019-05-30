import cv2
vidcap = cv2.VideoCapture(r"G:\10_R_21052019_120000.dav")
success,image = vidcap.read()
count = 0
success = True
resto = 1
while success:
  success,image = vidcap.read()
  if resto == 0:
    print("chegou a", count)
    cv2.imwrite(r"C:\Users\Matriz\Documents\frames_vouga\21052019\frame%d.jpg" % count, image)     # save frame as JPEG file
    next  
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
  resto = count % 13
