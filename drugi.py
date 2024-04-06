import requests
from bs4 import BeautifulSoup

res = []
for i in range(1400):
    response = requests.get(f'https://www.realitica.com/?cur_page={i}&for=Prodaja&pZpa=Istra&pState=hrvatska&type%5B%5D=&since-day=p-anytime&qob=p-default&lng=hr')
    soup = BeautifulSoup(response.content, 'html.parser')
    found_divs = soup.find_all('div',
                        style="padding:15px 10px;clear:both;white-space: normal; overflow: hidden; text-overflow: ellipsis; border: 1px solid #ccc; background:#fff9dd;")

    for elem in found_divs:
        pass # just pull demand elements by tags

# and then save all in .csv throw DictWriter