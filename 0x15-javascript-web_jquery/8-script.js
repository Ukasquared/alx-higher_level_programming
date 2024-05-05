button = $("UL#list_movies")
$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
  function(data){
    $.each(data.results, function(index, value) {
        button.append("<li>"+value.title+"</li>")
        })
  })
