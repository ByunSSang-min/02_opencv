# OpenCV - Day 2

## 📡 Image Operations

**Date:** 2025-07-29
**Author:** Sang-Min Byun

---

<br>

## 📋 Project Summary

⚫ **Image Operations**

This project demonstrates image **color processing**, binary image generation through **thresholding**, and image **compositing**.

The core idea:
- The image colors are represented using 3 methods: BGR(BGRA), HSV, YUV.
- Generate a binary image through thresholding using Otsu's binarization method to find optimal threshold without iteration.
- Using masking, extract only the subject from a photo with a chroma key background, and then composite it with a photo of a different background.
  - The photo with a chroma key background should be smaller than the other photo that be composited.


<br>

## 🟥 Representing the image colors

### 📷 Python Code

This code displays the image in three formats: the original format, BGR format, and BGRA format.

```python
import cv2
import numpy as np

# 기본값
img = cv2.imread('../img/like_lenna.png')

# bgr
bgr = cv2.imread('../img/like_lenna.png', cv2.IMREAD_COLOR)

# a
bgra = cv2.imread('../img/like_lenna.png', cv2.IMREAD_UNCHANGED)

# shape
print("default", img.shape, "color", bgr.shape, "unchanged", bgra.shape)

# 이미지 보여주기
cv2.imshow('img', img)
cv2.imshow('bgr', bgr)
cv2.imshow('alpha', bgra[:,:,3])

cv2.waitKey(0)
cv2.destroyAllWindows()

---

