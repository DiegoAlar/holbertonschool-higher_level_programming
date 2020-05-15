$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    const titles = data.results;
    $.each(titles, function (i, title) {
      $('#list_movies').append('<li>' + title.title + '</li>');
    });
  });
});
