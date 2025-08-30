function opening() {
  console.log("page loaded");
}
$(document).ready(opening());

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
} // component function

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
    let isRequestAccepted = response["isRequestAccepted"];
    if (isRequestAccepted) {
      moveToQuestions();
    } else {
      alert("login denied");
    }
  });

  id.val("");
  pw.val("");
}

function signup() {
  let signupHolder = $("#sign-up");
  let idElement = signupHolder.find("#id-sign-up");
  let pw1Element = signupHolder.find("#pw-sign-up");
  let pw2Element = signupHolder.find("#pw-check-sign-up");

  $.ajax({
    type: "POST",
    url: "/signup",
    data: { id: idElement.val(), pw1: pw1Element.val(), pw2: pw2Element.val() },
  }).done(function (response) {
    let isRequestAccepted = response["isRequestAccepted"];
    if (isRequestAccepted) {
      alert("sign up success!");
    }
    idElement.val("");
    pw1Element.val("");
    pw2Element.val("");
    backToLogin();
  });
}
