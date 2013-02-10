#!/usr/bin/env python2.5

from google.appengine.ext import db

class Wine(db.Model):
  date = db.DateProperty(auto_now=True)
  country_region = db.StringProperty()
  vintage = db.StringProperty()
  description = db.StringProperty()
  unit_size = db.StringProperty()
  unit_per_case = db.StringProperty()
  bottles = db.StringProperty()
  cases = db.StringProperty()
  price_in_bond = db.StringProperty()
  price_duty_paid_ex_vat = db.StringProperty()
  price_duty_paid_inc_vat = db.StringProperty()
  price_per = db.StringProperty()
  status = db.StringProperty()
  ullage = db.StringProperty()
  packaging = db.StringProperty()
  label_condition = db.StringProperty()
  link = db.StringProperty()
  is_new = db.BooleanProperty()
  price_per_bottle = db.FloatProperty()

#for row in models.Wine.all().filter('price_per_bottle !=', None):
#  price_per = row.price_per.strip().upper()
#  total_price = float(row.price_duty_paid_inc_vat)
#  row.price_per_bottle = total_price
#  if price_per.startswith('CASE'):
#    row.price_per_bottle = total_price / float(row.unit_per_case)
#  row.put()