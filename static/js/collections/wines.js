define(['underscore',
        'backbone',
        'models/wine'], function(_, Backbone, WineModel){

  var WineCollection = function() {
    Backbone.Collection.prototype.constructor.apply(this, arguments);
    this.model = WineModel;
  };
  Backbone.Collection.extend(WineCollection.prototype);

  return WineCollection;
});
