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
      alert("log in interface");
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

function signup() {
  let signupForm = $("#sign-up");
  let id = signupForm.find("#id-sign-up").val();
  let pw1 = signupForm.find("#pw-sign-up").val();
  let pw2 = signupForm.find("#pw-check-sign-up").val();
  if (pw1 != pw2) {
    alert("disqualified on password check up");
    signupForm.find("#id-sign-up").val("");
    signupForm.find("#pw-sign-up").val("");
    signupForm.find("#pw-check-sign-up").val("");
    return;
  }

  $.ajax({
    type: "POST",
    url: "/signup",
    data: { id: id.val(), pw: pw1.val() },
    success: function () {
      alert("sign up completed!");
      signupForm.find("#id-sign-up").val("");
      signupForm.find("#pw-sign-up").val("");
      signupForm.find("#pw-check-sign-up").val("");
    },
  });
}
