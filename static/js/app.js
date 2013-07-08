define(['jquery',
        'underscore',
        'backbone',
        'router'], function($, _, Backbone, Router){

  var App = function() {
    Router.init();
  };

  App.prototype.init = function() {
    Router._events.showWines[0].callback();
  };

  return new App();

});
