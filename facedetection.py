import cv2
import dlib

from facePoints import eyesPoints, facePoints, nosePoints, mouthPoints


def writeFaceLandmarksToLocalFile(faceLandmarks, fileName):
    with open(fileName, 'w') as f:
        for p in faceLandmarks.parts():
            f.write("%s %s\n" % (int(p.x), int(p.y)))

    f.close()


def face_detection(imagePath, detect):
    faceLandmarkDetector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    frontalFaceDetector = dlib.get_frontal_face_detector()

    img = cv2.imread(imagePath)
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    allFaces = frontalFaceDetector(imageRGB, 0)
    allFacesLandmark = []

    for face in allFaces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 68), 1)
        faceRectangleDlib = dlib.rectangle(int(x1), int(y1), int(x2), int(y2))

        detectedLandmarks = faceLandmarkDetector(imageRGB, faceRectangleDlib)
        allFacesLandmark.append(detectedLandmarks)

        match detect:
            case "face":
                facePoints(img, detectedLandmarks)
            case "eyes":
                eyesPoints(img, detectedLandmarks)
            case "nose":
                nosePoints(img, detectedLandmarks)
            case "mouth":
                mouthPoints(img, detectedLandmarks)

    return img


