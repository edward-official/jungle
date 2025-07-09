$(document).ready(function (response) {
  displayMovies();
});

let isHiddenConsidered = false;
let isLikeOrderPrior = true;
let yearOrder = -1;
let likeOrder = -1;

function displayMovies() {
  $("#movie-container").empty();
  $.ajax({
    type: "GET",
    url: "/listup",
    data: {
      isLikeOrderPrior: isLikeOrderPrior,
      yearOrder: yearOrder,
      likeOrder: likeOrder,
    },
    success: function (response) {
      $("#movie-container").cl;
      let movies = response["movies"];
      for (let index = 0; index < movies.length; index++) {
        let movie = movies[index];
        if (movie["hidden"] == !isHiddenConsidered) continue;
        let movieID = movie["_id"];
        console.log(typeof movieID);
        let title = movie["title"];
        let releasedYear = movie["releasedYear"];
        let runningTime = movie["runningTime"];
        let likes = movie["likes"];
        let buttons;
        if (isHiddenConsidered) {
          buttons = `<button class="button-1" onclick="buttonRestore('${movieID}')">♻️ restore</button>
                    <button class="button-1" onclick="buttonDelete('${movieID}')">❌ delete</button>`;
        } else {
          buttons = `<button class="button-1" onclick="buttonLike('${movieID}')">👍 ${likes}</button>
                    <button class="button-1" onclick="buttonHide('${movieID}')">❌ hide</button>`;
        }
        let appendee = `<div class="movie-element">
                          <div>
                            <span class="movie-title">${title}</span>
                            <span class="movie-likes">${buttons}</span>
                          </div>
                          <div class="movie-releasedYear">${releasedYear}</div>
                          <div class="movie-runningTime">${runningTime}</div>
                        </div>`;
        $("#movie-container").append(appendee);
      }
    },
  });
}

function buttonLike(movieID) {
  console.log("like: " + movieID);
  $.ajax({
    type: "POST",
    url: "/like",
    data: { movieID: movieID },
    success: function (response) {
      console.log("success");
      displayMovies();
    },
  });
}

function buttonHide(movieID) {
  console.log("hide: " + movieID);
  $.ajax({
    type: "POST",
    url: "/hide",
    data: { movieID: movieID },
    success: function (response) {
      displayMovies();
    },
  });
}

function buttonRestore(movieID) {
  $.ajax({
    type: "POST",
    url: "/unhide",
    data: { movieID: movieID },
    success: function (response) {
      displayMovies();
    },
  });
}

function buttonDelete(movieID) {
  $.ajax({
    type: "POST",
    url: "/delete",
    data: { movieID: movieID },
    success: function (response) {
      displayMovies();
    },
  });
}

function convertMode() {
  isHiddenConsidered = !isHiddenConsidered;
  if (isHiddenConsidered) $("#button-mode").text("convert to visible movies");
  else $("#button-mode").text("convert to hidden movies");
  displayMovies();
}

function flipYearOrder() {
  yearOrder = yearOrder * -1;
  isLikeOrderPrior = false;
  displayMovies();
}

function flipLikeOrder() {
  likeOrder = likeOrder * -1;
  isLikeOrderPrior = true;
  displayMovies();
}
