$(document).ready(function () {
  console.log("ready");
  $.ajax({
    type: "GET",
    url: "/api/players",
    data: {},
    success: function (response) {
      // rendering the database information into the HTML code
      let players = response["players"];
      console.log(players);
      for (let index = 0; index < players.length; index++) {
        let playerName = players[index]["player_name"];
        let uniformNumber = players[index]["uniform_number"];
        if (index % 3 == 0) {
          $("#card-container").append(`<div class="row"></div>`);
        }
        $("#card-container .row:last-child").append(`<div class="col-sm-4">
                                                        <div class="card">
                                                          <div class="card-body">
                                                            <h5 class="card-title">${playerName}</h5>
                                                            <p class="card-text">${uniformNumber}</p>
                                                          </div>
                                                        </div>
                                                      </div>`);
        console.log("complete");
      }
    },
  });
});

function savePlayer() {
  let playerName = $("#player-name").val();
  let uniformNumber = $("#uniform-number").val();
  $("#player-name").val("");
  $("#uniform-number").val("");
  console.log(playerName, uniformNumber);
  $.ajax({
    type: "POST",
    url: "/save",
    data: { playerNameGive: playerName, uniformNumberGive: uniformNumber },
    success: function (response) {
      console.log("passing data to the flask application");
      window.location.reload();
    },
  });
}
