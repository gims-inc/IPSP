function newPopup(url) {
	popupWindow = window.open(
		url,'popUpWindow','height=300,width=600,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
}


const input = document.getElementById('country');
//const divs = document.querySelectorAll('.p-country');
const out = document.getElementsByClassName('.p-class');


// input.onkeyup = function() {
//   divs.forEach(function(div) {
//     div.innerHTML = input.value;
//   });
// }

document.getElementById('edit-profile').addEventListener('load', 
  

input.onkeyup = function() {
	out.innerHTML = input.value;
  }
    
, false);