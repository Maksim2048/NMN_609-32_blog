let menuBtn = document.querySelector(".menu-btn");
let menu = document.querySelector(".references");
let block = document.querySelector(".menu__block");

menuBtn.addEventListener("click", function () {
  menuBtn.classList.toggle("btn__active");
  menu.classList.toggle("references__active");
  block.classList.toggle("menu__block__active");
        block.classList.toggle("menu__block__active");
});