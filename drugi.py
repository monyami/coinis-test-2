import requests
from bs4 import BeautifulSoup
from re import compile, match
from fake_useragent import UserAgent as ua
import csv


def add_key_value(found_items: dict, key_name: str, text: str):
    item = soup.find('strong', text=text)
    if not item:
        return

    item = item.find_next_sibling(text=True)
    if not item:
        return

    value = item.replace(':', '').strip()
    if value.isdigit():
        found_items[key_name] = int(value)
        return
    try:
        temp = None
        if '€' in value:
            temp = value.replace('€', '').replace('.', '')
        elif 'm' in value:
            temp = value.replace('m', '').replace('.', '')
        float(temp)
        if temp:
            found_items[key_name] = float(temp)
        elif value:
            found_items[key_name] = float(temp)
    except:
        found_items[key_name] = value


res = []
for i in range(1):
    response = requests.get(f'https://www.realitica.com/?cur_page={i}&for=Prodaja&pZpa=Istra&pState=hrvatska&type%5B%5D=&since-day=p-anytime&qob=p-default&lng=hr')
    soup = BeautifulSoup(response.content, 'html.parser')
    found_divs = soup.find_all('a', href=compile(r"https://www.realitica.com/hr/listing/\d+"))
    links = set()
    for elem in found_divs:
        links.add(elem['href'])

    for link in links:
        found_items = {
            'title': 'Nema podataka',
            'city': 'Nema podataka',
            'location': 'Nema podataka',
            'beds_number': 0,
            'bathrooms': 0,
            'price': 0.0,
            'living_area': 0.0,
            'land_area': 0.0,
            'parking_places': 0,
            'distance_from_sea': 0,
            'new_construction': False,
            'air_conditioning': False,
        }
        response = requests.get(link, headers={'User-Agent': ua().random})
        soup = BeautifulSoup(response.content, 'html.parser')

        add_key_value(found_items, 'title', 'Vrsta')
        add_key_value(found_items, 'city', 'Područje')
        add_key_value(found_items, 'location', 'Adresa')
        add_key_value(found_items, 'beds_number', 'Spavaćih Soba')
        add_key_value(found_items, 'bathrooms', 'Kupatila')
        add_key_value(found_items, 'price', 'Cijena')
        add_key_value(found_items, 'living_area', 'Stambena Površina')
        add_key_value(found_items, 'land_area', 'Zemljište')
        add_key_value(found_items, 'parking_places', 'Parking Mjesta')
        add_key_value(found_items, 'distance_from_sea', 'Od Mora (m)')
        item = soup.find('strong', text='Novogradnja')
        if item:
            found_items['new_construction'] = True
        item = soup.find('strong', text='Klima Uređaj')
        if item:
            found_items['air_conditioning'] = True

        res.append(found_items)

with open('realitika.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=res[0].keys())
    writer.writeheader()
    writer.writerows(res)

# and then save all in .csv throw DictWriter
