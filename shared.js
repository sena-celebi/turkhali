
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

async function goRandom() {
  const response = await fetch('pages.json');
  const pages = await response.json();
  const pick = pages[Math.floor(Math.random() * pages.length)];
  location.href = pick + ".html";
}
