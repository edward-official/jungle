const Sort = {
  BY_LIKES: "likes",
  BY_VIEWERS: "viewers",
  BY_DATE: "date",
};

let sortMode = Sort.BY_LIKES;
let trashMode = false;

$(document).ready(function () {
  showMovie();
  displaySorter();
  displayTrashMode(trashMode);
});

function changeMode() {
  if (trashMode == false) trashMode = true;
  else trashMode = false;
  showMovie();
}

function showMovie() {
  $("#movie-box").empty();
  if (trashMode == false) {
    $.ajax({
      type: "GET",
      url: "/api/list",
      data: { sortMode: sortMode },
      success: function (response) {
        if (response["result"] != "success") {
          alert(sortMode + " 순으로 영화 목록 받아오기 실패!");
          return;
        }
        let movies = response["movies_list"];
        addMovieCards(movies, false);
      },
    });
  } else {
    $.ajax({
      type: "GET",
      url: "/api/trash",
      data: { sortMode: sortMode },
      success: function (response) {
        if (response["result"] != "success") {
          alert(sortMode + " 순으로 영화 목록 받아오기 실패!");
          return;
        }
        let movies = response["movies_list"];
        addMovieCards(movies, true);
      },
    });
  }
}

function addMovieCards(movies, trashMode) {
  for (let i = 0; i < movies.length; i++) {
    let movie = movies[i];
    let id = movie["_id"];
    let title = movie["title"];
    let viewers = movie["viewers"];
    let likes = movie["likes"];
    let openYear = movie["open_year"];
    let openMonth = movie["open_month"];
    let openDay = movie["open_day"];

    let cardContentHtml = `
      <!--<img src="https://cataas.com/cat" class="movie-poster"/>-->
      <span class="movie-title">${title}</span>
      <div>
        <span class="icon"><i class="fas fa-thumbs-up"></i></span>
        <span class="movie-likes">${likes}</span>
      </div>
      <span class="movie-viewers">누적관객수: ${viewers}명</span>
      <span class="movie-date">개봉일: ${openYear}-${openMonth}-${openDay}</span>
    `;

    let cardFooterHtml = "";
    if (trashMode == false) {
      cardFooterHtml = `
        <a href="#" onclick="likeMovie('${id}')">like</a>
        <a href="#" onclick="trashMovie()">bin</a>
      `;
    } else {
      cardFooterHtml = `
        <a href="#" onclick="restoreMovie()">restore</a>
        <a href="#" onclick="deleteMovie()">delete</a>
      `;
    }

    $("#movie-box").append(`
      <div class="card">
        ${cardContentHtml}
        ${cardFooterHtml}
      </div>
    `);
  }
}

function likeMovie(movieID) {
  alert(movieID);
  $.ajax({
    type: "POST",
    url: "/api/like",
    data: { _id: movieID },
    success: function (response) {
      if (response["result"] == "success") {
        alert("좋아요 완료!");
        showMovie();
      } else {
        alert("좋아요 실패ㅠㅠ");
      }
    },
  });
}

function trashMovie() {
  alert(
    "휴지통 보내기 기능을 직접 구현해보세요.\n서버 측에 API 를 추가 후 여기서 그 API 를 호출하면 됩니다."
  );
}

function restoreMovie() {
  alert(
    "휴지통에서 되살리기 기능을 직접 구현해보세요.\n서버 측에 API 를 추가 후 여기서 그 API 를 호출하면 됩니다."
  );
}

function deleteMovie() {
  alert(
    "휴지통에서 아주 삭제 기능을 직접 구현해보세요.\n서버 측에 API 를 추가 후 여기서 그 API 를 호출하면 됩니다."
  );
}

function changeSorter(newMode) {
  if (sortMode == newMode) {
    return;
  }
  sortMode = newMode;
  displaySorter();
  showMovie();
}

function displaySorter() {
  document.getElementById("sorter-likes").classList.remove("active");
  document.getElementById("sorter-viewers").classList.remove("active");
  document.getElementById("sorter-date").classList.remove("active");
}

function displayTrashMode(trashMode) {
  // trashMode 에 따라 "휴지통 보기" 또는 "휴지통 나가기" 가 출력 되게 구현해야 됩니다.
}
