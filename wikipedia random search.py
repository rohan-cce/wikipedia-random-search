import bs4
#   Beautiful Soup is a Python library for pulling data out of HTML

import requests
#   to make http requests

import pyfiglet as pf
#   with this module we can convert regular strings in to ASCII art fonts

import sys
#    for using sys.exit() function
import time
#   for time.sleep() function

word=pf.figlet_format("wikipedia random search")
#with this command we can convert the string "Wikipedia random search" into ASCII art font

print(word)

def wiki_random_search():
    

    page=''
    
    while page=='':
        """ we are using while loop with page='' here
       because we will be trying to get data using requests.get()
       until we get the data"""
        try:

            response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            #sends a GET request to the specified article
            
            break
            #after we get the data we dont need to use a request again so we are breaking out of the loop
        
        except:
            
            time.sleep(5)
            #sleeps for  5 seconds 

            continue
            #try again to request data     
        
    if response is not None:
        #after we get the response and response is not empty we are now selecting the title and display in the program

        html = bs4.BeautifulSoup(response.text, 'html.parser')
        #we use this statement to select and copy the html code [ <html>.....</html> ]

        title = html.select("#firstHeading")[0].text
        #we use this statement to select content in <title> tag

        print("----------------------------------------------")

        print("random generated is :",title,"\n")
        #printing the title of random generated article

        print("If you wish to read this article press -y- :\n")        

        c=input()
        #asking input from user whether they are interested in reading the random generated article

        if c[:1]=='y' or c[:1]=='Y':
            #if input is y then proceeding to display the article

            print("searching for %s in wikipedia"%title)

            print("------------------------------------")

            paragraphs = html.select("p")
            #selecting and copying the content inside <p></p> html tag

            for para in paragraphs:
                print (para.text)
                #printing the contents
            


            print("-----------------------------------------------------")
            
            time.sleep(5)
            #sleep for 5 seconds
            
            print("if want to continue reading articles press -y-")
            #if user wants to continue reading ,user can press y
            
            ch=input()
            if ch[:1]=='y' or ch[:1]=='Y':

                wiki_random_search()
                #if 'y' is inputted call the function again to generate a random wikipedia article

            else:
                print("""Thank You for using wikipedia random search
                                    Exiting please wait             """)                              

                time.sleep(3)

                sys.exit(0)
                #exiting
                
        else:

            print("generating other article please wait\n")
            #if user is not interested in recently randomly generated article he can again generate a random article
            
            wiki_random_search()

wiki_random_search()
