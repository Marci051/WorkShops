import cv2 as cv
import random as rd
import imageio
import numpy as np


bg = cv.imread('bg.png', cv.IMREAD_COLOR_BGR)

rows, cols, channels = bg.shape
print(rows, cols)

snows_x = []
for j in range(100):
    snows_x.append(rd.randint(0, cols))

print(snows_x)

# for snow in snows_x:
#     cv.circle(bg, center=(snow, 30), radius=2, color=(250, 244, 255), thickness=-1)
#
# cv.imshow('snow', bg)
# cv.waitKey(0)


def snowww():
    img = bg.copy()
    images_list = []
    for row in range(rows):
        for snow in snows_x:
            cv.circle(img, center=(snow, row), radius=2, color=(250, 245, 255), thickness=-1)
            # cv.imshow('snow', img)
            # cv.waitKey(10)
            images_list.append(img)
            img = bg.copy()
    with imageio.get_writer('snow1.gif', mode='I') as writer:
        for image in images_list:
            writer.append_data(image)



#### AI
# snows_y = [rd.randint(0, rows//3) for _ in snows_x]  # random start point
#
# images_list = []
# for _ in range(50):
#     img = bg.copy()
#     for i in range(len(snows_x)):
#         cv.circle(img, center=(snows_x[i], snows_y[i]), radius=2, color=(250, 245, 255), thickness=-1)
#         snows_y[i] += 5  # حرکت رو به پایین
#         if snows_y[i] >= rows:
#             snows_y[i] = 0  # ریست بعد از رسیدن به پایین
#     images_list.append(img)
#
# with imageio.get_writer('snow.gif', mode='I') as writer:
#     for image in images_list:
#         writer.append_data(image)

if __name__ == '__main__':
    snowww()