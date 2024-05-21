const body = document.querySelector("body"),
section=document.getElementById("tranding"),
sidebar=body.querySelector(".sidebar"),
toggle=body.querySelector(".toggle"),
searchBtn=body.querySelector(".search-box"),
modeSwitch=body.querySelector(".toggle-switch"),
modeText=body.querySelector(".mode-text");

toggle.addEventListener("click",()=>{
    sidebar.classList.toggle("close");
});
modeSwitch.addEventListener("click",()=>{
    body.classList.toggle("dark");
    section.classList.toggle("dark");
    if(body.classList.contains("dark")){
        modeText.innerText="Light Mode"
    }else{
        modeText.innerText="Dark Mode"
    }
});

var TrandingSlider = new Swiper('.tranding-slider', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });



