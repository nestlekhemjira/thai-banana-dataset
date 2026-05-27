import os
import time
import pandas as pd
import torch
from ultralytics import YOLO

# CONFIG (USER EDIT ONLY)
DATA_YAML = "data.yaml"
MODEL_NAME = "yolov8s.pt"

RUN_DIR = "./runs"
RUN_NAME = "experiment"

EPOCHS = 100
IMG_SIZE = 640
BATCH_SIZE = 16
WORKERS = 2
PATIENCE = 10
DEVICE = 0 if torch.cuda.is_available() else "cpu"

# LOAD MODEL
model = YOLO(MODEL_NAME)

print("🚀 Training started")

start_time = time.time()

# TRAIN
results = model.train(
    data=DATA_YAML,
    epochs=EPOCHS,
    imgsz=IMG_SIZE,
    batch=BATCH_SIZE,
    device=DEVICE,
    workers=WORKERS,
    patience=PATIENCE,
    project=RUN_DIR,
    name=RUN_NAME,
    exist_ok=True,
    save=True,
    verbose=True
)

train_time = (time.time() - start_time) / 60
print(f"⏱ Training time: {train_time:.2f} min")

# save time
os.makedirs(RUN_DIR, exist_ok=True)
with open(os.path.join(RUN_DIR, "training_time.txt"), "w") as f:
    f.write(str(train_time))
