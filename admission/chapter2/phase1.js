function proceed(message) {
  console.log("\n💻 " + message);
}


proceed("split");
let gmail = "something@google.com";
console.log(gmail);

let domain = gmail.split("@")[1].split(".")[0];
console.log(domain);

let naverMail = gmail.split("google").join("naver");
console.log(naverMail);


proceed("array");
let containerList = ["index zero", 1];
console.log(containerList);

containerList.push(["inner list", 1]);
console.log(containerList);

let doubledList = containerList.concat(containerList);
console.log(doubledList);
console.log("LENGTH: " + doubledList.length);


proceed("dictionary");
let dictionary = {
  "year": 2025,
  "comment": "dictionary looks like json",
}
console.log(dictionary);


proceed("closing");
let players = [
  {"name": "raya", "rating": 4},
  {"name": "white", "rating": 5},
  {"name": "saliba", "rating": 4},
  {"name": "rice", "rating": 5},
  {"name": "saka", "rating": 5},
  {"name": "havertz", "rating": 3},
  {"name": "sterling", "rating": 2},
  {"name": "merino", "rating": 3},
  {"name": "pepe", "rating": 1},
];
for(let index=0; index<players.length; index++) {
  if(players[index].rating<=3) console.log("❌" + players[index].name + " is not a successful player");
  else console.log("🎉" + players[index].name + " is a successful player");
}