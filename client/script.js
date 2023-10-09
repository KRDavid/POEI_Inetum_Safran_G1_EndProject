const API_URL = 'https://your-api-endpoint.com/vehicles';
const vehicleDropdown = document.getElementById('vehicleDropdown');

fetch(API_URL)
    .then(response => response.json())
    .then(data => {
        data.forEach(vehicle => {
            const option = document.createElement('option');
            option.value = vehicle.id;
            option.textContent = vehicle.name;
            vehicleDropdown.appendChild
        });
    })
    .catch(error => {
        console.error("Erreur lors de la récupération des véhicules:", error);
    });