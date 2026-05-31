# Benchmark Results

This directory contains the experimental benchmark results for evaluating YOLO-based object detection models trained on the **Thai Banana Cultivar Detection Dataset** with data-centric negative sample fine-tuning.

---

# Evaluated Models

The following models were trained and evaluated based on the research paper parameters:

- **YOLOv8s** (50 Epochs)
- **YOLOv9s** (40 Epochs)
- **YOLOv10s** (19 Epochs)

---

# Evaluation Artifacts
Each model directory contains evaluation artifacts representing the following metrics:
- mAP50 & mAP50-95 (Mean Average Precision)
- Precision & Recall
- Precision-Confidence Curve (BoxP_curve.png)
- Recall-Confidence Curve (BoxR_curve.png)
- Precision-Recall Curve (BoxPR_curve.png)
- Confusion Matrix (confusion_matrix.png)

---

### Benchmark Summary

Three YOLO-based object detection models were evaluated using the Thai Banana Cultivar Detection Dataset with data-centric negative sample fine-tuning.

Among the evaluated architectures, **YOLOv8s** demonstrated the most balanced performance across detection accuracy, localization quality, and training stability. Achieving the highest overall validation metrics, it was selected as the final model for subsequent deployment. Meanwhile, **YOLOv9s** delivered comparable detection performance with reduced training time, while **YOLOv10s** achieved the fastest convergence despite slightly lower precision and localization quality.

Detailed quantitative results are provided in `metrics_summary.csv`, while individual evaluation artifacts are available within each model-specific directory.
