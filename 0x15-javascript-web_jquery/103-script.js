$(document).ready(() => {
    $('INPUT#btn_translate').on('click', sayHello);
    $('INPUT#language_code').focus(function () {
	$(this).keydown(function (e) {
	    if (e.keyCode === 13) {
		sayHello();
	    }
	});
    });
});

const sayHello = () => {
    let lang = $('INPUT#language_code').val();
    fetch(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`)
	.then(resp => resp.json())
	.then(resp => {
	    $('DIV#hello').text(resp.hello);
	})
	.catch(err => console.log(err));
}
