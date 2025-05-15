import os

# Klasörün içindeki resimleri al
image_folder = "images"
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])
base_names = [os.path.splitext(f)[0] for f in image_files]

template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>turkhali.net</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Serif:400,400i,700,700i&display=swap" />
  <style>
    body {{
      background-color: #000;
      color: #fff;
      text-align: center;
      font-family: "PT Serif", serif;
      font-weight: bold;
      font-style: italic;
    }}
    img {{
      margin: 20px auto;
      display: block;
      max-width: 100%;
      height: auto;
      height: 650px;
    }}
    h1 {{ color: red; }}
    a {{ color: orange; padding: 0 5px; }}
    button {{
      border: none;
      background: none;
      color: inherit;
      text-decoration: underline;
      cursor: pointer;
    }}
    @media screen and (max-width: 768px) {{
      img {{
        width: 100vw;
        height: 100%;
        object-fit: contain;
      }}
    }}
  </style>
</head>
<body>
  <h1>turkhali.net</h1>
  <h2>#{title}</h2>
  {nav_links}
  <img src="images/{img_file}" alt="{title}" />
  <button id="random-button">rastgele</button>
  <script>
    document.addEventListener("keydown", function (event) {{
      if (event.keyCode === 37 && document.getElementById("previous")) {{
        window.location.href = document.getElementById("previous").href;
      }}
      if (event.keyCode === 39 && document.getElementById("next")) {{
        window.location.href = document.getElementById("next").href;
      }}
    }});
    const randomButton = document.getElementById("random-button");
    randomButton.addEventListener("click", function () {{
      const pages = {pages};
      const randomPage = pages[Math.floor(Math.random() * pages.length)];
      window.location.href = randomPage + ".html";
    }});
  </script>
</body>
</html>
"""

for i, name in enumerate(base_names):
    img_file = image_files[i]
    prev_page = f"{base_names[i-1]}.html" if i > 0 else ""
    next_page = f"{base_names[i+1]}.html" if i < len(base_names)-1 else ""

    nav_links = ""
    if prev_page:
        nav_links += f'<a href="{prev_page}" id="previous">önceki</a>'
    if next_page:
        nav_links += f'<a href="{next_page}" id="next">sonraki</a>'

    html = template.format(
        title=name,
        img_file=img_file,
        nav_links=nav_links,
        pages=base_names
    )

    with open(f"{name}.html", "w", encoding="utf-8") as f:
        f.write(html)

# index.html'i ilk halı sayfasıyla aynı yap
with open("index.html", "w", encoding="utf-8") as index_f:
    with open(f"{base_names[0]}.html", "r", encoding="utf-8") as first_page:
        index_f.write(first_page.read())

print("✅ Tüm HTML dosyaları oluşturuldu!")