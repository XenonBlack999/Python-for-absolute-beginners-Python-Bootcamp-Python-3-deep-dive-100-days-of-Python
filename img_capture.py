import cv2

imgca = cv2.VideoCapture(0)

result = True


while (result):
    ret, frame = imgca.read()
    cv2.imwrite("test.jpg", frame)
    result = False
    print("Image capture .....")
    
imgca.release()
