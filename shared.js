
async function setupPage(currentPage) {
  const response = await fetch('pages.json');
  const pages = await response.json();
  const currentIndex = pages.indexOf(currentPage);
  const prev = currentIndex > 0 ? pages[currentIndex - 1] + ".html" : "#";
  const next = currentIndex < pages.length - 1 ? pages[currentIndex + 1] + ".html" : "#";

  document.getElementById("nav").innerHTML = `
    <a href="${prev}" id="prev">önceki</a>
    <a href="${next}" id="next">sonraki</a>
    <button onclick="goRandom()">rastgele</button>
  `;
}
<style>
    body {
      background-color: #000;
      color: #fff;
      text-align: center;
      font-family: 'PT Serif', serif;
      font-style: italic;
      font-weight: bold;
    }
    img {
      max-width: 100%;
      height: auto;
      margin-top: 20px;
    }
    a {
      color: orange;
      margin: 0 10px;
    }
    button {
      background: none;
      border: none;
      color: white;
      text-decoration: underline;
      cursor: pointer;
      margin-top: 20px;
    }
  </style>

async function goRandom() {
  const response = await fetch('pages.json');
  const pages = await response.json();
  const pick = pages[Math.floor(Math.random() * pages.length)];
  location.href = pick + ".html";
}
