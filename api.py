#!/usr/bin/env python2.5

import json

from google.appengine.ext import webapp

import models


class WineListHandler(webapp.RequestHandler):
  def get(self):
    wines = [w.to_dict() for w in models.Wine.all().run(limit=10)]
    self.response.out.write(json.dumps(wines))