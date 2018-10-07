import sys
import re
import random
import datetime
from pymongo import *
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#================================================(def)


def HTTP_lift(url):
    try:
        html = urlopen(url)
    except:
        print("is ERROR")
        follow_External_Only("http://syosetu.com/")
        k = 0
        return None
    return "OK"
#------------------------------------------------


def get_Internal_Link(bs4, includeUrl):
    internal_Link = []
    for link in bs4.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] not in internal_Link:
            internal_Link.append(link.attrs['href'])
    return internal_Link

#--------------------------------------------------


def get_External_Link(bs4, excludeUrl):
    external_Link = []
    for link in bs4.findAll("a", href=re.compile("^(http://.*" + excludeUrl + ").*")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_Link:
                external_Link.append(link.attrs['href'])
    return external_Link

#--------------------------------------------------


def split_Address(address):
    address_part = address.replace("http://", "").split("/")
    return address_part

#--------------------------------------------------


def get_Random_External_Link(startingPage):
    global k
    if HTTP_lift(startingPage) == None:
        return None
    else:
        html = urlopen(startingPage)
        bs4 = BeautifulSoup(html, "lxml")
        external_Link = get_External_Link(bs4, urlparse(startingPage).netloc)
        if len(external_Link) == 0:
            # print("\t\t\t\t\t\t\t---------error number is : " +
            #       str(k) + "---------------------")
            # k += 1
            # print("\t\t\t\t\t\t\tNo external link")
            domain = urlparse(startingPage).scheme + "://" + \
                urlparse(startingPage).netloc
            internal_Link = get_Internal_Link(bs4, domain)
            try:
                return get_Random_External_Link(internal_Link[random.randint(0, len(internal_Link) - 1)])
            except ValueError:
                return "http://syosetu.com/"
        else:
            return external_Link[random.randint(0, len(external_Link) - 1)]

#---------------------------------------------------


def follow_External_Only(startingSite):
    external_Link = get_Random_External_Link(startingSite)
    if HTTP_lift(external_Link) != None:
        display(external_Link)
    follow_External_Only(external_Link)

#--------------------------------------------------


def display(external_Link):
    global i
    global k
    if external_Link != "http://syosetu.com/":
        html = urlopen(external_Link)
        bs4 = BeautifulSoup(html, "lxml")
        if len(bs4.findAll("div", {"id": "novel_ex"})) != 0:
            print('===============find number is :  ' +
                  str(i) + '====================')
            try:
                print("Random external Link is :" + external_Link)
            except TypeError:
                print("THE LINK TYPE ERROR")
            try:
                if HTTP_lift("http://ncode.syosetu.com/novelview/infotop/ncode" + urlparse(external_Link).path) != None:
                    html = urlopen(
                        "http://ncode.syosetu.com/novelview/infotop/ncode" + urlparse(external_Link).path)
                    bs4 = BeautifulSoup(html, "lxml")
                    liste = []

                    if bs4.find("p", {"id": "ncode"}).get_text() not in nolist:

                        nolist.add(bs4.find("p", {"id": "ncode"}).get_text())

                        liste.append(bs4.h1.get_text())  # 標題

                        for temp in bs4.findAll("p", {"id": "ncode"}):
                            liste.append(temp.get_text(":", strip=True))

                        if len(bs4.findAll("span", {"id": "noveltype_notend"})) == 0:
                            for temp in bs4.findAll("span", {"id": "noveltype"}):
                                liste.append(temp.get_text(":", strip=True))
                        else:
                            for temp in bs4.findAll("span", {"id": "noveltype_notend"}):
                                liste.append(temp.get_text(":", strip=True))

                        for temp in bs4.find("table", {"id": "noveltable1"}).findAll("tr", limit=3):
                            liste.append(temp.get_text("\n", strip=True))

                        for temp in bs4.find("table", {"id": "noveltable2"}).findAll("tr", limit=2):
                            liste.append(temp.get_text(":", strip=True))

                        liste.append(bs4.find("table", {"id": "noveltable2"}).find(
                            text="文字数").parent.parent.get_text(":", strip=True))

                        importdata = {
                            "link": external_Link,
                            "title": liste[0],
                            "NO_ID": liste[1],
                            "id_end": liste[2],
                            "Introduction": liste[3],
                            "author": liste[4],
                            "Keywords": liste[5],
                            "start_date": liste[6],
                            "end_date": liste[7],
                            "Word_Count": liste[8]
                        }

                        collection.insert(importdata)
                        k = 0
                        print(importdata)
                        print("\n\n\n\n\n\n")
                        print(nolist)
                    liste = []
                    k += 1
                else:
                    k += 1
            except AttributeError:
                print("NOT TITLE OR novel")
                for temp in liste:
                    print(temp)
                    print("\n\n")
            i += 1
        elif k > 20:
            follow_External_Only("http://syosetu.com/")
            random.seed(datetime.datetime.now())
            print("!!!!!!!!!!!!!!!!!!找不到!!!!!!!!!!!!!")
            k = 0
        else:
            k += 1
            print("目前 未找到數為:" + str(k))


#================================================(dim)
i = 1
k = 1
nolist = set()
random.seed(datetime.datetime.now())
sys.setrecursionlimit(1000000)
#================================================(main)

client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.novel
collection = db.novel

for temp in collection.find({}, {"NO_ID": 1, "_id": 0}):
    for Key, value in temp.items():
        nolist.add(value)
print(nolist)
follow_External_Only("http://syosetu.com/")
