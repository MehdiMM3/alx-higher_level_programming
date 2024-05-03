// Add  LI element to the list when the div#add_item tag is clicked
// The new element must be <li>Item</li> and added to UL.my_list

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
