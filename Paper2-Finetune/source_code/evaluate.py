from ultralytics import YOLO
import pandas as pd
import numpy as np

from config import *

model = YOLO(MODEL_PATH)

results = model.predict(
    source=NON_BANANA_DIR,
    conf=CONF_THRESHOLD
)

# calculate false positive metrics
