import cv2
img_org = cv2.imread("imgs/tiger.jpg")
img = cv2.cvtColor(img_org,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
countours,hierachy=cv2.findContours(image=img,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image=img_org,contours=countours,contourIdx=-1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)
cv2.imshow("Contours",img_org)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RETR_TREE for all contours
#RETR_EXTRENAL for outer contours