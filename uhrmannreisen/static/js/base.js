const cookie = document.querySelector("#menu-cookie");
const menu = document.querySelector("#navbar-cta");

function toggleMenu() {
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
  } else {
    menu.classList.add("hidden");
  }
}

function toggle() {
  const menu = document.querySelector("#menu");
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
    menu.classList.add("absolute");
  } else {
    menu.classList.add("hidden");
    menu.classList.remove("absolute");
  }
}


function cookieRefresh() {
  if (cookieselect == null) {
    cookie.classList.add("block");
    cookie.classList.remove("hidden");
  } else {
    cookie.classList.add("hidden");
  }
}

function acceptCookie() {
  document.cookie =
    "Cookie-Consent=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Analytic=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Font=true; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  location.reload();
  cookieRefresh();
}

function refuseCookie() {
  document.cookie =
    "Cookie-Consent=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Analytic=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  document.cookie =
    "Cookie-Font=false; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  location.reload();
  cookieRefresh();
}

cookieRefresh();

if (!window.location.pathname.includes("cms")) {
  // Swiper Slider
  const swiper = new Swiper('.swiper', {
    speed: 400,
    spaceBetween: 100,
    loop: true, // Aktiviert das endlose Swipen
    autoplay: {
      delay: 5000,
      disableOnInteraction: false, // Autoplay nach Benutzung der Buttons nicht deaktivieren
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true, // Bullets anklickbar machen
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    scrollbar: {
      el: '.swiper-scrollbar',
      draggable: true,
    },
  });
}