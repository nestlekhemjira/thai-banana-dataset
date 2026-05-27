# MODEL EXPORT (ONNX + PYTORCH)
from ultralytics import YOLO
import os
import torch

MODEL_PATH = "./runs/experiment/weights/best.pt"
EXPORT_DIR = "./export"

os.makedirs(EXPORT_DIR, exist_ok=True)

model = YOLO(MODEL_PATH)

# ONNX export
onnx_path = model.export(format="onnx", imgsz=640, dynamic=True)

print("📦 ONNX exported:", onnx_path)

# PyTorch weights copy
torch.save(model.model.state_dict(),
           os.path.join(EXPORT_DIR, "model.pth"))

print("✅ Export completed")
