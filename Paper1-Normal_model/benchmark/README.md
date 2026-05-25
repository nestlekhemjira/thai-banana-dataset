# Benchmark Results

This directory contains benchmark results for multiple YOLO-based object detection models trained on the Thai Banana Cultivar Detection Dataset.

---

# Evaluated Models

The following models were evaluated:

- YOLOv8n
- YOLOv8s
- YOLOv9t (100 Epochs)
- YOLOv9t (88 Epochs)

---

# Directory Structure

```text
benchmark/
├── yolov8/
├── yolov8s/
├── yolov9t(100epoch)/
├── yolov9t(88epoch)/
│
├── benchmark_summary.csv
├── benchmark_comparison.xlsx
└── README.md
```

---

# Included Benchmark Files

Each model directory may contain:

- results.png
- confusion_matrix.png
- BoxPR_curve.png
- BoxF1_curve.png
- metrics.csv

---

# Evaluation Metrics

The benchmark evaluation includes:

- mAP50-95
- mAP50
- Precision
- Recall
- Precision-Recall Curve
- F1-Confidence Curve
- Confusion Matrix

---

# Notes

- All models were trained using the same dataset split configuration.
- Training and evaluation were conducted using the Ultralytics YOLO framework.
- Results may vary depending on hardware configuration and random initialization.

---

# Framework

- Ultralytics YOLO
- PyTorch
- Python 3
