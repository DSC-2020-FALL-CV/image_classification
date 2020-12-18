#pip install wikipedia -api
import wikipediaapi

#pip install git+https://github.com/alainrouillon/py-googletrans@feature/enhance-use-of-direct-api
from googletrans import Translator

#english word -> translate korean -> search wiki
def wiki(class_name):
    wiki = wikipediaapi.Wikipedia( 
        language='ko', 
        extract_format=wikipediaapi.ExtractFormat.WIKI)

    trans = Translator(service_urls=['translate.googleapis.com'])
    class_name = trans.translate(class_name, dest='ko', src='en')
    print(class_name)
    p_wiki = wiki.page(class_name.text)

    print("Page - Exists: %s" % p_wiki.exists())

    if(p_wiki.exists()):
        print(p_wiki.text)