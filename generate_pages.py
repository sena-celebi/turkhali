
import os
import json

# Paths
images_folder = "images"
pages_json_path = "pages.json"

# Template for the HTML page
page_template = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name}</title>
  <style>
    body {{
      background-color: #000;
      color: #fff;
      text-align: center;
      font-family: 'PT Serif', serif;
      font-style: italic;
      font-weight: bold;
    }}
    img {{
      max-width: 100%;
      height: auto;
      margin-top: 20px;
    }}
    a {{
      color: orange;
      margin: 0 10px;
    }}
    button {{
      background: none;
      border: none;
      color: white;
      text-decoration: underline;
      cursor: pointer;
      margin-top: 20px;
    }}
  </style>
</head>
<body>
  <h1 style="color:red;">turkhali.net</h1>
  <h2>#{name}</h2>
  <img src="images/{image}" alt="{name}">
  <div id="nav"></div>
  <script src="shared.js"></script>
  <script>setupPage("{name}");</script>
</body>
</html>"""

# Get all .png files in the images folder
image_files = [f for f in os.listdir(images_folder) if f.endswith(".png")]
page_names = [os.path.splitext(f)[0] for f in image_files]

# Save the HTML files
for name in page_names:
    html = page_template.format(name=name, image=f"{name}.png")
    with open(f"{name}.html", "w", encoding="utf-8") as f:
        f.write(html)

# Update pages.json
with open(pages_json_path, "w", encoding="utf-8") as f:
    json.dump(page_names, f)

print("✔ All pages generated and pages.json updated.")
