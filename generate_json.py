import os, json

image_dir = 'images'
output_file = 'images.json'

valid = ['.png', '.jpg', '.jpeg', '.webp']
images = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in valid]
with open(output_file, 'w', encoding='utf-8') as out:
    json.dump(images, out, indent=2)

print(f"✔ {output_file} updated with {len(images)} image(s).")