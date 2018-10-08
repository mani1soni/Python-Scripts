#   $ python weather.py 'your_zipcode'
import urllib
import json
import sys

if len(sys.argv)<2:
    print 'Please provide a US zipcode'
    exit(1)

zipcode=sys.argv[1]
url='http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+'&units=imperial&APPID=81bf6ab8b40197439ba85fbc537fbaac'
res=urllib.urlopen(url)
data=json.loads(res.read())
print("\nIt's now %sF with %s in %s" % (data['main']['temp'],data['weather'][0]['description'],data['name']))