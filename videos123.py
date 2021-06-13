import cv2

vidcap = cv2.VideoCapture('')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count%(10*fps) == 0 :
         cv2.imwrite('D:/cam/testimages/frame%d.jpg'%count,image)
         print('successfully written 10th frame')
    count+=1
