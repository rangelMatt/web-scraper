import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  
  page = requests.get(url)

  # print(page.content)
  soup = BeautifulSoup(page.content, "html.parser")
  # print(type(soup))

  results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  # print(results.prettify())
  print(f"{len(results)} Citations requested for Wiki Article.")

get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")

print("""
      
--------------- 

      """)

def get_citations_needed_report(url):
  page = requests.get(url)
  # print(page.content)

  soup = BeautifulSoup(page.content, "html.parser")
  # print(type(soup))

  results = soup.find_all(class_="noprint Inline-Template Template-Fact")
  
  for result in results:
    print(f"{result.parent.text} CITATION NEEDED HERE.")

# return len(results)

(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))