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

function checkPass() {
  var pass1 = document.getElementById("password1").value;
  var pass2 = document.getElementById("password2").value;
  var div = document.getElementById("warning-password");
  if (pass1 != "") {
    if (pass1 != pass2) {
      div.innerHTML = "Passwords doesn't match..Please try again.";
    } else {
      div.innerHTML = "";
    }
  }
}
