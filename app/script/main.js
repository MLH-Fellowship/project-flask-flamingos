function initialize() {
  var mapOptions = {
    center: new google.maps.LatLng(0, 0),
    zoom: 1,
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}
window.addEventListener("DOMContentLoaded", initialize);
