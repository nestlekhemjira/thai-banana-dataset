from pathlib import Path

ROOT = Path(".")

print("=" * 60)
print("Thai Banana Cultivar Detection Dataset Checker")
print("=" * 60)

required_dirs = [
    ROOT / "images" / "train",
    ROOT / "images" / "val",
    ROOT / "images" / "test",
    ROOT / "labels" / "train",
    ROOT / "labels" / "val",
    ROOT / "labels" / "test"
]

print("\nChecking directory structure...")

missing_dirs = []

for d in required_dirs:
    if not d.exists():
        missing_dirs.append(str(d))

if missing_dirs:
    print("\nMissing directories:")
    for d in missing_dirs:
        print(" -", d)
    exit()

print("Directory structure OK")

total_images = 0
total_labels = 0
banana_images = 0

missing_label_files = []
orphan_label_files = []

for split in ["train", "val", "test"]:

    image_dir = ROOT / "images" / split
    label_dir = ROOT / "labels" / split

    image_stems = set()
    label_stems = set()

    image_files = (
        list(image_dir.glob("*.jpg")) +
        list(image_dir.glob("*.jpeg")) +
        list(image_dir.glob("*.png")) +
        list(image_dir.glob("*.JPG")) +
        list(image_dir.glob("*.JPEG")) +
        list(image_dir.glob("*.PNG"))
    )

    label_files = list(label_dir.glob("*.txt"))

    total_images += len(image_files)
    total_labels += len(label_files)

    for img in image_files:
        image_stems.add(img.stem)

    for lbl in label_files:
        label_stems.add(lbl.stem)

        with open(lbl, "r", encoding="utf-8") as f:
            lines = [x.strip() for x in f if x.strip()]

        if len(lines) > 0:
            banana_images += 1

    missing = image_stems - label_stems
    orphan = label_stems - image_stems

    for x in sorted(missing):
        missing_label_files.append(f"{split}/{x}")

    for x in sorted(orphan):
        orphan_label_files.append(f"{split}/{x}")

    print(f"\n[{split}]")
    print(f"Images : {len(image_files)}")
    print(f"Labels : {len(label_files)}")

hard_negative_images = total_images - banana_images

print("\n" + "=" * 60)
print("Dataset Summary")
print("=" * 60)

print(f"Total Images        : {total_images}")
print(f"Banana Images       : {banana_images}")
print(f"Hard Negative Images: {hard_negative_images}")

print("\nIntegrity Check")

print(f"Images without labels : {len(missing_label_files)}")
print(f"Labels without images : {len(orphan_label_files)}")

if len(missing_label_files) == 0 and len(orphan_label_files) == 0:
    print("Dataset integrity check PASSED")
else:
    print("Dataset integrity issues detected")

print("\nDone")
