import cv2 
src = cv2.imread("imgs/test_img.webp", cv2.IMREAD_GRAYSCALE); 
th, dst = cv2.threshold(src, 127, None, cv2.THRESH_TRUNC); 
cv2.imshow("1",dst)
cv2.waitKey()
cv2.destroyAllWindows()
