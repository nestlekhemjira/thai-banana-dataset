# DATASET CHECK
import os

DATASET_PATH = "./dataset"
LABELS_PATH = os.path.join(DATASET_PATH, "labels")

total = 0
empty = 0

for file in os.listdir(LABELS_PATH):
    if file.endswith(".txt"):
        total += 1
        with open(os.path.join(LABELS_PATH, file)) as f:
            if f.read().strip() == "":
                empty += 1

print("📊 Dataset Report")
print("Total labels:", total)
print("Empty labels:", empty)
