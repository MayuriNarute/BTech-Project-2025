let chart;

function uploadImage() {
    const input = document.getElementById('imageUpload');
    if (!input.files.length) {
        alert('Please select an image.');
        return;
    }

    const file = input.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Show original image
    const originalImageUrl = URL.createObjectURL(file);
    document.getElementById('originalImage').src = originalImageUrl;

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        // Show enhanced image (served from /static/ folder)
        document.getElementById('enhancedImage').src = `/static/enhanced/enhanced_image.jpg?${Date.now()}`;

        // Show predicted class
        document.getElementById('predictedClass').innerText = `Prediction: ${data.predicted_class}`;

        // Plot chart
        const ctx = document.getElementById('probabilityChart').getContext('2d');
        const labels = Object.keys(data.probability_scores);
        const scores = Object.values(data.probability_scores);

        if (chart) {
            chart.destroy();
        }

        chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Probability (%)',
                    data: scores,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    })
    .catch(err => {
        console.error('Prediction failed:', err);
        alert('Prediction failed. See console for details.');
    });
}
