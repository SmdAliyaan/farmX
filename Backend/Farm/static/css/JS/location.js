function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(setPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function setPosition(position) {
    var userLat = position.coords.latitude;
    var userLon = position.coords.longitude;
    document.getElementById("lat").value = userLat;
    document.getElementById("lon").value = userLon;
    alert("Location set! You can now click 'Get Forecast'.");
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}