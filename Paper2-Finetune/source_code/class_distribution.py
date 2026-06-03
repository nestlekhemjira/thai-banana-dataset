from pathlib import Path
from collections import defaultdict
import pandas as pd

ROOT = Path(".")

CLASS_NAMES = {
    0: "Candyapple",
    1: "Namwa",
    2: "Namwadam",
    3: "Homthong",
    4: "Nak",
    5: "Thepphanom",
    6: "Kai",
    7: "Lepchanggud",
    8: "Ngachang",
    9: "Huamao"
}

stats = defaultdict(lambda: {
    "train": 0,
    "valid": 0,
    "test": 0
})

for split in ["train", "val", "test"]:

    label_dir = ROOT / "labels" / split

    for txt_file in label_dir.glob("*.txt"):

        with open(txt_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        # Hard negative image
        if len(lines) == 0:
            continue

        # ใช้ class แรกของภาพ
        cls_id = int(lines[0].split()[0])

        split_name = "valid" if split == "val" else split

        stats[cls_id][split_name] += 1

rows = []

for cls_id in sorted(CLASS_NAMES.keys()):

    train_count = stats[cls_id]["train"]
    valid_count = stats[cls_id]["valid"]
    test_count = stats[cls_id]["test"]

    rows.append({
        "class_name": CLASS_NAMES[cls_id],
        "train": train_count,
        "valid": valid_count,
        "test": test_count,
        "total": train_count + valid_count + test_count
    })

df = pd.DataFrame(rows)

total_row = {
    "class_name": "Total",
    "train": df["train"].sum(),
    "valid": df["valid"].sum(),
    "test": df["test"].sum(),
    "total": df["total"].sum()
}

df = pd.concat(
    [df, pd.DataFrame([total_row])],
    ignore_index=True
)

print("\nClass Distribution")
print(df)

output_file = "dataset_statistics.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved: {output_file}")
