function newPopup(url) {
	popupWindow = window.open(
		String(url),'popUpWindow','height=400,width=600,left=100,top=100,resizable=yes,scrollbars=yes,toolbar=no,menubar=no,location=no,directories=no,status=yes')
}


// const input = document.getElementById('country');
// //const divs = document.querySelectorAll('.p-country');
// const out = document.getElementsByClassName('.p-class');


// // input.onkeyup = function() {
// //   divs.forEach(function(div) {
// //     div.innerHTML = input.value;
// //   });
// // }

// document.getElementById('edit-profile').addEventListener('load', 
  

// input.onkeyup = function() {
// 	out.innerHTML = input.value;
//   }
    
// , false);

function updateUser(jsonobj){
	fetch("/update_user", {
		method: "POST",
		body: JSON.stringify({}),
	}).then((_res) => {
	window.location.href = "/user_profile/"+{userId} ;
	});
}

function notImplementedYet(){
	alert("This feature is currently being implemented!")
}


function exitPopup(){
	window.open('','_self').close();
}

function confirmRequest(jsonObj){

}