const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);
const endpoint = '/api/v1/';

let DOMTemperatuur;

const showTemperatuur = function(jsonObject){
  DOMTemperatuur.innerHTML = jsonObject[jsonObject.length - 1].Waarde+ ' °C';
}

const getTemperatuur = function(){
  console.log(`http://${lanIP}${endpoint}sensoren/1/historiek/`);
  handleData(`http://${lanIP}${endpoint}sensoren/1/historiek/`, showTemperatuur);
}

const init = function () {
  DOMTemperatuur = document.querySelector('.js-temperatuur');
  getTemperatuur();
 }


document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  init();
});
