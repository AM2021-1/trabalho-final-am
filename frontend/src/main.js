function uploadFile() {
	let file = document.getElementById('file').files[0]
	let fileName = file.name
	let formData = new FormData()

	formData.append('file', file)
	formData.append('name', fileName)

	fetch('http://localhost:5000', {
		method: 'POST',
		body: formData
	}).then((res) => {
		console.log(res);
	}).catch((err) => {
		console.log(err)
	})
}
