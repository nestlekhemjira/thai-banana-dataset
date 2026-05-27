# =========================================================
# INFERENCE SCRIPT
# =========================================================

from ultralytics import YOLO

MODEL_PATH = "./runs/experiment/weights/best.pt"
SOURCE = "test.jpg"

model = YOLO(MODEL_PATH)

results = model.predict(
    source=SOURCE,
    conf=0.5,
    save=True,
    show=True
)

print("✅ Prediction done")
