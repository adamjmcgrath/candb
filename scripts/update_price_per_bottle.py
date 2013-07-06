#!/usr/bin/env python2.7

import dev_appserver
dev_appserver.fix_sys_path()

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db
import getpass
import models

def auth_func():
  return (raw_input('Username:'), getpass.getpass('Password:'))

remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_func,
                                   'candbupdates.appspot.com')

def main():
  wines = models.Wine.all().fetch(999)

  while wines:
    to_put = []
    for wine in wines:
      price_per = wine.price_per.strip().upper()
      if wine.price_per_bottle or not price_per.startswith('CASE'):
        continue
      total_price = float(wine.price_duty_paid_inc_vat)
      wine.price_per_bottle = total_price
      try:
        wine.price_per_bottle = total_price / float(wine.unit_per_case)
        to_put.append(wine)
        print 'DONE: %s' % wine.description
      except ZeroDivisionError:
        print 'FAIL: %s' % wine.description

    db.put(to_put)
    wines = models.Wine.all().filter('__key__ >', wines[-1].key()).fetch(999)


if __name__ == '__main__':
  main()
