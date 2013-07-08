#!/usr/bin/env python2.5

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import logging
import models
import os

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Development')


class Main(webapp.RequestHandler):
  def get(self):
    html = template.render(os.path.join(os.path.dirname(__file__),
                                        'templates/main.html'), {})
    self.response.out.write(html)


class SendEmail(webapp.RequestHandler):
  def get(self):
    wines = models.Wine.gql(
                'WHERE is_new = True ORDER BY date DESC, vintage').fetch(500)
    wine_arr = []
    for wine in wines:
      wine.is_new = False
      wine.put()
      wine_arr.append(wine)
    if len(wine_arr):
      template_values = {
        'wines': wine_arr,
        'is_email': True
      }
      to = 'adamjmcgrath@gmail.com'
      if not DEBUG:
        to += ', Thomas.Holmes@miller-insurance.com, SHolmes@imgworld.com'
      path = os.path.join(os.path.dirname(__file__), 'templates/email.html')
      mail.send_mail(sender='adamjmcgrath@gmail.com',
                     to=to,
                     subject='New wines on Corney & Barrow',
                     body='View in HTML',
                     html=template.render(path, template_values))
      logging.info('email sent')
