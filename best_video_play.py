#!/usr/bin/python3
'''
search anything and get best video of it..
'''

import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import pafy
import webbrowser
import os
srch_query = input("enter video name: ")

query = urllib.parse.quote(srch_query)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)

html = response.read()

soup = BeautifulSoup(html)
zx = 0
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    x = ('https://youtube.com/'+vid['href'])
    print (zx)

    if x !=None and zx ==1:

        recv_url = x
        break

    zx += 1
    
    


video = pafy.new(recv_url)
best = video.getbest()
playurl = best.url
webbrowser.open(playurl)
