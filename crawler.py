## Interview Question
## Build a basic crawler that can visit a url and collect all urls, recurssively, from that site.

import urllib2
from xml.dom import minidom

start_url = ""

def get_all_urls_from_page(url):
    all_urls = set()
    xml_data = urllib2.urlopen(url).read()
    dom = minidom.parseString(xml_data)
    items = dom.getElementsByTagName('a')
    for item in items:
        link = item.getElementsByTagName('link')[0].childNodes[0].data
        all_urls.add(link)

    return all_urls

def crawler(start_url):
    visited = set()

    que = get_all_urls_from_page(start_url)

    while len(que) != 0:
        v = que[0]
        visited.add(v)
        que.remove(v)

        urls = get_all_urls_from_page(v)
        for u in urls:
            if u not in visited:
                que.add(u)


    return visited

