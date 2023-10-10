const API_URL = 'http://127.0.0.1:5000';
const vehicleDropdown = document.getElementById('vehicleDropdown');
const vehicleForm = document.getElementById('vehicleForm');

fetch(API_URL + '/get_vehicules')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data.forEach(vehicle => {
            const option = document.createElement('option');
            option.value = vehicle.id;
            option.textContent = vehicle.desc;
            vehicleDropdown.appendChild(option);
        });
    })
    .catch(error => {
        console.error("Erreur lors de la récupération des véhicules:", error);
    });

vehicleForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const selectedVehicleId = vehicleDropdown.value;
    console.log('pomme')
    fetch(`${API_URL}/get_summary/${selectedVehicleId}`, { method: 'GET' })
        .then(response => response.text())
        .then(filename => {
            console.log('Nom du fichier:', filename);

            const downloadBox = document.getElementById('downloadBox');
            const linkElement = document.getElementById('downloadLink');
            linkElement.href = `${API_URL}${filename}`;
            downloadBox.style.display = 'block';    
        })
        .catch(error => {
            console.error('Erreur lors de la soumission:', error);
        });
});
