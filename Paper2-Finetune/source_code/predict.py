from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(
    source="sample.jpg",
    save=True
)
