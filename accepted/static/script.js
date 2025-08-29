function opening() {
  console.log("page loaded");
}
$(document).ready(opening());

function login() {
  let loginHolder = $("#log-in");
  let id = loginHolder.find("#id");
  let pw = loginHolder.find("#pw");

  if (id.val() == "" || pw.val() == "") {
    alert("id and pw must be entered");
    id.val("");
    pw.val("");
    return;
  }

  $.ajax({
    type: "POST",
    url: "/login",
    data: { id: id.val(), pw: pw.val() },
  }).done(function (response) {
    let isAuthenticated = response["isAuthenticated"];
    if (isAuthenticated) {
      moveToQuestions();
    } else {
      alert("login denied");
    }
  });

  id.val("");
  pw.val("");
}

function moveToSignup() {
  let loginHolder = $("#log-in");
  let signupHolder = $("#sign-up");
  loginHolder.addClass("hidden");
  signupHolder.removeClass("hidden");
}

function backToLogin() {
  let loginHolder = $("#log-in");
  let signupHolder = $("#sign-up");
  loginHolder.removeClass("hidden");
  signupHolder.addClass("hidden");
}

function moveToQuestions() {
  let loginHolder = $("#log-in");
  let signupHolder = $("#sign-up");
  let questions = $("#questions");
  if (!loginHolder.hasClass("hidden")) loginHolder.addClass("hidden");
  if (!signupHolder.hasClass("hidden")) signupHolder.addClass("hidden");
  questions.removeClass("hidden");
}

function signup() {
  let signupHolder = $("#sign-up");
  let id = signupHolder.find("#id-sign-up").val();
  let pw1 = signupHolder.find("#pw-sign-up").val();
  let pw2 = signupHolder.find("#pw-check-sign-up").val();
  if (pw1 != pw2) {
    alert("disqualified on password check up");
    signupHolder.find("#id-sign-up").val("");
    signupHolder.find("#pw-sign-up").val("");
    signupHolder.find("#pw-check-sign-up").val("");
    return;
  }

  $.ajax({
    type: "POST",
    url: "/signup",
    data: { id: id.val(), pw: pw1.val() },
    success: function () {
      alert("sign up completed!");
      signupHolder.find("#id-sign-up").val("");
      signupHolder.find("#pw-sign-up").val("");
      signupHolder.find("#pw-check-sign-up").val("");
    },
  });
}
