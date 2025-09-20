// Mobile menu toggle
document.getElementById('menu-toggle').addEventListener('click', function() {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
})
// Form submission handling
document.getElementById('data-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const category = document.getElementById('category').value;
    const number = document.getElementById('number').value;
    const description = document.getElementById('description').value;
    
    // Validate form
    if (!category || !number || !description) {
        alert('Please fill in all fields');
        return;
    }
    
    // Create result HTML
    const resultHTML = `
        <div class="space-y-3">
            <p><strong>Category:</strong> ${category}</p>
            <p><strong>Number:</strong> ${number}</p>
            <p><strong>Description:</strong></p>
            <p class="bg-gray-50 p-3 rounded-lg">${description.replace(/\n/g, '<br>')}</p>
            <p class="text-sm text-gray-500 mt-4">Submitted on: ${new Date().toLocaleString()}</p>
        </div>
    `;
    
    // Display results
    document.getElementById('results').innerHTML = resultHTML;
    
    // Reset form
    this.reset();
});