document.querySelectorAll('.action-btn').forEach(button => {
    button.addEventListener('click', function () {
        const action = this.title;
        const fileName = this.closest('.entry-item').querySelector('.text-gray-900').textContent;

        if (action === 'Delete') {
            if (confirm(`Are you sure you want to delete "${fileName}"?`)) {
                this.closest('.entry-item').style.opacity = '0.5';
                setTimeout(() => {
                    this.closest('.entry-item').remove();
                }, 300);
            }
        } else if (action === 'Disable' || action === 'Enable') {
            if (action === 'Disable') {
                this.title = 'Enable';
                this.innerHTML = '<i class="fas fa-check-circle"></i>';
                this.closest('.entry-item').style.opacity = '0.6';
            } else {
                this.title = 'Disable';
                this.innerHTML = '<i class="fas fa-ban"></i>';
                this.closest('.entry-item').style.opacity = '1';
            }
        } else if (action === 'Download') {
            alert(`Downloading "${fileName}"...`);
        }
    });
});