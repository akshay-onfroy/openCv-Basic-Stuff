import cv2
import numpy as np
from skimage import data,filters
cap=cv2.VideoCapture("vids/traffic_video.mp4")
frames=[]
frameids=cap.get(7) * np.random.uniform(size=25) #7 returns the total no of frames
for fis in frameids:
    cap.set(cv2.CAP_PROP_POS_FRAMES,fis) #set the frame at that pos
    ret , frame = cap.read()
    frames.append(frame)
medianframe=np.median(frames,axis=0).astype(dtype=np.uint8)
cv2.imshow("Median",medianframe)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
 
# Convert background to grayscale
graymedian=cv2.cvtColor(medianframe,cv2.COLOR_BGR2GRAY)
ret =True
while ret:
    ret , frame = cap.read()
    if not ret:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ab=cv2.absdiff(frame,graymedian)
    th, ab= cv2.threshold(ab,30,255,cv2.THRESH_BINARY)
    cv2.imshow("frame",ab)
    cv2.waitKey(20)
cap.release()
cv2.destroyAllWindows()