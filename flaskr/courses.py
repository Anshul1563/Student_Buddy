def Search(link,num):
  from serpapi import GoogleSearch
  params = {
    "engine": "google",
    "q": link,
    "location": "Austin, Texas, United States",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en",
    "num": "10",
    "api_key": "4e62c2f5f0250bd7d49871a23734b04798ed23a18e2cf9b149b8aa701c66486b"
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  links = {'link':[],'title':[],'students':[],'time':[],'cost':[],'pic':[]}
  
  for x in results["organic_results"]:
        if num == 1:
            dict = Udemy(x['link'])
            try :
                print(x['link'])
                links['link'].append(x['link'])
                links['title'].append(x['title'])
                links['time'].append(dict['price'])
                links['cost'].append(dict['rating'])
                links['pic'].append('data:image/png;base64,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')
                
            except:
                None
        if num == 2:
            dict = Skillshare(x['link'])
        if num == 3:
            dict = Edx(x['link'])
            try :
                print(x['link'])
                links['link'].append(x['link'])
                links['title'].append(x['title'])
                links['time'].append(dict['students'])
                links['students'].append(dict['dur'])
                links['pic'].append('data:image/png;base64,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')
            except:
                None
        if num == 4:
            dict = Coursera(x['link'])
            try :
                print(x['link'])
                links['link'].append(x['link'])
                links['pic'].append('data:image/png;base64,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')
                links['title'].append(x['title'])
                links['time'].append(dict['students'])
                links['cost'].append(dict['rating'])
                links['students'].append(dict['dur'])
            except:
                None
        
  
  return links

def Udemy(link):
    None
def Skillshare(link):
    None
def Edx(url):
    d = {}
    try :
        response = requests.get(url)
        r=str(response.content)

        regex1 = '<div class="h4 mb-0">(\d+) weeks</div>'
        match1 = re.findall(regex1, r)

        regex2 = '<div class="d-md-none x-small heading-label text-brand-500">(((\d+)(,*))*) already enrolled!</div>'
        match2 = re.findall(regex2,r)

        d = {"dur":match1[0],"students":match2[0][0]}
    except :
        None
    return d 

    
import requests
import re


def Coursera(lnk):
    d = {}
    try :
        response = requests.get(lnk)
        c=str(response.content)
        a = 'data-test="number-star-rating"'
        r1=c.index(a)
        r2 = c[r1+len(a)+1:r1+len(a)+4]

        regex1 = '<span>(\d+)(,*)(\d+)</span></strong> already enrolled</span>'
        match1 = re.findall(regex1, c)
        aa = ''
        for i in match1[0]:
            aa = aa+i

        regex2 = '<div class="_16ni8zai m-b-0 m-t-1s">(.*) Level</div>(.*)'
        match2 = re.findall(regex2, c)

        a = ''
        for i in match2[0][0]:
            if i == ' ':
                break 
            a = a+i

        regex3 = '<span>Approx. (\d+) hours to complete</span>'
        match3 = re.findall(regex3, c)

        d = {"dur":match3[0],"students":aa,"level":a,"rating":r2}
    except :
        None
    return d

def Udemy(url):
    try :
        response = requests.get(url)
        a = str(response.content)

        rating='aggregateRating": {"@type": "AggregateRating", "ratingValue":'
        price='<meta property="udemy_com:price" content='
        aa = '\\xb9'

        r1=a.index(rating)
        p1=a.index(price)
        # print(e)
        r2 = a[r1+len(rating)+2:r1+len(rating)+5]
        p2 = a[p1+len(price):p1+len(price)+18]

        a = ''
        for i in p2[::-1]:
            if i.isnumeric():
                a = a+i
            if i!="b":
                break

        a[::-2] 


        bx = p2.index(aa)
        a = p2[bx+4:len(p2)]
        # a = re.findall(r'\d+', p2)
        d = {"rating":r2,"price":a}
        return d
    except:
        None



def Links(entry,num):
    if num == 1:
        links = Search(entry + ' site:https://www.udemy.com/course',1)
    if num == 2:
        links = Search(entry + ' site:skillshare.com/classes',2)  
    if num == 3:
        links  = Search(entry + ' site:edx.org/course',3)  
    if num == 4:
        links  = Search(entry +' site:coursera.org/learn',4)
        
    return links



