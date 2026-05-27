# Robust Banana Detection under LED/LCD Domain Shift

This repository provides benchmark results for evaluating YOLO-based object detection models on monitor-captured banana images, with a focus on **domain shift between LED and LCD screen displays**.

---

# Project Overview

This work investigates the robustness of object detection models under **screen-based domain shift**, where images are captured from digital displays (LED and LCD monitors).

Such conditions introduce visual distortions including noise, color variation, and reflection artifacts, which can significantly affect detection performance.

The main objective is to evaluate and compare YOLO-based models under this challenging and non-standard imaging scenario.

---

# Models Evaluated

The following models were trained and evaluated based on the research study:

- **YOLOv9s** — 99 epochs (high-accuracy configuration)
- **YOLOv10s** — 90 epochs (efficient real-time detection with zero-NMS design)

All models were implemented using the **Ultralytics YOLO framework** and trained under the same dataset configuration to ensure a fair comparison.

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
# Evaluation Artifacts

Each model directory includes the following outputs:

### results.png
Training and validation loss curves with metric progression across epochs.

### confusion_matrix.png
Visualization of true vs. predicted banana cultivar classes for error analysis.

### BoxPR_curve.png
Precision–Recall curve illustrating performance across confidence thresholds.

### BoxF1_curve.png
F1-score vs. confidence curve used to identify optimal operating threshold.

### metrics.csv
Final epoch performance metrics including:

- **mAP50**: Mean Average Precision at IoU = 0.50  
- **mAP50-95**: Mean Average Precision across IoU thresholds (0.50–0.95)  
- **Precision**: Accuracy of predicted positive detections  
- **Recall**: Coverage of ground-truth objects  

---

# 🛠️ Framework & Environment

- **Model Framework:** Ultralytics YOLO (YOLOv9, YOLOv10)
- **Deep Learning Library:** PyTorch
- **Programming Language:** Python 3.x
