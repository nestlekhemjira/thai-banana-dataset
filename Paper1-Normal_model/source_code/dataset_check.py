import os

# Configuration
IMAGE_DIR = '../train/images'
LABEL_DIR = '../train/labels'

# Validate Dataset
missing_labels = []
missing_images = []

# Load Image Filenames
image_files = [
    os.path.splitext(f)[0]
    for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith(
        ('.jpg', '.jpeg', '.png')
    )
]

# Load Label Filenames
label_files = [
    os.path.splitext(f)[0]
    for f in os.listdir(LABEL_DIR)
    if f.lower().endswith('.txt')
]

# Check Missing Labels
for image_name in image_files:

    if image_name not in label_files:
        missing_labels.append(image_name)

# Check Missing Images
for label_name in label_files:

    if label_name not in image_files:
        missing_images.append(label_name)

# Print Results
print(f'Total images: {len(image_files)}')
print(f'Total labels: {len(label_files)}')

print(f'Missing labels: {len(missing_labels)}')
print(f'Missing images: {len(missing_images)}')

# Display Missing Labels
if missing_labels:

    print('\nImages without labels:')

    for item in missing_labels:
        print(item)

# Display Missing Images
if missing_images:

    print('\nLabels without images:')

    for item in missing_images:
        print(item)
