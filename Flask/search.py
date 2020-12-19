#pip install wikipedia -api
import wikipediaapi

#pip install git+https://github.com/alainrouillon/py-googletrans@feature/enhance-use-of-direct-api
from googletrans import Translator

#pip install requests beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup

#english word -> translate korean -> search wiki
def wiki(class_name):
    wiki = wikipediaapi.Wikipedia( 
        language='ko', 
        extract_format=wikipediaapi.ExtractFormat.WIKI)

    trans = Translator(service_urls=['translate.googleapis.com'])
    result = trans.translate(class_name, dest='ko', src='en')
    class_name = result.text
    print(class_name)
    p_wiki = wiki.page(class_name)

    print("Page - Exists: %s" % p_wiki.exists())

    if(p_wiki.exists()):
        print(p_wiki.text)

#search from site
def dogSite(class_name):
    html = urlopen("https://www.akc.org/?s=" + class_name)
    bsObject = BeautifulSoup(html,"html.parser")

    secondURL = None

    #get secondURL 
    for link in bsObject.find_all('a'):
        url = link.get('href')
        if url is not None:
            if("/dog-breeds/" in url) and not(url.endswith("/dog-breeds/")):
                secondUrl = url
                print(link.text.strip(), url)
                break

    
    #search at secondURL
    if secondUrl is not None:
        html = urlopen(secondUrl)
        bsObject = BeautifulSoup(html,"html.parser")

        result = []
        
        name = bsObject.find("h1",{"class" : "page-header__title"}).string
        name = name.replace("\n","").strip()

        for contents in bsObject.find_all("span",{"class":"attribute-list__text"}):
            result.append(contents.string)

        information = bsObject.find("div",{"class" : "breed-hero__footer"}).string
        information = information.replace("\n","").strip()

        print(result)

        return name, result, information