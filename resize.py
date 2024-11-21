import cv2
image=cv2.imread('imgs/test_img.webp',1)
h,w,c=image.shape
print("Image size=:",h,'x',w)
cv2.imshow('Original image',image)
#using width and height
"""
width=300
height=600
points=(width,height)
resized_img = cv2.resize(image,points,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Image',resized_img)
cv2.waitKey()
cv2.destroyAllWindows()"""
# using scaling method

scale=0.6
resized_img = cv2.resize(image,None,fx=scale,fy=scale,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Image',resized_img)
cv2.waitKey()
cv2.destroyAllWindows()