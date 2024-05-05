$(document).ready(function() {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr",
    function(data) {
      $.each(data, function(key, value) {
          $("DIV#hello").text(key)})
   })
})
