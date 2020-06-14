const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);
const endpoint = '/api/v1/';

let DOMTemperatuur; let DOMLicht;

const getHistoryLicht = function () {
    handleData(`http://${lanIP}${endpoint}componenten/2/historiek/`, showGraphLicht);
  };
  
  const showLicht = function (jsonObject) {
      console.log(jsonObject);
      DOMLicht.innerHTML = jsonObject.Waarde;
  };
  
  const getHistoryTemperatuur = function () {
    handleData(`http://${lanIP}${endpoint}componenten/1/historiek/`, showGraphTemperatuur);
  };
  
  const showTemperatuur = function (jsonObject) {
      console.log(jsonObject);
      DOMTemperatuur.innerHTML = jsonObject.Waarde;
  };

const showGraphLicht = function (jsonObject) {
  labels = [];
  data = [];
  for (const measurement of jsonObject) {
    labels.push(measurement.DateTime);
    data.push(measurement.Waarde);
  }
  var chart = new Chartist.Line(
    '.ct-licht',
    {
      labels: labels,
      series: [data],
    },
    {
      low: 0,
      high: 100,
      showArea: true,
      showPoint: false,
    }
  );

  chart.on('draw', function (data) {
    if (data.type === 'line' || data.type === 'area') {
      data.element.animate({
        d: {
          begin: 2000 * data.index,
          dur: 2000,
          from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
          to: data.path.clone().stringify(),
          easing: Chartist.Svg.Easing.easeOutQuint,
        },
      });
    }
  });
};

const showGraphTemperatuur = function (jsonObject) {
  labels = [];
  data = [];
  for (const measurement of jsonObject) {
    labels.push(measurement.DateTime);
    data.push(measurement.Waarde);
  }
  var chart = new Chartist.Line(
    '.ct-temperatuur',
    {
      labels: labels,
      series: [data],
    },
    {
      low: 0,
      high: 30,
      showArea: true,
      showPoint: false,
      fullWidth: true,
      height: '228px',
    }
  );

  chart.on('draw', function (data) {
    if (data.type === 'line' || data.type === 'area') {
      data.element.animate({
        d: {
          begin: 2000 * data.index,
          dur: 2000,
          from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
          to: data.path.clone().stringify(),
          easing: Chartist.Svg.Easing.easeOutQuint,
        },
      });
    }
  });
};


const init = function () {
  DOMTemperatuur = document.querySelector('.js-temperatuur');
  DOMLicht = document.querySelector('.js-licht');
  getHistoryTemperatuur();
  getHistoryLicht();
  socket.emit('connect');
  socket.on('temperatuur', function (data) {
    showTemperatuur(data);
  });
  socket.on('Licht', function (data) {
    showLicht(data);
  });
};

document.addEventListener('DOMContentLoaded', function () {
  console.info('DOM geladen');
  init();
});