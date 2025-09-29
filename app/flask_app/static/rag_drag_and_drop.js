const fileInput = document.getElementById('file-upload');
const fileNameDisplay = document.getElementById('file-name');
const selectedFileName = document.getElementById('selected-file-name');

fileInput.addEventListener('change', function (e) {
    if (this.files && this.files[0]) {
        selectedFileName.textContent = this.files[0].name;
        fileNameDisplay.classList.remove('hidden');
    } else {
        fileNameDisplay.classList.add('hidden');
    }
});

// Drag and drop functionality
const dropArea = document.querySelector('.border-dashed');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight() {
    dropArea.classList.add('border-blue-400', 'bg-blue-50');
}

function unhighlight() {
    dropArea.classList.remove('border-blue-400', 'bg-blue-50');
}

dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    fileInput.files = files;

    if (files && files[0]) {
        selectedFileName.textContent = files[0].name;
        fileNameDisplay.classList.remove('hidden');
    }
}