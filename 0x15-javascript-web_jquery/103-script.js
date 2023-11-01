$(document).ready(function () {
  function translate () {
    $('DIV#hello').empty();
    const ser = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + ser,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  }
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (i) {
    const key = i.which;
    if (key == 13) {
      translate();
    }
  });
});