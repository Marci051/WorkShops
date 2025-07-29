import cv2 as cv
import random as rd
import imageio
import numpy as np


bg = cv.imread('bg.png', cv.IMREAD_COLOR_BGR)

rows, cols, channels = bg.shape
print(rows, cols)
cv.imshow('bg', bg)
cv.waitKey(1000)

def snow():
    img = np.array(bg.copy())
    center = (rd.randint(0, cols - 1), rd.randint(0, rows - 1))
    color = (rd.randint(245, 255), rd.randint(245, 255), rd.randint(245, 255))
    radius = rd.randint(1, 3)
    cv.circle(img, center=center , radius=radius, color=color, thickness=-1)
    # img[rd.randint(0, 380), rd.randint(0, 690)] = rd.randint(200, 255)
    return img

if __name__ == '__main__':
    count = 60
    images_list = []
    for i in range(count):
        images_list.append(snow())

    with imageio.get_writer('snow_1.gif', mode='I') as writer:
        for image in images_list:
            writer.append_data(image)
