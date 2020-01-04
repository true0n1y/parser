import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    targets = soup.find_all('section', class_='plugin-section')

    print(targets)




def main():
    url = "https://wordpress.org/plugins/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
