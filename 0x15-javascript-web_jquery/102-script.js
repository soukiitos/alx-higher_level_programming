$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
    });
  });
});