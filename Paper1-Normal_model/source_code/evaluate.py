from ultralytics import YOLO
import pandas as pd
import numpy as np
import os

# Configuration
MODEL_PATH = '../benchmark/yolov8s_train/weights/best.pt'
DATA_CONFIG = '../data.yaml'

RESULT_DIR = '../benchmark/evaluation'
EXPERIMENT_NAME = 'test_evaluation'

# Create Output Directory
os.makedirs(RESULT_DIR, exist_ok=True)

# Load Model
model = YOLO(MODEL_PATH)

# Evaluate Model
metrics = model.val(
    split='test',
    data=DATA_CONFIG,
    project=RESULT_DIR,
    name=EXPERIMENT_NAME
)

# Save Evaluation Metrics
metrics_data = {
    'Metric': ['mAP50-95', 'mAP50', 'Precision', 'Recall'],
    'Overall': [
        metrics.box.maps.mean() if hasattr(metrics.box, 'maps') else np.nan,
        metrics.box.map50 if hasattr(metrics.box, 'map50') else np.nan,
        metrics.box.mp if hasattr(metrics.box, 'mp') else np.nan,
        metrics.box.mr if hasattr(metrics.box, 'mr') else np.nan
    ]
}

metrics_df = pd.DataFrame(metrics_data)

metrics_df.to_csv(
    os.path.join(RESULT_DIR, 'metrics.csv'),
    index=False
)

print('Evaluation completed successfully.')
