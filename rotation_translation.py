import cv2
image=cv2.imread('imgs/test_img2.webp')
height,width=image.shape[:2]
center=(width/2,height/2)
rotat_matrix=cv2.getRotationMatrix2D(center=center,angle=90,scale=1)
rotated_img=cv2.warpAffine(src=image,M=rotat_matrix,dsize=(width,height))
cv2.imshow('Original Image',image)
cv2.imshow('Rotated image',rotated_img)
cv2.waitKey()
cv2.destroyAllWindows()
