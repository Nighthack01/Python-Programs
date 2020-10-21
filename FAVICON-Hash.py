 # Check /favicon.ico

import mmh3
import requests
import codecs
 
 
response = requests.get('#target-website-libnk') #https://www.evil.com.favicon.in
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)
