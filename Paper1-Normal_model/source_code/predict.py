from ultralytics import YOLO
import pandas as pd
import os

# Configuration
MODEL_PATH = '../benchmark/yolov8s_train/weights/best.pt'
SOURCE_DIR = '../test/images'
RESULT_DIR = '../benchmark/predictions'
LABEL_DIR = '../test/labels'

CLASS_NAMES = [
    'Candyapple',
    'Namwa',
    'Namwadam',
    'Homthong',
    'Nak',
    'Thepphanom',
    'Kai',
    'Lepchanggud',
    'Ngachang',
    'Huamao'
]
os.makedirs(RESULT_DIR, exist_ok=True)

# Load Model
model = YOLO(MODEL_PATH)

# Run Prediction
results = model.predict(
    source=SOURCE_DIR,
    conf=0.5,
    save=True,
    project=RESULT_DIR,
    name='predict_results'
)

# Save Prediction Logs
log_data = []

for result in results:
    img_path = result.path if hasattr(result, 'path') else None
    img_name = os.path.splitext(os.path.basename(img_path))[0]

    label_path = os.path.join(LABEL_DIR, img_name + '.txt')

    true_classes = []

    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) > 0:
                    class_id = int(parts[0])

                    if 0 <= class_id < len(CLASS_NAMES):
                        true_classes.append(CLASS_NAMES[class_id])
   true_label_str = ', '.join(sorted(set(true_classes))) if true_classes else 'Unknown'

    for box, conf, cls in zip(
        result.boxes.xyxy.cpu().numpy(),
        result.boxes.conf.cpu().numpy(),
        result.boxes.cls.cpu().numpy()
    ):
        log_data.append({
            'image': img_path,
            'predicted_class': result.names[int(cls)],
            'true_label': true_label_str,
            'confidence': float(conf),
            'x1': float(box[0]),
            'y1': float(box[1]),
            'x2': float(box[2]),
            'y2': float(box[3])
        })

# Export Prediction Logs
df_log = pd.DataFrame(log_data)

output_path = os.path.join(RESULT_DIR, 'prediction_logs.xlsx')

df_log.to_excel(output_path, index=False)

print(f'Prediction logs saved to: {output_path}')
