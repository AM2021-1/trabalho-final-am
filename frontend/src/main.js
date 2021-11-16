var HTMLSnippets = {
	defaultModal: `
	<div class="loading-div">
		<h2>You better go grab a coffee and walk around town. This will take at least a while.</h2>
		<div class="lds-ripple" id="loading-spinner">
			<div></div>
			<div></div>
		</div>
	</div>
	`
}
var modalBody = null

function toggleCollapse(id) {
	let collapsible = $(`#${id}`)

	if(collapsible.css('display') == 'none')
		collapsible.css('display', 'block')
	else
		collapsible.css('display', 'none')
}

function showResults(results) {
	let resultHTML = `<div class="results">`

	for(let index of Object.keys(results)) {
		let pageContents = {}
		const page = `<button class="result-type" onclick="toggleCollapse(${index})">Página ${index}</button>`

		for(let value of results[index]) {
			if(!pageContents[value.label])
				pageContents[value.label] = value.text
			else
				pageContents[value.label] += `<br><br>${value.text}`
		}

		console.log(pageContents)

		resultHTML += page
		resultHTML += `<div class="result-content" id="${index}">`

		for(let type of Object.keys(pageContents)) {
			resultHTML += `
			<details>
				<summary>${type}</summary>
				<p align="justify">${pageContents[type]}</p>
			</details>
			`
		}

		resultHTML += '</div>'
	}

	resultHTML += '</div>'
	modalBody.html(resultHTML)
}

function uploadFile() {
	let file = document.getElementById('file').files[0]
	let fileName = file.name
	let formData = new FormData()

	formData.append('file', file)
	formData.append('name', fileName)

	console.log(file);
	console.log(formData);

	for (var pair of formData.entries()) {
		console.log(pair[0]+ ', ' + pair[1]); 
	}
	
	fetch('https://secure-dawn-93408.herokuapp.com/', {
		method: "POST", 
		body: formData
	  }).then(async (res) => {
		showResults(await res.json());
	  }).catch((err) => {
		console.log(err);
	}) 

	// fetch('http://localhost:5000', {
	// 	method: "POST", 
	// 	body: formData
	//   }).then(async (res) => {
	// 	showResults(await res.json());
	//   }).catch((err) => {
	// 	console.log(err);
	// }) 

	toggleModal();
}

function toggleModal() {
	toggleModal.visible = !toggleModal.visible;
	
	if(!toggleModal.modal) {
		toggleModal.modal = $(".modal");
		toggleModal.backdrop = $(".backdrop");
		modalBody = $(".modal-body")
		
		toggleModal.modal.css('transition', '0.5s');
		toggleModal.backdrop.css('transition', '0.5s');
	}
	
	if(toggleModal.visible) {
		modalBody.html(HTMLSnippets.defaultModal)
		toggleModal.modal.css({'opacity': '1', 'pointer-events': 'auto'});
		toggleModal.backdrop.css({'opacity': '0.2', 'pointer-events': 'auto'});
	}
	
	else {
		toggleModal.modal.css({'opacity': '0', 'pointer-events': 'none'});
		toggleModal.backdrop.css({'opacity': '0', 'pointer-events': 'none'});
	}
}