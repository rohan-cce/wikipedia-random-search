import webbrowser as wb
import bs4
import requests
import pyfiglet as pf

word=pf.figlet_format("wikipedia random search")

print(word)

def wiki_random_search():
    
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')

        title = html.select("#firstHeading")[0].text

        print("----------------------------------------------")

        print("random generated is :",title,"\n")

        print("If you wish to read this article press -y- :\n")        

        c=input()

        if c[:1]=='y' or c[:1]=='Y':

            print("Opening browser and searching for %s in wikipedia"%title)

            s="https://en.wikipedia.org/wiki/"+title

            wb.open(s)

        else:

            print("generating other article please wait\n")

            wiki_random_search()

wiki_random_search()
