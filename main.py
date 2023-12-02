from ultralytics import YOLO
import cv2

model = YOLO('best_v1.pt')
results = model("4.jpg", show = True)
cv2.waitKey(0)