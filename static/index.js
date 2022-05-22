function updateTextArea() {
    let textArea = document.querySelector('textarea[class="form-control"]')
    let iframeBody = document.querySelector('iframe[class="form-control"]').contentDocument.body

    iframeBody.innerHTML = textArea.value
}