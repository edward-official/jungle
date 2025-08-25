function opening() {
  console.log("page loaded");
}
$(document).ready(opening());

function login() {
  let loginForm = $("#log-in");
  let id = loginForm.find("#id");
  let pw = loginForm.find("#pw");

  $.ajax({
    type: "GET",
    url: "/login",
    data: { id: id.val() },
    success: function (response) {
      alert("api");
    },
  });

  id.val("");
  pw.val("");
}

function unveilSignup() {
  let loginForm = $("#log-in");
  let signupForm = $("#sign-up");
  loginForm.addClass("hidden");
  signupForm.removeClass("hidden");
}

function cancelSignup() {
  let loginForm = $("#log-in");
  let signupForm = $("#sign-up");
  loginForm.removeClass("hidden");
  signupForm.addClass("hidden");
}
