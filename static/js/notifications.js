// Toast notifications functionality
document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss toast notifications after 5 seconds
    const toasts = document.querySelectorAll('.toast');
    
    toasts.forEach(toast => {
        setTimeout(() => {
            const bsToast = new bootstrap.Toast(toast);
            bsToast.hide();
        }, 5000);
        
        // Add ability to dismiss toast by clicking anywhere on it
        toast.addEventListener('click', function(e) {
            if (!e.target.classList.contains('btn-close')) {
                const bsToast = new bootstrap.Toast(this);
                bsToast.hide();
            }
        });
    });
});
