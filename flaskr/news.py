from serpapi import GoogleSearch


def news_buddy(query):
    params = {
    "engine": "google",
    "q": query,
    "location": "Delhi, India",
    "google_domain": "google.co.in",
    "gl": "in",
    "hl": "en",
    "tbm": "nws",
    "num": "10",
    "api_key": "4e62c2f5f0250bd7d49871a23734b04798ed23a18e2cf9b149b8aa701c66486b"
    }

    search = GoogleSearch(params)
    results = search.get_dict()


    news=[]
    for i in results["news_results"]:
        news.append({"title":i['title'],"link":i['link'],"source":i['source'],"date":i['date'],"snippet":i['snippet'],"title":i['title'],"pic":i['thumbnail']})

    return news


