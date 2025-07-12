$(document).ready(function (response) {
  updatePage();
});

function updatePage() {
  $.ajax({
    type: "GET",
    url: "/update/page",
    data: {},
    success: function (response) {
      $("#card-list").empty();
      let memos = response["memos"];
      for (let index = 0; index < memos.length; index++) {
        let memo = memos[index];
        let memoID = memo["_id"];
        let html = `<div class="card">
                      <h3 class="card-title">${memo["title"]}</h3>
                      <p class="card-text">${memo["text"]}</p>
                      <p class="card-likes">${memo["likes"]}</p>
                      <div class="button-group" style="display: flex;">
                        <div class="edit-button button" onclick="buttonEdit(this, '${memoID}')">수정</div>
                        <div class="delete-button button" onclick="buttonDelete('${memoID}')">삭제</div>
                        <div class="link-like button" onclick="buttonLike('${memoID}')">좋아요! 👍</div>
                      </div>
                    </div>`;
        $("#card-list").append(html);
      }
    },
  });
}

function submitMemo() {
  let title = $("#memo-title").val();
  let content = $("#memo-content").val();
  if (title == "") {
    alert("nothing entered");
    return;
  }
  $.ajax({
    type: "POST",
    url: "/save/memo",
    data: { title: title, content: content },
    success: function (response) {
      if (response["result"] == "ignored") {
        alert("ignored: identical title already exists");
      }
      $("#memo-title").val("");
      $("#memo-content").val("");
      updatePage();
    },
  });
}

function buttonEdit(targetButton, memoID) {
  let targetCard = $(targetButton).closest(".card");
  targetCard.empty();
  let html = `<form class="edit-form">
                <input class="new-title" placeholder="제목을 입력하세요" />
                <textarea class="new-text" placeholder="내용을 입력하세요"></textarea>
                <div class="button-group" style="display: flex;">
                  <div class="save-button button" type="submit" onclick="submitEdit(this, '${memoID}')">저장하기</div>
                  <div class="cancel-button button" onclick="cancelEdit(this, '${memoID}')">취소</div>
                </div>
              </form>`;
  targetCard.append(html);
}

function submitEdit(targetButton, memoID) {
  let targetCard = $(targetButton).closest(".card");
  let title = targetCard.find(".new-title").val();
  let text = targetCard.find(".new-text").val();
  if (text == "") text = "default content";
  console.log(title);
  console.log(text);
  if (title == "") {
    alert("nothing entered");
    return;
  }
  $.ajax({
    type: "POST",
    url: "/button/edit",
    data: { memoID: memoID, title: title, text: text },
    success: function (response) {
      updatePage();
    },
  });
}

function cancelEdit(targetButton, memoID) {
  $.ajax({
    type: "GET",
    url: "/cancel/edit",
    data: { memoID: memoID },
    success: function (response) {
      let targetCard = $(targetButton).closest(".card");
      targetCard.empty();
      let memo = response["memo"];
      let html = `<h3 class="card-title">${memo["title"]}</h3>
                  <p class="card-text">${memo["text"]}</p>
                  <p class="card-likes">${memo["likes"]}</p>
                  <div class="button-group" style="display: flex;">
                    <div class="edit-button button" onclick="buttonEdit(this, '${memoID}')">수정</div>
                    <div class="delete-button button" onclick="buttonDelete('${memoID}')">삭제</div>
                    <div class="link-like button" onclick="buttonLike('${memoID}')">좋아요! 👍</div>
                  </div>`;
      targetCard.append(html);
    },
  });
}

function buttonDelete(memoID) {
  $.ajax({
    type: "POST",
    url: "/button/delete",
    data: { memoID: memoID },
    success: function (response) {
      updatePage();
    },
  });
}

function buttonLike(memoID) {
  $.ajax({
    type: "POST",
    url: "/button/like",
    data: { memoID: memoID },
    success: function (response) {
      updatePage();
    },
  });
}
