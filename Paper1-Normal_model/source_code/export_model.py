from ultralytics import YOLO
import torch
import shutil
import os

# Configuration
MODEL_PATH = '../benchmark/yolov8s_train/weights/best.pt'

EXPORT_DIR = '../benchmark/exported_models'

os.makedirs(EXPORT_DIR, exist_ok=True)

# Load Model
model = YOLO(MODEL_PATH)

# Export .pt Model
pt_output = os.path.join(
    EXPORT_DIR,
    'best_model.pt'
)

shutil.copy(
    MODEL_PATH,
    pt_output
)

print(f'PT model exported to: {pt_output}')

# Export ONNX Model
model.export(
    format='onnx',
    dynamic=True,
    simplify=True,
    opset=12
)

onnx_source = (
    '../benchmark/yolov8s_train/weights/best.onnx'
)

onnx_output = os.path.join(
    EXPORT_DIR,
    'best_model.onnx'
)

if os.path.exists(onnx_source):

    shutil.copy(
        onnx_source,
        onnx_output
    )

    print(
        f'ONNX model exported to: {onnx_output}'
    )

else:
    print('ONNX export failed.')

# Export PyTorch State Dictionary
pth_output = os.path.join(
    EXPORT_DIR,
    'best_model.pth'
)

torch.save(
    model.model.state_dict(),
    pth_output
)

print(
    f'PTH model exported to: {pth_output}'
)
