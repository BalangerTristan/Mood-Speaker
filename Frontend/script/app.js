const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);
const endpoint = '/api/v1/';

let DOMTemperatuur; let DOMLicht; 


const showLicht = function(jsonObject){
  // DOMTemperatuur.innerHTML = jsonObject[jsonObject.length - 1].Waarde+ ' °C';
  DOMLicht.innerHTML = jsonObject.Waarde;
}

const getLicht = function(){
  handleData(`http://${lanIP}${endpoint}componenten/2/historiek/`, showLicht);
}

const showTemperatuur = function(jsonObject){
  // DOMTemperatuur.innerHTML = jsonObject[jsonObject.length - 1].Waarde+ ' °C';
  DOMTemperatuur.innerHTML = Math.round(jsonObject.Waarde * 100) / 100;
}

const getTemperatuur = function(){
  handleData(`http://${lanIP}${endpoint}componenten/1/historiek/`, showTemperatuur);
}

const init = function () {
  DOMTemperatuur = document.querySelector('.js-temperatuur');
  DOMLicht = document.querySelector('.js-licht');
  socket.emit('connect');
  socket.on('temperatuur', function(data){
    showTemperatuur(data);
  });
  socket.on('Licht', function(data){
    showLicht(data);
  });
  // getTemperatuur();
};


document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  init();
});
