// function for blinking arrows
function blink() {
   var a1 = document.getElementById('arrow1');
   var a2 = document.getElementById('arrow2');
   setInterval(function() {
      a1.style.color = (a1.style.color == 'black' ? '#00ff00': 'black')
      a2.style.color = (a2.style.color == 'black' ? '#00ff00': 'black')
   }, 1000);
}
