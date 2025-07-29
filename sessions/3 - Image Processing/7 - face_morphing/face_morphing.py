import cv2 as cv
import numpy as np
import imageio


p2001 = cv.imread("2001.jpg")
p2002 = cv.imread("2002.jpg")
p2003 = cv.imread("2003.jpg")
p2004 = cv.imread("2004.jpg")
p2005 = cv.imread("2005.jpg")
p2006 = cv.imread("2006.jpg")
p2007 = cv.imread("2007.jpg")
p2008 = cv.imread("2008.jpg")
p2009 = cv.imread("2009.jpg")
p2010 = cv.imread("2010.jpg")
p2011 = cv.imread("2011.jpg")
p2012 = cv.imread("2012.jpg")
p2013 = cv.imread("2013.jpg")
p2014 = cv.imread("2014.jpg")
p2015 = cv.imread("2015.jpg")
p2016 = cv.imread("2016.jpg")
p2017 = cv.imread("2017.jpg")
p2018 = cv.imread("2018.jpg")

emma = [p2001, p2002, p2003, p2004, p2005, p2006, p2007, p2008, p2009, p2010, p2011, p2012, p2013, p2014, p2015, p2016, p2017, p2018]

emma = list(map(lambda x: cv.resize(x, (400, 400)), emma))

images = []
for idx, image in enumerate(emma):
    current_image = image.astype(np.float64)
    try:
        new_image = emma[idx + 1].astype(np.float64)
    except IndexError:
        break
    i = 100
    while (i >= 0):
        input_current_image = current_image * (i / 100)
        input_new_image = (new_image * ((100 - i) / 100))
        result = cv.add(input_current_image, input_new_image).astype(np.uint8)
        if i == 100:
            cv.waitKey(1000)
        else:
            cv.waitKey(10)
        cv.imshow("Face Morphing", result)
        result = cv.cvtColor(result, cv.COLOR_BGR2RGB)
        images.append(result)
        i -= 1


with imageio.get_writer('face_morphing.gif', mode='I') as writer:
    for image in images:
        writer.append_data(image)

