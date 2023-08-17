let subBtn = document.getElementById("submit");
let paragraph = document.getElementById("end");

subBtn.addEventListener("click", () => {
  console.log("clicked");
  paragraph.innerHTML = "PDFs merged!";
});
