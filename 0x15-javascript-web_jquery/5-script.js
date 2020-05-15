$('#add_item').click(function () {
  var item = $('<li></li>').text('Item');
  $('UL.my_list').append(item);
});
