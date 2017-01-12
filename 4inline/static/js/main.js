$(document).ready( function() {

  var turn = $('input#turn').val();
  var state = $('input#state').val();
  var color1, color2;

  if(state == 1){
    confetti('#fce50f', '#b4a30c');
  }else if(state == 2){
    confetti('#d91408', '#a10f06');
  }

  $('.cell').mouseover(function(){
    var x = parseInt($(this).attr('id').split('_')[1]);
    if(state != 0){
      return;
    }
    $('#preview').show();
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
