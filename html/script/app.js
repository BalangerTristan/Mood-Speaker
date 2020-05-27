const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);
const endpoint = '/api/v1/';

let DOMTemperatuur;

const showTemperatuur = function(jsonObject){
  // DOMTemperatuur.innerHTML = jsonObject[jsonObject.length - 1].Waarde+ ' °C';
  DOMTemperatuur.innerHTML = jsonObject.Waarde+ ' °C';
}

const getTemperatuur = function(){
  handleData(`http://${lanIP}${endpoint}componenten/1/historiek/`, showTemperatuur);
}

const init = function () {
  DOMTemperatuur = document.querySelector('.js-temperatuur');
  socket.emit('connect');
  socket.on('temperatuur', function(data){
    showTemperatuur(data);
  });
  // getTemperatuur();
};


document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  init();
});
