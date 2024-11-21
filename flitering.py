import cv2
import numpy as np
image=cv2.imread('imgs/blur.jpg')
cv2.imshow('Roiginal img',image)
#identity
"""
identity_kernel=np.array([[0,0,0],[0,1,0],[0,0,0]])
blurred_img=cv2.filter2D(src=image,ddepth=-1,kernel=identity_kernel)
cv2.imshow('blurred img',blurred_img)
cv2.waitKey()
cv2.destroyAllWindows()"""
img_blur=cv2.blur(src=image,ksize=(11,11))
cv2.imshow('Blurred',img_blur)
cv2.waitKey()
cv2.destroyAllWindows()
kernel3 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)
 
cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharp_img)
     
cv2.waitKey()
cv2.imwrite('imgs/sharp_image.jpg', sharp_img)
cv2.destroyAllWindows()