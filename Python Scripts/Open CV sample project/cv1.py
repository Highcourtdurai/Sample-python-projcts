"""import cv2
img=cv2.imread("sample1.jpg")
cv2.imshow("DuraiLogo",img)
cv2.imwrite("Logo.png",img)
cv2.waitKey(0)
cv2.destroyAllWindow()"""

"""import cv2
img=cv2.imread("sample1.jpg")
print(img.shape)
print(img.size)
print(img.dtype)"""


"""import cv2
img=cv2.imread("sample1.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow("OriginalImage",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindow()"""

"""import cv2
import imutils

img=cv2.imread("sample1.jpg")
gaussianImg=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianImg.jpg",gaussianImg)"""


"""import cv2
import imutils

img=cv2.imread("sample1.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdImg=cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg.jpg",thresholdImg)"""


