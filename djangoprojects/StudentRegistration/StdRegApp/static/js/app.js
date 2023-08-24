function clearFields() {
  document.getElementById("inputFName").value = "";
  document.getElementById("inputLName").value = "";
  document.getElementById("inputPhone").value = "";
  document.getElementById("inputEmail").value = "";
  document.getElementById("inputCourse").value = "";
  document.getElementById("inputAddress").value = "";
}

$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function () {
  $('[data-toggle="popover"]').popover();
});
