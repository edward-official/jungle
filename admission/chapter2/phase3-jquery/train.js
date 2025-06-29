function q1() {
  let text = $("#input-q1").val();
  console.log(text);
  if(text=="") alert("please enter something");
  else {
    alert(text);
    $("#input-q1").val("");
  }
}

function q2() {
  let text = $("#input-q2").val();
  if(text.includes("@")) {
    let domain = text.split("@")[1].split(".")[0];
    alert(domain);
  }
  else {
    alert("this is not a format of an email");
  }
}

function q3() {
  let text = $("#input-q3").val();
  let appendee = `<li>${text}</li>`;
  if(text!="") {
    $("#names-q3").append(appendee);
    $("#input-q3").val("");
  }
}

function q3_remove() {
  $("#names-q3").empty();
  $("#input-q3").val("");
}