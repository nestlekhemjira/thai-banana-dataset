# Robust Banana Detection under LED/LCD Domain Shift

This repository contains benchmark results for evaluating YOLO-based object detection models on monitor-captured banana images, focusing on the domain shift between LED and LCD screen displays.

---

# 📌 Overview

This project investigates the robustness of object detection models when input images are affected by **screen-based domain shift**, where images are captured from digital displays (LED and LCD monitors). Such conditions introduce noise, color distortion, and reflection artifacts that impact detection performance.

The goal is to evaluate and compare YOLO-based models under this challenging scenario.

---

# 🤖 Evaluated Models

The following models were trained and evaluated:

- YOLOv9s (100 epochs)
- YOLOv10s (90 epochs)

All models were implemented using the Ultralytics framework and trained under the same dataset configuration.

---

# 📊 Benchmark Structure

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
