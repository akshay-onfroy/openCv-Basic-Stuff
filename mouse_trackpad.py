import cv2
top_up=[]
bottom_down=[]
def draw_rectangle(action,x,y,*userdata):
    global top_up,bottom_down
    if action == cv2.EVENT_LBUTTONDOWN:
        top_up=[(x,y)]
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_down =[(x,y)]
        cv2.rectangle(img,top_up[0],bottom_down[0],(0,0,255),thickness=3)
        cv2.imshow("Window",img)
img = cv2.imread("imgs/mouse_img.webp")
cv2.namedWindow("Window")
temp=img.copy()
cv2.setMouseCallback("Window",draw_rectangle)

k=0
while k!=ord('q'):
    cv2.imshow("Window",img)
    k=cv2.waitKey(0)
    if k==ord('c'):
        image= temp.copy()
        cv2.imshow("Window", image)
 
cv2.destroyAllWindows()



    

