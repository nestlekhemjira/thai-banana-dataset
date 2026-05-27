# Robust Banana Detection under LED/LCD Domain Shift

This repository contains benchmark results for evaluating YOLO-based object detection models on monitor-captured banana images, focusing on the **domain shift between LED and LCD screen displays**.

---

# 📌 Overview

This project investigates the robustness of object detection models when input images are affected by **screen-based domain shift**, where images are captured from digital displays (LED and LCD monitors).  

Such conditions introduce visual distortions such as noise, color variation, and reflection artifacts, which can negatively impact detection performance. The main objective is to evaluate and compare YOLO-based models under this challenging scenario.

---

# 🤖 Evaluated Models

The following models were trained and evaluated based on the research study:

- **YOLOv9s** (100 Epochs) - Optimized for high accuracy and robust performance across screen domains.
- **YOLOv10s** (90 Epochs) - Real-time end-to-end object detection model with zero-NMS training.

*All models were implemented using the Ultralytics YOLO framework and trained under the same dataset configuration to ensure a fair comparison.*

---

# 📊 Benchmark Structure

```text
benchmark/
├── yolov9s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── yolov10s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── benchmark_summary.csv
├── benchmark_comparison.xlsx
└── README.md

---

# 📋 Included Artifacts & Metrics

Each model directory contains the following evaluation files:

- `results.png` - Training/validation loss curves and metric progression over epochs.
- `confusion_matrix.png` - Highlights true vs. predicted banana cultivars to analyze error patterns.
- `BoxPR_curve.png` - **Precision-Recall Curve** visualization (representing the trade-off at different thresholds).
- `BoxF1_curve.png` - **F1-Confidence Curve** visualization (used to determine the optimal confidence threshold).
- `metric.csv` - Summary table of key performance indicators from the final training epoch:
  - **mAP50:** Mean Average Precision at an IoU threshold of 0.50.
  - **mAP50-95:** Mean Average Precision calculated across IoU thresholds from 0.50 to 0.95.
  - **Precision:** The ratio of correctly predicted positive banana instances to the total predicted positives.
  - **Recall:** The ratio of correctly predicted positive banana instances to all actual positive instances.

---

# 🛠️ Framework & Environment

- **Core Framework:** Ultralytics YOLO (YOLOv9 & YOLOv10)
- **Deep Learning Library:** PyTorch
- **Language:** Python 3
