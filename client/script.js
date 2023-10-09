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

vehicleForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const selectedVehicleId = vehicleDropdown.value;

    fetch(`${API_URL}/get_summary/${selectedVehicleId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Réponse du serveur:', data);
        // Traitez la réponse ici, par exemple en affichant un message à l'utilisateur
    })
    .catch(error => {
        console.error('Erreur lors de la soumission:', error);
    });
});
