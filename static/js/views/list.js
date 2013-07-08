define(['jquery',
        'underscore',
        'backbone',
        'collections/wines',
        'text!templates/list.html'],
    function($, _, Backbone, WineCollection, wineListTemplate){

  var WineListView = function() {
    this.el = $('#container');
  };
  Backbone.View.extend(WineListView);

  WineListView.prototype.render = function() {
    this.collection = new WineCollection();
    this.collection.add({name: 'Merlot'});
    var compiledTemplate = _.template(wineListTemplate,
        {wines: this.collection.models});
    this.el.html(compiledTemplate);
  };

  return WineListView;
});