var map = L.map('map').setView([-22.9068, -43.1729], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


L.marker([latitude, longitude]).addTo(map)
    .bindPopup('Listing Location') 
    .openPopup();
