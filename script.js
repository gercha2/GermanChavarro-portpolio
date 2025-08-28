const API_BASE_URL = 'http://localhost:8000/api';

// Load recommendations from API on page load
document.addEventListener('DOMContentLoaded', async function() {
    await loadRecommendations();
});

async function loadRecommendations() {
    try {
        const response = await fetch(`${API_BASE_URL}/recommendations`);
        if (response.ok) {
            const recommendations = await response.json();
            const container = document.getElementById("all_recommendations");
            
            // Clear existing recommendations except the static ones
            // We'll keep the static ones for now to avoid breaking the layout
            
            // Add loaded recommendations
            recommendations.forEach(rec => {
                const element = document.createElement("div");
                element.setAttribute("class", "recommendation");
                element.innerHTML = `<span class="quotes">&#8220;</span>${rec.message}<span class="quotes">&#8221;</span> - ${rec.name}`;
                container.appendChild(element);
            });
        }
    } catch (error) {
        console.log('Could not load recommendations from API:', error);
        // Fall back to static recommendations (already in HTML)
    }
}

async function submitRecommendation() {
    const name = document.getElementById("name");
    const recommendation = document.getElementById("comment");

    if (recommendation.value != null && recommendation.value.trim() != "") {
        console.log("New recommendation added");

        try {
            // Try to submit to API
            const response = await fetch(`${API_BASE_URL}/recommendations`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name: name.value || 'Anonymous',
                    message: recommendation.value
                })
            });

            if (response.ok) {
                const newRec = await response.json();
                console.log('Recommendation saved to API:', newRec);
                showPopup(true);

                // Add to display
                const element = document.createElement("div");
                element.setAttribute("class", "recommendation");
                element.innerHTML = `<span class="quotes">&#8220;</span>${newRec.message}<span class="quotes">&#8221;</span> - ${newRec.name}`;
                document.getElementById("all_recommendations").appendChild(element);

                name.value = "";
                recommendation.value = "";
            } else {
                throw new Error('API request failed');
            }
        } catch (error) {
            console.log('Could not save to API, using local storage:', error);
            // Fallback to original behavior
            showPopup(true);

            // Create div element locally
            const element = document.createElement("div");
            element.setAttribute("class", "recommendation");
            element.innerHTML = `<span class="quotes">&#8220;</span>${recommendation.value}<span class="quotes">&#8221;</span> ${name.value ? '- ' + name.value : ''}`;
            document.getElementById("all_recommendations").appendChild(element);

            name.value = "";
            recommendation.value = "";
        }
    }
}

function showPopup(bool) {
    if (bool) {
        document.getElementById("showPopup").style.visibility = 'visible';
    } else {
        document.getElementById("showPopup").style.visibility = 'hidden';
    }
}

// Add smooth scrolling behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const nameInput = document.getElementById('name');
    const commentInput = document.getElementById('comment');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic validation
            if (!commentInput.value.trim()) {
                commentInput.style.borderColor = '#ff4444';
                commentInput.focus();
                return false;
            } else {
                commentInput.style.borderColor = '#e0e0e0';
            }

            submitRecommendation();
        });
    }

    // Reset border color on input
    if (commentInput) {
        commentInput.addEventListener('input', function() {
            if (this.value.trim()) {
                this.style.borderColor = '#e0e0e0';
            }
        });
    }
});

