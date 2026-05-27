# =========================================================
# MODEL EVALUATION
# =========================================================

from ultralytics import YOLO

MODEL_PATH = "./runs/experiment/weights/best.pt"
DATA_YAML = "data.yaml"

model = YOLO(MODEL_PATH)

metrics = model.val(data=DATA_YAML)

print("📊 Evaluation Results")
print(metrics)
