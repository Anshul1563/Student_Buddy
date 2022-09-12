from serpapi import GoogleSearch
import requests
import pandas as pd
from bs4 import BeautifulSoup

def getdata(url):
	r = requests.get(url)
	return r.text

def sorting(lst):
    lst.sort(key=len)
    return lst

def project_txt(query):
    params = {
    "engine": "google",
    "num": "10",
    "q": query,
    "google_domain": "google.com",
    "gl": "in",
    "hl": "en",
    "api_key": "4e62c2f5f0250bd7d49871a23734b04798ed23a18e2cf9b149b8aa701c66486b"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    ne=[]
    for i in results["organic_results"]:
        ne.append(i['link'])

    # print(ne)

    para=[]
    r = requests.get(ne[0])
    htmldata = r.text
    # htmldata = getdata(ne[0])
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data in soup.find_all("p"):
        para.append(data.get_text())


    # print(para)
    para.sort(key=len)
    # para=sorting(para)
    para=para[::-1]
    # para = soup.find_all("p")
    # para = [str(i) for i in para]

    # print(para[2])

    return para

