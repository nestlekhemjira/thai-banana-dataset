# Benchmark Results

This directory contains the experimental benchmark results for evaluating YOLO-based object detection models trained on the **Thai Banana Cultivar Detection Dataset** for cultivar conservation and commercial management.

---

# Evaluated Models

The following models were trained and evaluated based on the research paper parameters:

- **YOLOv8n**
- **YOLOv8s**
- **YOLOv9t** (100 Epochs)
- **YOLOv9t** (88 Epochs) — *Identified as the most suitable model balancing accuracy, robustness, and stability while preventing overfitting.*

---

# Directory Structure

```text
benchmark/
├── yolov8n/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── yolov8s/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── yolov9t(100epoch)/
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── BoxPR_curve.png
│   ├── BoxF1_curve.png
│   └── metric.csv
│
├── yolov9t(88epoch)/
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
Each model directory contains evaluation artifacts representing the following metrics:
- mAP50 & mAP50-95 (Mean Average Precision)
- Precision & Recall
- Precision-Recall Curve (BoxPR_curve.png)
- F1-Confidence Curve (BoxF1_curve.png)
- Confusion Matrix (confusion_matrix.png)

---
# Framework & Environment
- Core Framework: Ultralytics YOLO
- Deep Learning Library: PyTorch
- Language: Python 3.x
