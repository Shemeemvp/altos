$(".owl-carousel").owlCarousel({
  loop: true,
  margin: 10,
  autoplay: true,
  autoplayTimeout: 1000,
  autoplayHoverPause: false,
  responsive: {
    0: {
      items: 3,
    },
    300: {
      items: 4,
    },
    600: {
      items: 5,
    },
    1000: {
      items: 7,
    },
    1250: {
      items: 9,
    },
  },
});
$(document).ready(function () {
  $(".wish-icon i").click(function () {
    $(this).toggleClass("fa-heart fa-heart-o");
  });
});
