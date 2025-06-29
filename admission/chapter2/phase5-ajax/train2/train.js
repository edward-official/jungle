function q1() {
  $.ajax({
    type: "GET",
    url: "https://api.thecatapi.com/v1/images/search",
    data: {},
    success: function(response) {
      let appender = $("#cat-image");
      appender.empty();
      let imageLink = response[0]["url"];
      let appendee = `<img id="img-cat" src="${imageLink}">`;
      appender.append(appendee);
      //proper way to do it might be to change only the 'src' attribute than to renew the whole tag by empty and append
    }
  });
}