require.config({
  paths: {
    jquery: '/static/libs/jquery/jquery',
    underscore: '/static/libs/underscore-amd/underscore',
    backbone: '/static/libs/backbone-amd/backbone',
    text: '/static/libs/requirejs-text/text'
  }
});

require(['app'], function(App){
  App.init();
});
