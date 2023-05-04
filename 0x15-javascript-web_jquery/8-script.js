fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(resp => resp.json())
    .then(body => {
	body.results.map(value => {
	    $('UL#list_movies').append(`<li>${value.title}</li>`);
	});
    })
    .catch(err => console.log(err));
