import requests
from bs4 import BeautifulSoup

URL = "http://www.ans.gov.br"

def get_links(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'lxml')
  links = soup.find_all('a')
  return links

def get_version(links, title):
  for link in links:
    if title in link.text:
      add = link.attrs['href']
      return add

def save_PDF(filename, content):
  open(filename,'wb').write(content)

if __name__ == '__main__':
  address = "/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
  title = "Padrão TISS – "
  name = "Componente Organizacional"
  links = get_links(URL + address)
  nextAddress = get_version(links, title)
  nextLinks = get_links(URL + str(nextAddress))
  downloadAddress = get_version(nextLinks, name)
  res = requests.get(URL + str(downloadAddress))
  filename = downloadAddress.split("/")[-1]
  save_PDF(filename, res.content)