function uploadFile() {
	let file = document.getElementById('file').files[0]
	let formData = new FormData()

	formData.append('file', file)
	console.log(file)
	console.log(formData)
	fetch('http://localhost:8000/testShitUploadFromSomethingCompletelyUnrelatedToThisApplication', {
		method: 'POST',
		body: formData
	})
}