# Import dependencies
import cv2
# Read Images
img = cv2.imread('imgs/test_img3.webp')
h,w,x=img.shape
print("Size:",h,"x",w)
# Display Image
cv2.imshow('Original Image',img)
cv2.waitKey(0)
# Print error message if image is null
if img is None:
    print('Could not read image')
# Draw Circle on image
"""imagecircle=img.copy()
point=(415,190)
radius=100
cv2.circle(imagecircle,point,radius,(0,0,255),thickness=3)#change 3 to -1 for filled circle
cv2.imshow('Filled image',imagecircle)
cv2.waitKey()
cv2.destroyAllWindows()"""

#draw line on image

imageline = img.copy()
start=(400,80)
end=(600,80)
cv2.line(imageline,start,end,(0,0,255),thickness=3)
cv2.imshow("lined image",imageline)
cv2.waitKey()
cv2.destroyAllWindows()
