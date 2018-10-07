#!/usr/bin/python

import urllib2
from xml.dom import minidom

xml_data = urllib2.urlopen("https://hnrss.org/newest").read()

dom = minidom.parseString(xml_data)

items = dom.getElementsByTagName('item')

for i in iter(items[:10]):
    title = i.getElementsByTagName('title')[0].childNodes[0].data
    date = i.getElementsByTagName('pubDate')[0].childNodes[0].data
    link = i.getElementsByTagName('link')[0].childNodes[0].data

    print '%s\n\t%s\n\t%s\n' % (title, date, link) 