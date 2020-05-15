document.addEventListener('DOMContentLoaded', function () {
  // this function runs when the DOM is ready, i.e. when the document has been parsed
  exec();
});

const exec = function () {
  $(document).ready(function () {
    $('#btn_translate').click(function () {
      const lang = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(url, function (data) {
        $('#hello').text(data.hello);
      });
    });
  });
};
