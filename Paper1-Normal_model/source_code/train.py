from ultralytics import YOLO
import torch

# Configuration
MODEL_NAME = 'yolov8s.pt'
DATA_CONFIG = '../data.yaml'
PROJECT_NAME = '../benchmark'
EXPERIMENT_NAME = 'yolov8s_train'

# Train Model
model = YOLO(MODEL_NAME)

model.train(
    data=DATA_CONFIG,
    epochs=100,
    imgsz=640,
    batch=16,
    optimizer='AdamW',
    device='cuda:0' if torch.cuda.is_available() else 'cpu',
    project=PROJECT_NAME,
    name=EXPERIMENT_NAME
)
