import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key = "-IMAGE-")],
    [sg.Text("People in the picture: 0", key = "-TEXT-", expand_x=True, justification="c")] # c means center.
    ]

window = sg.Window("Face Detector", layout)

# get video.
video = cv2.VideoCapture(0) # 0 for webcam, 1 for dslr etc.
face_cascade = cv2.CascadeClassifier("face_detector\haarcascade_frontalface_default.xml")

while True:
    event, values = window.read(timeout = 0)
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 7,
        minSize = (50,50))

    # draw the rectangles.
    for (x, y, w, h) in faces: # x and y are the origin of face, w and h are the width and height.
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)  # (image, top left, bottom right, color, line width)

    # update the image.
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["-IMAGE-"].update(data = imgbytes)
    
    # update the text.
    window["-TEXT-"].update(f"People in picture: {len(faces)}")

window.close()