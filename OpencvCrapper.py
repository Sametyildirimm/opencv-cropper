import numpy as np
import cv2


resim = cv2.imread("resimm.jpg")
rows, cols = resim.shape[:2]
a = []
def draw(event, x, y, flags, param):
    global a

  
    if event == cv2.EVENT_LBUTTONDBLCLK and len(a) < 4:
        a.append((x, y))
        cv2.circle(resim, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("resim", resim)

   
    if len(a) == 4:
      
        points = np.array(a, dtype="float32")

      
        def order_points(pts):
            rect = np.zeros((4, 2), dtype="float32")
            s = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)

            rect[0] = pts[np.argmin(s)]  
            rect[2] = pts[np.argmax(s)]   
            rect[1] = pts[np.argmin(diff)] 
            rect[3] = pts[np.argmax(diff)] 

            return rect

       
        ordered_points = order_points(points)

        
        destination_matrix = np.array([
            [0, 0],                
            [cols-1, 0],         
            [cols-1, rows-1],      
            [0, rows-1]           
        ], dtype="float32")
        perspective_matrix = cv2.getPerspectiveTransform(ordered_points, destination_matrix)
        img3 = cv2.warpPerspective(resim, perspective_matrix, (cols, rows))  
        cv2.imshow("Kesilmiş Görüntü", img3)
        
        a.clear()


cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("resim", draw)

while True:
    cv2.imshow("resim", resim)
    if cv2.waitKey(1) == ord("q"):  
        break

cv2.destroyAllWindows()
