var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("pr-img-mySlides");
  var dots = document.getElementsByClassName("pr-img-demo");
  var captionText = document.getElementById("pr-img-caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" pr-img-active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " pr-img-active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}