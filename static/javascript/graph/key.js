document.addEventListener('DOMContentLoaded', function () {
    var canvas = document.getElementById('keyCanvas').getContext('2d');
    

    const graph = fetch('/get-data-graph-key')
        .then(response => response.json())
        .then(data => {
            const labels = Object.keys(data);
            const values = Object.values(data);

            
            var myChart = new Chart(canvas, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '# of songs',
                        data: values,
                        borderWidth: 1
                    }]
                },
                options: {
                }
            });
        }
        );
    
    
});