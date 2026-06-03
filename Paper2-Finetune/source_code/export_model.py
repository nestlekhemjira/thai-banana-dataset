from ultralytics import YOLO
from config import *

model = YOLO(MODEL_PATH)

model.export(
    format="onnx",
    imgsz=IMG_SIZE,
    simplify=True,
    dynamic=False
)
