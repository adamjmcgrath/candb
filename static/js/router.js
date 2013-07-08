define(['jquery',
        'underscore',
        'backbone',
        'views/list'], function($, _, Backbone, WineList){

  var Router = Backbone.Router.extend({
    routes: {
      // Define some URL routes
      '/wine': 'showWines',

      // Default
      '*actions': 'defaultAction'
    }
  });

  Router.prototype.init = function() {
    this.on('showWines', function(){
      var wineListView = new WineList();
      wineListView.render();
    });

    this.on('defaultAction', function(actions){
      console.log('No route:', actions);
    });

    Backbone.history.start();
  };

  return new Router();
});