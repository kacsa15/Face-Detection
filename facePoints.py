import cv2
import numpy as np


def drawPoints(image, faceLandmarks, startpoint, endpoint, isClosed=False):
    points = []
    for i in range(startpoint, endpoint + 1):
        point = [faceLandmarks.part(i).x, faceLandmarks.part(i).y]
        points.append(point)

    points = np.array(points, dtype=np.int32)
    cv2.polylines(image, [points], isClosed, (253, 184, 55), thickness=2, lineType=cv2.LINE_8)


def facePoints(image, faceLandmarks):
    assert (faceLandmarks.num_parts == 68)
    drawPoints(image, faceLandmarks, 27, 30)  # Nose bridge
    drawPoints(image, faceLandmarks, 30, 35, True)  # Lower nose
    drawPoints(image, faceLandmarks, 36, 41, True)  # Left eye
    drawPoints(image, faceLandmarks, 42, 47, True)  # Right Eye
    drawPoints(image, faceLandmarks, 48, 59, True)  # Outer lip
    drawPoints(image, faceLandmarks, 60, 67, True)  # Inner lip


def eyesPoints(image, faceLandmarks):
    assert (faceLandmarks.num_parts == 68)
    drawPoints(image, faceLandmarks, 36, 41, True)  # Left eye
    drawPoints(image, faceLandmarks, 42, 47, True)  # Right Eye


def mouthPoints(image, faceLandmarks):
    assert (faceLandmarks.num_parts == 68)
    drawPoints(image, faceLandmarks, 48, 59, True)  # Outer lip
    drawPoints(image, faceLandmarks, 60, 67, True)  # Inner lip


def nosePoints(image, faceLandmarks):
    assert (faceLandmarks.num_parts == 68)
    drawPoints(image, faceLandmarks, 27, 30)  # Nose bridge
    drawPoints(image, faceLandmarks, 30, 35, True)  # Lower nose
