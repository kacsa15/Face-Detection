import PySimpleGUI as sg
import cv2
from PIL import Image
import io
from facedetection import face_detection


def update_window(window, newImg):
    image = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    bio = io.BytesIO()
    image.save(bio, format="PNG")

    window["-IMAGE-"].update(data=bio.getvalue())


def create_window():
    layout = [
        [sg.Column([[sg.Text("Image File"), sg.Input(size=(25, 1), key="-FILE-"), sg.FileBrowse()]], justification='center')],
        [sg.Radio("Detect Faces", "detection", key="face"),
         sg.Radio("Detect Eyes", "detection", key="eyes"),
         sg.Radio("Detect Nose", "detection", key="nose"),
         sg.Radio("Detect Mouth", "detection", key="mouth")],
        [sg.Column([[sg.Button("Load Image"), sg.Button("Show Image")]], justification='center')],
        [sg.Column([[sg.Image(key="-IMAGE-")]], justification='center')]
    ]

    window = sg.Window('Face Detection', layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            image = cv2.imread(values["-FILE-"])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Show Image":
            if values["face"]:
                newImg = face_detection(values["-FILE-"], "face")
                update_window(window,newImg)
            elif values["eyes"]:
                newImg = face_detection(values["-FILE-"], "eyes")
                update_window(window,newImg)
            elif values["nose"]:
                newImg = face_detection(values["-FILE-"], "nose")
                update_window(window,newImg)
            elif values["mouth"]:
                newImg = face_detection(values["-FILE-"], "mouth")
                update_window(window,newImg)


if __name__ == "__main__":
    create_window()
