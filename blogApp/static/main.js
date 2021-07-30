let toggle = document.querySelector("#header .toggle-button");
let collapse = document.querySelectorAll("#header .collapse");

toggle.addEventListener('click', function(){
   collapse.forEach(col => col.classList.toggle("collapse-toggle"));
})

// With masonry

new Masonry("#posts .grid", {
    itemSelector : '.grid-item',
    gutter : 20
});

// Swiper library initialization

new Swiper('.swiper-container',{
    direction : "horizontal",
    loop : true,
    slidesPerView : 5,
    autoplay : {
        delay: 1000
    },

    // Responsive breakpoints
    breakpoints : {
       '@0' : {
           slidesPerView: 2
       }, 

       // greater than 888px

       '@1.00' : {
           slidesPerView: 3
       }, 

       // greater than 1110px

       '@1.25' : {
           slidesPerView: 4
       }, 

       // greater than 1330px

       '@1.50' : {
           slidesPerView: 5
       }
    }
})

// Sticky Navigation bar
window.onscroll = function(){myFunction()};

let navbar = document.getElementById("header");


let sticky = navbar.offsetTop;

// sticky function

function myFunction(){
    if(window.pageXOffset >= sticky){
        navbar.classList.add("sticky");
    }else{
        navbar.classList.remove("sticky");
    }
}