// Cart functionality
document.addEventListener('DOMContentLoaded', function() {
    // Quantity selector buttons
    const quantityBtns = document.querySelectorAll('.quantity-btn');
    
    if (quantityBtns) {
        quantityBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const action = this.dataset.action;
                const input = this.closest('.quantity-selector').querySelector('input[type="number"]');
                
                let currentValue = parseInt(input.value);
                
                if (action === 'increase' && currentValue < parseInt(input.max)) {
                    input.value = currentValue + 1;
                } else if (action === 'decrease' && currentValue > parseInt(input.min)) {
                    input.value = currentValue - 1;
                }
            });
        });
    }
    
    // Clear cart functionality
    const clearCartBtn = document.getElementById('clear-cart');
    
    if (clearCartBtn) {
        clearCartBtn.addEventListener('click', function() {
            if (confirm('Êtes-vous sûr de vouloir vider votre panier ?')) {
                fetch('/cart/clear/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.ok) {
                        window.location.reload();
                    }
                });
            }
        });
    }

    // Add to cart animation
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
    
    if (addToCartBtns) {
        addToCartBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check me-1"></i> Ajouté!';
                this.classList.remove('btn-success');
                this.classList.add('btn-secondary');
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('btn-secondary');
                    this.classList.add('btn-success');
                }, 1500);
            });
        });
    }
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
