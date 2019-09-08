import urllib
from bs4 import BeautifulSoup

# Base website
website = 'https://devpost.com/software/search?page='

# Keyword looking to be found
keyword = "Oh no! Looks like there's no software matching your query."


# Checks if the keyword is on the desired page
def content_check(page):
    html = urllib.request.urlopen(website + str(page)).read()
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    return text.find(keyword) != -1


# Preforms a binary search to find the last page
def binary_search():    
    i = 10000
    currentPage = 0
    pastPage = i
    state = False

    while True:
        state = bool((int(state) + 1) % 2)
        i = i // 2

        while content_check(currentPage) == state:        
            if currentPage == pastPage:
                return currentPage
            else:
                pastPage = currentPage

            if state == True:
                currentPage -= i
            else:
                currentPage += i



#pulls text and converts into txt file
def pull_text(page):
    html = urllib.request.urlopen(website + str(page)).read()
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    # print(text)

    pageText = open('PageText.txt','w')
    pageText.write(text)
    pageText.write('\n')


for page in range(2):
    pull_text(page + 1)


def extract_links(page):
    html = urllib.request.urlopen(website + str(page)).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.findAll('a')
    keyphrase = "https://devpost.com/software/"
    linkList = []

    for t in tags:
        text = t.attrs['href']
        if text.find(keyphrase) != -1 and text.find('https://devpost.com/software/search?page=') == -1:
            linkList.append(t.attrs['href'])
    
    return linkList

for page in range(2):
    print(extract_links(page + 1))

    

    

# Get the max page count
# def get_page_count()
#     for 

# lastPage = 

# for link in devpost.find_all('page='):
#     print(link)

# print(devpost)
