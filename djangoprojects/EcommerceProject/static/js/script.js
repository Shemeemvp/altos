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
