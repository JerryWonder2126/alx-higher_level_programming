$(document).ready(() => {
    let list = $('UL.my_list');

    $('DIV#add_item').on('click', () => {
	list.append('<li>Item</li>');
    });

    $('DIV#remove_item').on('click', () => {
	list.find('li:last').remove();
    });

    $('DIV#clear_list').on('click', () => {
	list.text('');
    });
});
