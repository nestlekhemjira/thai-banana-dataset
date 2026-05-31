# Benchmark Results

This directory contains the experimental benchmark results for evaluating YOLO-based object detection models trained on the **Thai Banana Cultivar Detection Dataset** for cultivar conservation and commercial management.

---

# Evaluated Models

The following models were trained and evaluated based on the research paper parameters:

- **YOLOv8n** (100 Epochs)
- **YOLOv8s** (100 Epochs)
- **YOLOv9t** (100 Epochs)
- **YOLOv9t** (88 Epochs)

---

# Evaluation Metrics

Each model directory contains evaluation artifacts representing the following metrics:

- **mAP50 & mAP50-95** (Mean Average Precision)
- **Precision & Recall**
- **Precision-Recall Curve** (BoxPR_curve.png)
- **F1-Confidence Curve** (BoxF1_curve.png)
- **Confusion Matrix** (confusion_matrix.png)

---

# Benchmark Summary

Among the evaluated configurations, **YOLOv9t trained for 88 epochs** demonstrated the most balanced overall performance in terms of detection accuracy, training stability, and generalization capability.

While several models achieved competitive accuracy, extended training to 100 epochs resulted in observable overfitting tendencies in some configurations.

The optimized **YOLOv9t (88 Epochs)** maintained strong evaluation metrics while achieving lower validation loss and more stable convergence behavior, making it the most suitable model for deployment within the proposed smart agriculture system.

Detailed quantitative results are provided in `metrics_summary.csv`, while individual evaluation artifacts are available within each model-specific directory.
