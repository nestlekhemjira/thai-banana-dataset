# Benchmark Results

This directory contains the experimental benchmark results evaluating YOLO-based object detection models on monitor-captured banana images, specifically focusing on the **domain shift between LED and LCD screen displays**.

---

# Evaluated Models

The following models were trained and evaluated under identical dataset configurations to ensure a fair comparison:

- **YOLOv9s** (99 Epochs)
- **YOLOv10s** (90 Epochs)

---

# Evaluation Metrics

Each model directory contains artifacts representing the following metrics:

- **mAP50 & mAP50-95** (Mean Average Precision)
- **Precision & Recall**
- **Precision-Recall Curve** (BoxPR_curve.png)
- **F1-Confidence Curve** (BoxF1_curve.png)
- **Confusion Matrix** (confusion_matrix.png)

---

## Benchmark Summary

Two YOLO-based object detection architectures were evaluated using a dataset of 10,380 recaptured screen images to investigate performance under display-induced domain shifts and structural image artifacts.

Among the evaluated models, **YOLOv9s** demonstrated superior overall performance across key evaluation metrics. The model achieved a higher mAP50-95 score and lower validation loss while maintaining excellent precision and recall, making it the most suitable architecture for deployment within the proposed system.

Although **YOLOv10s** achieved competitive results, **YOLOv9s** exhibited stronger localization consistency and greater robustness under display-related distortions.

Confusion matrix analysis revealed minimal cross-class confusion between banana cultivars, with most errors originating from background-object separation. These findings suggest that both architectures are highly robust to screen-induced domain variations and image degradation effects.

Detailed quantitative results are provided in `metrics_summary.csv`, while individual evaluation artifacts are available within each model-specific directory.
