# Source Code

This directory contains the source code used for training, evaluation, prediction, model export, and dataset validation for the Thai Banana Cultivar Detection Dataset.

---

# Directory Structure

```text
source_code/
├── train.py
├── evaluate.py
├── predict.py
├── export_model.py
├── dataset_check.py
├── requirements.txt
└── README.md
Requirements
Install required packages before running the scripts:
pip install -r requirements.txt
Scripts Overview
train.py
Train the YOLOv8 model using the provided dataset configuration.
Features:
YOLOv8 training pipeline
AdamW optimizer
GPU/CPU automatic detection
Benchmark output generation
Run:
python train.py
evaluate.py
Evaluate the trained model on the test dataset.
Features:
mAP50-95 evaluation
Precision and Recall calculation
Automatic metrics export to CSV
Run:
python evaluate.py
Output:
metrics.csv
predict.py
Run inference on test images and export prediction logs.
Features:
Confidence score prediction
Bounding box extraction
Ground truth comparison
Excel prediction logging
Run:
python predict.py
Output:
prediction_logs.xlsx
predicted images
export_model.py
Export trained models into multiple formats.
Supported formats:
PyTorch (.pt)
PyTorch State Dictionary (.pth)
ONNX (.onnx)
Run:
python export_model.py
dataset_check.py
Validate dataset integrity by checking:
missing labels
missing images
filename mismatches
Run:
python dataset_check.py
Dataset Configuration
The scripts use the dataset configuration file:
data.yaml
Example:
train: train/images
val: valid/images
test: test/images

nc: 10

names:
  - Candyapple
  - Namwa
  - Namwadam
  - Homthong
  - Nak
  - Thepphanom
  - Kai
  - Lepchanggud
  - Ngachang
  - Huamao
Framework
This project uses:
Ultralytics YOLOv8
PyTorch
Python 3
Notes
All scripts use relative paths for portability.
GPU acceleration is automatically enabled when CUDA is available.
The provided scripts are intended for research and educational purposes.
