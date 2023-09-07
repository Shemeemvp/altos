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

function changeQuantity(cartId, prodId, count) {
  var incCount = count;
  var display = parseInt(cartId);
  //   let quantity = $("#" + display).val();
  let quantity = document.getElementById("qnt" + display).innerHTML;
  var token = $("input[name = csrfmiddlewaretoken]").val();
  $.ajax({
    method: "POST",
    url: "/change-product-quantity",
    data: {
      cart: cartId,
      product: prodId,
      count: incCount,
      quantity: quantity,
      csrfmiddlewaretoken: token,
    },
    success: (response) => {
      $("#qnt" + display).html(response.qty);
      $("#price" + display).html(response.totPrice);
      $("#cart-total").html(response.sum);
      $("#sum-total").html(response.sum);
      if (response.qty == 1 || response.qty == 2) {
        location.reload();
      }
    },
  });
}

// document.getElementById('netamount').
window.onload = () => {
  var sum = parseInt(document.getElementById("subtotal").innerHTML);
  var netSum = sum + 20;
  $("#netamount").html(netSum);
  document.getElementById("netamountInput").value = netSum;
};

function removeCartProduct(prodId) {
  swal({
    title: "Are you sure?",
    text: "Once deleted, item will be removed from the cart!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/remove-cart-item/0".replace(
        "0",
        parseInt(prodId)
      );
    } else {
      swal("Operation Aborted!");
    }
  });
}

function addToCart(productId) {
  var prodId = parseInt(productId);
  var token = $("input[name = csrfmiddlewaretoken]").val();
  $.ajax({
    method: "POST",
    url: "/add-to-cart",
    data: {
      product: prodId,
      csrfmiddlewaretoken: token,
    },
    success: (response) => {
      //   alert("Item Added");
      $("#cart-count").html(response.cartCount);
      $("#add-to-cart"+prodId).html(`<i class="fa fa-check mr-2"></i>Added to Cart`)
      $("#addtocart"+prodId).html(`<i class="fa fa-check mr-2"></i>Added to Cart`)
      $("#adbtn"+prodId).html(`<i class="fa fa-check mr-2"></i>Added to Cart`)
      $("#addButton"+prodId).html(`<i class="fa fa-check mr-2"></i>Added to Cart`)
    },
  });
}
