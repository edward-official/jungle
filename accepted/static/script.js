function opening() {
  console.log("page loaded");
}
$(document).ready(opening());

function moveToSignup() {
  let loginHolder = $("#login");
  let signupHolder = $("#signup");
  loginHolder.addClass("hidden");
  signupHolder.removeClass("hidden");
}

function backToLogin() {
  let loginHolder = $("#login");
  let signupHolder = $("#signup");
  loginHolder.removeClass("hidden");
  signupHolder.addClass("hidden");
}

function moveToQuestions() {
  let nextQuestion = `<fieldset>
          <legend>What does "dzien dobry" mean?</legend>

          <label class="display-block">
            <input type="radio" name="choices" />
            Good morning!
          </label>

          <label class="display-block">
            <input type="radio" name="choices" />
            How was your sleep?
          </label>

          <label class="display-block">
            <input type="radio" name="choices" />
            Nice to meet you!
          </label>

          <label class="display-block">
            <input type="radio" name="choices" />
            Can I help you?
          </label>

          <button class="display-block">submit</button>
        </fieldset>`;
  window.location.href = "/questions";
} // component function

function login() {
  let loginHolder = $("#login");
  let userId = loginHolder.find("#userid");
  let password = loginHolder.find("#password");

  if (userId.val() == "" || password.val() == "") {
    alert("user ID and password must be entered");
    userId.val("");
    password.val("");
    return;
  }

  $.ajax({
    type: "POST",
    url: "/login",
    data: { userId: userId.val(), password: password.val() },
  }).done(function (response) {
    let isRequestAccepted = response["isRequestAccepted"];
    if (isRequestAccepted) {
      userId.val("");
      password.val("");
      moveToQuestions();
    } else {
      userId.val("");
      password.val("");
      alert("login denied");
    }
  });
}

function signup() {
  let signupHolder = $("#signup");
  let userIdElement = signupHolder.find("#userid-signup");
  let password1Element = signupHolder.find("#password-signup-1");
  let password2Element = signupHolder.find("#password-signup-2");

  let targets = [userIdElement, password1Element, password2Element];
  for (let target of targets) {
    if (target.val().trim() == "") {
      alert("all the blanks have to be entered");
      return;
    }
  }

  $.ajax({
    type: "POST",
    url: "/signup",
    data: {
      userId: userIdElement.val(),
      password1: password1Element.val(),
      password2: password2Element.val(),
    },
  }).done(function (response) {
    let isRequestAccepted = response["isRequestAccepted"];
    if (isRequestAccepted) {
      alert("sign up success!");
    } else {
      let reason = response["reason"];
      let message = "sign up failed (" + reason + ") !!";
      alert(message);
    }
    userIdElement.val("");
    password1Element.val("");
    password2Element.val("");
    backToLogin();
  });
}
