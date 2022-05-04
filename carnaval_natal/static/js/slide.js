let slideIndex = 0;
showSlides();

function showSlides() {
  let slide = document.getElementById(slide);
  slide.style.backgroundImage= 'url(../img/slide/01.jpg);';
  setTimeout(showSlides, 10000); // Change image every 2 seconds
}