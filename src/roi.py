# 관심영역 표시

import cv2
import numpy as np

img = cv2.imread('../img/mbape_smiling.jpg')

x=140; y=30; w=350; h=380       # roi 좌표
roi = img[y:y+h, x:x+w]         # roi 지정        ---①

print(roi.shape)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
cv2.imshow("img", img)

# 이미지 저장
cv2.imwrite('../img/finished_emphasizing.jpg', img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()