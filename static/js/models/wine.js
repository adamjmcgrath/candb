define(['underscore',
        'backbone'], function(_, Backbone){

  var WineModel = function(data) {
    Backbone.Model.prototype.constructor.apply(this, arguments);
    this.name = data.name;
  };
  Backbone.Model.extend(WineModel.prototype);

  WineModel.prototype.defaults = null;

  return WineModel;
});
