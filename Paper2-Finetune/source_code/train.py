from ultralytics import YOLO
import torch
from config import *

device = "cuda" if torch.cuda.is_available() else "cpu"

model = YOLO(MODEL_PATH)

model.train(
    data=DATASET_YAML,
    epochs=EPOCHS,
    imgsz=IMG_SIZE,
    batch=BATCH_SIZE,
    device=device,
    freeze=10,
    lr0=1e-4,
    patience=10,
    optimizer="AdamW"
)
