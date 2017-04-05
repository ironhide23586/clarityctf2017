import numpy as np
import sys, os
import json

if __name__ == '__main__':
  f = open('dump.html', 'rb')
  html_txt = f.readlines()
  f.close()
  l = html_txt[2910].strip()[1:-1]
  raw = l.split('startDate')
  m = ['{startDate:'+r[:-3] for r in raw if r[1] == ':']
  date = None
  name = None
  loc = None
  for me in m:
    k = 0
    fields = me.split(',')
    for field in fields:
      if 'startDate' in field:
        print field.split(':')[-1]
      if 'name' in field:
        print field.split(':')[-1]
      if 'streetAddress' in field:
        print field.split(':')[-1]
        print '--------------'
      
  k = 0