# Benchmark Results

This directory contains the experimental benchmark results evaluating YOLO-based object detection models on monitor-captured banana images, specifically focusing on the **domain shift between LED and LCD screen displays**.

---

# Evaluated Models

The following models were trained and evaluated under identical dataset configurations to ensure a fair comparison:

- **YOLOv9s** — 99 Epochs (Optimized for robust performance across domains)
- **YOLOv10s** — 90 Epochs (Real-time end-to-end object detection)

---

# Directory Structure

```text
benchmark/
├── yolov9s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── yolov10s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── summary.csv
└── README.md
```
---

# Evaluation Metrics
- Each model directory contains artifacts representing the following metrics:
- mAP50 & mAP50-95 (Mean Average Precision)
- Precision & Recall
- Precision-Recall Curve (BoxPR_curve.png)
- F1-Confidence Curve (BoxF1_curve.png)
- Confusion Matrix (confusion_matrix.png)

---
# Framework & Environment
- Core Framework: Ultralytics YOLO (YOLOv9 & YOLOv10)
- Deep Learning Library: PyTorch
- Language: Python 3.x
