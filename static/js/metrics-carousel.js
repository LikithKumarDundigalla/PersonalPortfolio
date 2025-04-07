// GitHub Metrics Carousel
document.addEventListener('DOMContentLoaded', function() {
    const metricsContainer = document.getElementById('github-metrics');
    const prevButton = document.getElementById('prev-metric');
    const nextButton = document.getElementById('next-metric');
    const dots = document.querySelectorAll('.metrics-dot');
    
    let currentIndex = 0;
    const totalItems = 5; // Total number of metrics
    
    // Function to update the carousel position
    function updateCarousel() {
        if (metricsContainer) {
            metricsContainer.style.transform = `translateX(-${currentIndex * 20}%)`;
            
            // Update active dot
            dots.forEach((dot, index) => {
                if (index === currentIndex) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }
    }
    
    // Event listeners for navigation buttons
    if (prevButton) {
        prevButton.addEventListener('click', function() {
            currentIndex = (currentIndex - 1 + totalItems) % totalItems;
            updateCarousel();
        });
    }
    
    if (nextButton) {
        nextButton.addEventListener('click', function() {
            currentIndex = (currentIndex + 1) % totalItems;
            updateCarousel();
        });
    }
    
    // Event listeners for dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', function() {
            currentIndex = index;
            updateCarousel();
        });
    });
    
    // Add touch swipe functionality
    let touchStartX = 0;
    let touchEndX = 0;
    
    if (metricsContainer) {
        metricsContainer.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        }, false);
        
        metricsContainer.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, false);
    }
    
    function handleSwipe() {
        if (touchEndX < touchStartX) {
            // Swipe left
            currentIndex = (currentIndex + 1) % totalItems;
        } else if (touchEndX > touchStartX) {
            // Swipe right
            currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        }
        updateCarousel();
    }
    
    // Auto-advance the carousel every 5 seconds
    setInterval(function() {
        currentIndex = (currentIndex + 1) % totalItems;
        updateCarousel();
    }, 5000);
    
    // Initialize the carousel
    updateCarousel();
});
