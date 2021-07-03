# -*- coding: utf-8 -*-

import requests


class save:
     def toFile(text):
          file = open("pubkey_all.txt", "a+")
          file.write(text)
          file.close()

file = open('address_all.txt', 'r+')

for address in file.readlines():
     request = ('https://blockchain.info/q/pubkeyaddr/' + address)
     response = requests.get(request)
     
     if response.status_code == 404:
          print(address + "No Transaction")
          
     if response.status_code == 200:
          public_key = (response.text)
          print (address + " " + public_key)
          save.toFile(public_key + '\n')
