fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(resp => {
	resp.json().then(body => {
	    $('DIV#character').text(body.name);
	});
    })
    .catch(err => console.log(err));
