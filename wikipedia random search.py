import bs4
import requests
import pyfiglet as pf
import sys
import time

word=pf.figlet_format("wikipedia random search")
print(word)
def wiki_random_search():
    page=''
    while page=='':
        try:
            response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            break
        except:
            time.sleep(5)
            continue
    
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')

        title = html.select("#firstHeading")[0].text

        print("----------------------------------------------")

        print("random generated is :",title,"\n")

        print("If you wish to read this article press -y- :\n")        

        c=input()

        if c[:1]=='y' or c[:1]=='Y':

            print("searching for %s in wikipedia"%title)
            print("------------------------------------")
            paragraphs = html.select("p")
            for para in paragraphs:
                print (para.text)

            intro = '\n'.join([ para.text for para in paragraphs[0:5]])
            print (intro)
            
            print("-----------------------------------------------------")
            
            time.sleep(5)
            print("if want to continue reading articles press -y-")
            ch=input()
            if ch[:1]=='y' or ch[:1]=='Y':
                wiki_random_search()
            else:
                print("""Thank You for using wikipedia random search
                                    Exiting please wait             """)
                time.sleep(3)
                sys.exit(0)                
        else:
            print("generating other article please wait\n")
            wiki_random_search()

wiki_random_search()
