$(document).ready(opening());
function opening() {
  console.log("page loaded");
}

function logIn() {
  let logIn = $("#log-in");

  let tagIdEmail = logIn.find("#id-email");
  let tagPw = logIn.find("#pw");

  let idEmail = tagIdEmail.val();
  let pw = tagPw.val();

  console.log(idEmail);
  console.log(pw);

  tagIdEmail.val("");
  tagPw.val("");
}
