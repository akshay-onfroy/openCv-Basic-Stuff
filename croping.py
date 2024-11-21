import cv2
image=cv2.imread('imgs/test_img.webp')
print("Image shape:",image.shape)
cropped_img=image[100:682,200:800]
cv2.imshow('Cropped Image',cropped_img)
cv2.waitKey()
cv2.destroyAllWindows()
