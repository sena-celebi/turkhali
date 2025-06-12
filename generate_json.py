
import os
import json

images_folder = 'images'
output_file = 'images.json'

image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(image_files, f)

print(f"✔ Created {output_file} with {len(image_files)} images.")
