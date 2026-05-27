# Benchmark Results

This repository contains benchmark results for YOLO-based object detection models evaluated on monitor-captured banana images under LED/LCD domain shift conditions.

---

# Evaluated Models

- **YOLOv9s** — 99 epochs
- **YOLOv10s** — 90 epochs

All models were trained using the Ultralytics YOLO framework under identical dataset configurations for fair comparison.

---

# Benchmark Structure

```text
benchmark/
├── yolov9s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metrics.csv
│
├── yolov10s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metrics.csv
│
├── benchmark_summary.csv
├── benchmark_comparison.xlsx
└── README.md
```
---
# Evaluation Metrics
- mAP50
- mAP50-95
- Precision
- Recall
- Precision-Recall Curve
- F1-Confidence Curve
- Confusion Matrix

---
# Framework & Environment
- Ultralytics YOLO (YOLOv9, YOLOv10)
- PyTorch
- Python 3.x
