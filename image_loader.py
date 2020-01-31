from bs4 import BeautifulSoup
import requests
import hashlib
import json

URL = 'http://www.humansnotinvited.com/'

def add_hash_to_memory(category_name, img_hash):
    if category_name in memory:
        if img_hash in memory[category_name]:
            memory[category_name][img_hash] += 1
            print('update counter in category {0}'.format(category_name))
        else:
            memory[category_name][img_hash] = 1
            print('add new hash in category {0}'.format(category_name))
    else:
        memory[category_name] = { img_hash: 1 }
        print('add new category {0}'.format(category_name))

with open('D:\\solver_memory.json', 'r') as file:
    memory = json.load(file)

counter = 0

while counter < 2:
    print(15 * '-')
    counter += 1

    html_doc = requests.get(URL).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    input_tag = soup.find_all("input")[0]
    category_name = input_tag['value']

    div_containers = soup.find_all('div', class_='captcha-image')

    for div in div_containers:
        img = div.find_next('img')
        img_url = URL + img['src']
        img_data = requests.get(img_url).content

        img_hash = str(hashlib.md5(img_data).hexdigest())
        add_hash_to_memory(category_name, img_hash)

with open('D:\\solver_memory.json', 'w') as file:
    json.dump(memory, file, indent=2)