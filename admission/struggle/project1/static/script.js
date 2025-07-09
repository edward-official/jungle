$(document).ready(function (response) {
  $.ajax({
    type: "GET",
    url: "/listup",
    data: {},
    success: function (response) {
      let movies = response["movies"];
      displayMovies(movies);
    },
  });
});

function displayMovies(movies) {
  for (let index = 0; index < movies.length; index++) {
    let movie = movies[index];
    if (movie["hidden"]) continue;
    let movieID = movie["_id"];
    let title = movie["title"];
    let releasedYear = movie["releasedYear"];
    let runningTime = movie["runningTime"];
    let likes = movie["likes"];
    let appendee = `<div class="movie-element">
                      <div>
                        <span class="movie-title">${title}</span>
                        <span class="movie-likes">
                          <button class="button-likes" onclick="buttonLike('${movieID}')">👍 ${likes}</button>
                          <button class="button-hide" onclick="buttonHide('${movieID}')">❌ hide</button>
                        </span>
                      </div>
                      <div class="movie-releasedYear">${releasedYear}</div>
                      <div class="movie-runningTime">${runningTime}</div>
                    </div>`;
    $("#movie-container").append(appendee);
  }
}

function buttonLike(movieID) {
  console.log("like: " + movieID);
}

function buttonHide(movieID) {
  console.log("hide: " + movieID);
}
