button = $("DIV#character")
$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json",
  function(server_data){
    button.text(server_data.name)})
