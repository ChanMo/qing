$(document).foundation();


function send(e){
  var url = $(e).data('href');
  var data = $(e).serialize();
  $.post(url, data, function(data){
    alert('Success!');
  });
  return false;
}
