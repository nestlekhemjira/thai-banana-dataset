from ultralytics import YOLO
import torch

# Configuration
MODEL_NAME = 'yolov8s.pt'
DATA_CONFIG = '../data.yaml'

PROJECT_NAME = '../benchmark'
EXPERIMENT_NAME = 'yolov8s_train'

EPOCHS = 100
IMAGE_SIZE = 640
BATCH_SIZE = 16
OPTIMIZER = 'AdamW'

# Device Configuration
DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'

# Load Model
model = YOLO(MODEL_NAME)

# Train Model
model.train(
    data=DATA_CONFIG,
    epochs=EPOCHS,
    imgsz=IMAGE_SIZE,
    batch=BATCH_SIZE,
    optimizer=OPTIMIZER,
    device=DEVICE,
    project=PROJECT_NAME,
    name=EXPERIMENT_NAME
)
