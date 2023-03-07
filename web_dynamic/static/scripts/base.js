window.onload = (event) => {
	console.log("page is fully loaded");
 



function newPopup(url) {
	popupWindow = window.open(
		String(url),'popUpWindow','height=400,width=600,left=100,top=100,resizable=yes,titlebar=no,scrollbars=yes,toolbar=no,menubar=no,location=no,directories=no,status=yes')
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


// let checked_box = {};
// $(document).ready(function () {

//     $('input:checkbox').change(function () {
// 	if ($(this).is(':checked_box')) {
// 	    checked_box[$(this).data('id')] = $(this).data('name');
// 	}
// 	else {
// 	    delete checked_box[$(this).data('id')];
// 	}

// 		$('div.types h4').html(function () {
// 			let job_cat = [];
// 			Object.keys(checked_box).forEach(function (key) {
// 			job_cat.push(checked_box[key]);
// 			});
// 			if (job_cat.length === 0) {
// 			return ('&nbsp');
// 			}
// 			return (job_cat.join(', '));
// 		});
// 	});




// });

const enterDiv = document.getElementById("filter");
  const hideDiv = document.getElementById("cards-container");

  // Add a "mouseenter" event listener to div1
  enterDiv.addEventListener("mouseenter", function() {
    // Set the display property of div2 to "none"
    hideDiv.style.display = "none";
  });

  





};
// ========================================================

function getValue() {
    // Get the value of the select element
    const selectValue = document.getElementById("search-service").value;
    
    // Get the value of the text input element
    const inputValue = document.getElementById("search").value;
    
    // Log the values to the console
    console.log("Selected category:", selectValue);
    console.log("Entered Town:", inputValue);

	return {
        service: selectValue,
        town: inputValue 
    };
	
  }

function getUsers(tOwn,seRvice){

	tOwn? tOwn: "None";
	seRvice?seRvice: "None";

	url = `/search?town=${tOwn}&service=${seRvice}`;

	const userData = fetch(url)
	.then((response) => { 
			return response.json().then((data) => {
				//console.log(data);
			return data;
		}).catch((err) => {
			console.log(err);
		})
	});
	// .then(response => response.json())
	// .then(data => console.log(data))
	//.catch(error => console.error(error));
	return userData;
  }

   function setUsers(){
	// const categoryValue = document.getElementById("carts").value;
    // const townValue = document.getElementById("search").value;
	const htmlVal = getValue();

	return getUsers(htmlVal.town,htmlVal.service);

  }

   async function showUsers(){

	let jsonUsers =  await setUsers();

	
	console.log(jsonUsers);//debug

	// for(val of jsonUsers){
	// 	console.log(val)
	// }
	  


	//for (let i = 0; i < jsonUsers.length; i++) {
		//const user = jsonUsers[i];
		// for(key in jsonUsers[i]) {
		// 	console.log(jsonUsers[i][key]); 
		//  }
		//console.log(jsonUsers[i][]);


		// for(const val of jsonUsers[i]){
		// 		console.log(jsonUsers[i][val]);
		// 	}
		let htmlCards = [];

		jsonUsers.forEach((user) => {
				console.log(user.full_name);
	 		
	  

		const dp = user.dp;
		const fullname = user.full_name;
		const skill = user.skill;
		const town = user.town;
		const phone = user.phone;
		const id = user.id;

		htmlCards += `<div class="card" style="width: 18rem;padding: 2%;">
					<img src="${dp}" class="card-img-top" alt="...">
					<div class="card-body">
					<h5 class="card-title">${fullname}</h5>
					<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
					</div>
					<ul class="list-group list-group-flush">
					<li class="list-group-item">${skill}</li>
					<li class="list-group-item">${town}</li>
					<li class="list-group-item">${phone}</li>
					</ul>
					<div class="card-body">
					<a href="/profile_view/${id}" class="card-link">View</a>
					<a href="JavaScript:newPopup('/request_service/${id}')" class="card-link">Request</a>
					</div>
				</div>`

		});

		//console.log(htmlCards);

		let searchResultDiv = document.getElementById('results');
		searchResultDiv.innerHTML = htmlCards
		searchResultDiv.style.display = 'flex';



		// $(document).ready(function () {	

		// 	$( "#results" ).html( htmlCards );

		// });
			  
		
  }