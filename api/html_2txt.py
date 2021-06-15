from bs4 import BeautifulSoup
import logging
import html2text
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests


def print_menu():
    print("Please Select a Menu Option:")
    print("1. Enter Url to pull text using html2text")
    print("2. Enter URL to pull text with beautiful soup")
    print("3. Exit")


def get_article(html: str):
    """
    Retrieves all text with the <p> html tag

    :param html: html page content retrieved from url
    :return: plaintext webpage contents
    """
    soup = BeautifulSoup(html, "html.parser")

    article_text = ''
    article = soup.find_all('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text=True))
    return article_text


def scrapeSite(url: str):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
        
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    # get text
    text = soup.get_text() 
    headers = extractHeaders(url) 
    paragraphs = extractParagraphs(url)
    text = cleanText(text, headers, paragraphs)
    return text


def extractHeaders(url: str):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    # extract all the current titles 
    titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])

    results = []
    #clean headers 
    for t in titles:      
        h = BeautifulSoup(str(t), "lxml").text
        h = h.strip()
        results.append(h)

    return results


def extractParagraphs(url: str):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    # extract all the current paragraphs
    para = bs.find_all(['p'])

    results = []
    #clean paragraphs
    for p in para:      
        x = BeautifulSoup(str(p), "lxml").text
        x = x.strip()
        results.append(x)

    return results


def extract_seperated_text(url : str):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script', ]
    # there may be more elements you don't want, such as "style", etc.

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    print(output)


def cleanText(txt: str, headers: list, paragraphs: list):
    page ="---Full Page Text---"
    start = '***START OF PAGE READ ***'
    end = '***END OF PAGE READ ***'
    head = "---All Headers---"
    para = "---All Paragraphs---"

    txt = txt.replace('\n','')
    txt = txt.replace('\r','')
    txt = txt.replace('\t','')
    txt = txt.replace('-','')

    return page, start, txt, end, head, headers, para, paragraphs


def run_test():
    menu_choice = "0"
    
    while menu_choice != "3":
        logging.debug("While Loop 1 started...")
        print()
        print_menu()
        menu_choice = input().strip()
        logging.debug("Menu Choice {} Selected...".format(menu_choice))
    
        if menu_choice == "1":      
            # Enter url to classify example http://news.bbc.co.uk/2/hi/health/2284783.stm
            url = input("Enter URL: ").strip()
            logging.debug("Entered URL: {}".format(url))
        
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            
            # get text
            text = soup.get_text()
            print(html2text.html2text(text))
    
        elif menu_choice == "2":
            
            # Enter url to classify example http://news.bbc.co.uk/2/hi/health/2284783.stm
            url = input("Enter URL: ").strip()
            logging.debug("Entered URL: {}".format(url))
        
            html = urlopen(url).read()
            soup = BeautifulSoup(html)
            
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            
            # get text
            text = soup.get_text()       
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            print(text)
                  
            logging.debug("url text found sucessfuly") 
            
        else:
             print("Menu choice invalid to exit press 3:")
    
        logging.debug("End of While Loop 1 Reached")





#run_test()
#extract_seperated_text('https://wordpress.com/create-blog/')

# test urls
#https://www.joescrabshack.com/
#https://wordpress.com/create-blog/
#https://en.wikipedia.org/wiki/Main_Page
#