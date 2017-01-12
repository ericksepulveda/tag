$(document).ready( function() {

  $('.cell').mouseover(function(){
    var x = parseInt($(this).attr('id').split('_')[1]);
    if($('input#state').val() != 0){
      return;
    }
    $('#preview').show();
    var turn = $('input#turn').val();
    if(turn == 1){
      $('#preview').addClass('yellow');
    }else{
      $('#preview').addClass('red');
    }
    $('#preview').css('left', 46 * x);
  }).mouseout(function(){
    $('#preview').hide();
  });


  $('.cell').click(function(){
    var x = parseInt($(this).attr('id').split('_')[1]);
    play(x);
  });

});

function play(x){
  $('input#col').val(x);
  $('#play').submit();
}
