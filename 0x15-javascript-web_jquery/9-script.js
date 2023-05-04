$(document).ready(() => {
    fetch('https://fourtonfish.com/hellosalut/?lang=fr')
	.then(resp => resp.json()).then(resp => {
	    $('DIV#hello').text(resp.hello);
	})
	.catch(err => {
	    console.log(err);
	});
});
