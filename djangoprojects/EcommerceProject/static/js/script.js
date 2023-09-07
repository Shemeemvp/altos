function confirmDelete(prodId) {
  swal({
    title: "Are you sure?",
    text: "Once deleted, you will not be able to recover this product's data!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/remove-product/0".replace("0", parseInt(prodId));
    } else {
      swal("Operation Aborted!");
    }
  });
}
function deleteCategory(catId) {
  swal({
    title: "Are you sure?",
    text: "Once deleted, category and respective products will be removed!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/remove-category/0".replace("0", parseInt(catId));
    } else {
      swal("Operation Aborted!");
    }
  });
}

function deleteUser(userId) {
  swal({
    title: "Are you sure?",
    text: "Once deleted, user and order details of the User will be removed!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/remove-user/0".replace("0", parseInt(userId));
    } else {
      swal("Operation Aborted!");
    }
  });
}

function dispatchOrder(orderId) {
  swal({
    title: "Are you sure?",
    text: "The Order will be marked as dispatched!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDispatch) => {
    if (willDispatch) {
      window.location.href = "/dispatch-order/0".replace("0", parseInt(orderId));
    } else {
      swal("Operation Aborted!");
    }
  });
}

function deleteOrder(orderId) {
  swal({
    title: "Are you sure?",
    text: "Once deleted, the order details are permanently removed!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/remove-order/0".replace("0", parseInt(orderId));
    } else {
      swal("Operation Aborted!");
    }
  });
}
function deliverOrder(orderId) {
  swal({
    title: "Are you sure?",
    text: "The Order will be marked as delivered!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      window.location.href = "/deliver-order/0".replace("0", parseInt(orderId));
    } else {
      swal("Operation Aborted!");
    }
  });
}
// function dispatchOrder(orderId) {
//   const swalWithBootstrapButtons = swal.mixin({
//     customClass: {
//       confirmButton: "btn btn-success",
//       cancelButton: "btn btn-danger",
//     },
//     buttonsStyling: false,
//   });

//   swalWithBootstrapButtons
//     .fire({
//       title: "Are you sure?",
//       text: "The Order will be marked as dispatched!",
//       icon: "warning",
//       showCancelButton: true,
//       confirmButtonText: "Yes, Proceed!",
//       cancelButtonText: "No, Hold!",
//       reverseButtons: true,
//     })
//     .then((result) => {
//       if (result.isConfirmed) {
//         window.location.href = "/dispatch-order/0".replace(
//           "0",
//           parseInt(orderId)
//         );
//         swalWithBootstrapButtons.fire(
//           "Dispatched!",
//           "The order has been dispatched successfully.",
//           "success"
//         );
//       } else if (
//         /* Read more about handling dismissals below */
//         result.dismiss === Swal.DismissReason.cancel
//       ) {
//         swalWithBootstrapButtons.fire(
//           "Cancelled",
//           "Operation Aborted",
//           "error"
//         );
//       }
//     });
// }
