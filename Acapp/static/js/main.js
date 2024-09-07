new WOW().init();

// Cursor

let innerCursor = document.querySelector(".inner-cursor");
let outerCursor = document.querySelector(".outer-cursor");

document.addEventListener("mousemove", moveCursor);

function moveCursor(e){
    let x = e.clientX;
    let y = e.clientY;
    innerCursor.style.left = `${x}px`;
    innerCursor.style.top = `${y}px`;
    outerCursor.style.left = `${x}px`;
    outerCursor.style.top = `${y}px`;
}
let links = Array.from(document.querySelectorAll("a"));
links.forEach(link => {
    link.addEventListener("mouseover", () => {
        innerCursor.classList.add("grow");
    });
    link.addEventListener("mouseleave", () => {
        innerCursor.classList.remove("grow");
    });
});

// Navbar
// Function to handle the container class based on window width
function toggleMobileMenu() {
    const toggler = document.querySelector('.navbar-toggler');
    const collapse = document.querySelector('.navbar-collapse');
    
    // Toggle 'active' class for the button
    toggler.classList.toggle('active');
    
    // Toggle 'show' class for the navbar collapse
    collapse.classList.toggle('show');
}

// Attach event listener on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
    const toggler = document.querySelector('.navbar-toggler');
    
    // Attach click event to the toggler
    if (toggler) {
        toggler.addEventListener('click', toggleMobileMenu);
    }
});
  
      // Facts counter
      $('.counter').counterUp({
          delay: 10,
          time: 2000
      });

      
      $(document).ready(function() {
        $(".gallery-link").click(function() {
            var filter = $(this).data("filter");
    
            $(".gallery-link").removeClass("active");
            $(this).addClass("active");
    
            if (filter == "all") {
                $("#gallery .col-lg-4").show();
            } else {
                $("#gallery .col-lg-4").hide();
                $("#gallery .col-lg-4[data-category='" + filter + "']").show();
            }
        });
    });
    // preloader js code

document.addEventListener("DOMContentLoaded", function() {
    showPreloader(); 
    setTimeout(hidePreloader, 1500); 
    document.body.style.overflow = "hidden";
});

function showPreloader() {
    var preloader = document.getElementById("preloader");
    if (preloader) {
        preloader.style.display = "flex";
    }
}

function hidePreloader() {
    var preloader = document.getElementById("preloader");
    if (preloader) {
        preloader.style.display = "none";
        document.body.style.overflow = ""; 
    }
}
window.addEventListener("load",function(){
    this.setTimeout(
        function open(e){
            document.querySelector(".otp-Form").style.display = "block";
        },
        3000
    )
});

document.querySelector('.exitBtn').addEventListener("click",function(){
    document.querySelector(".otp-Form").style.display = "none";
});


document.addEventListener('DOMContentLoaded', function () {
    const toggler = document.querySelector('.navbar-toggler');
    const navbarNav = document.querySelector('.navbar-nav');
  
    toggler.addEventListener('click', function () {
      navbarNav.classList.toggle('show');
    });
  });
  
//   Full screen image
function openFullScreen(imgElement) {
    var modal = document.getElementById("fullScreenModal");
    var modalImg = document.getElementById("fullScreenImg");
    modal.style.display = "block";
    modalImg.src = imgElement.src;
}

function closeFullScreen() {
    var modal = document.getElementById("fullScreenModal");
    modal.style.display = "none";
}
