function clearFields() {
  document.getElementById("inputFName").value = "";
  document.getElementById("inputLName").value = "";
  document.getElementById("inputPhone").value = "";
  document.getElementById("inputEmail").value = "";
  document.getElementById("inputCourse").value = "";
  document.getElementById("inputAddress").value = "";
}

function removePhoto() {
  studentImg = document.getElementById("studentImage");
  isPhotoTrue = document.getElementById("photoTrue");

  studentImg.src = "/static/images/prof.jpg";
  isPhotoTrue.value = "false";
}

$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function () {
  $('[data-toggle="popover"]').popover();
});
