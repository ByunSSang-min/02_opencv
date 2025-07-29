# 관심영역 복제 및 새 창에 띄우기

import cv2
import numpy as np

img = cv2.imread('../img/mbape_smiling.jpg')

x=140; y=30; w=350; h=380       # roi 좌표
roi = img[y:y+h, x:x+w]         # roi 지정        ---①

print(roi.shape)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
img2 = roi.copy()           # roi 배열 복제 ---①

cv2.imshow("img", img)      # 원본 이미지 출력
cv2.imshow("roi", img2)     # roi 만 따로 출력

# 이미지 저장
cv2.imwrite('../img/finished_emphasizing.jpg', img)
cv2.imwrite('../img/emphasized_part.jpg', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()