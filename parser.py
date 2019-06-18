import re
import time

import requests
from bs4 import BeautifulSoup as bs

REGULAR_EXPRESSION_LINK = re.compile('tel:.{11,20}')
REGULAR_EXPRESSION_DIV = re.compile('[8+].{11,20}')


def extract_number(string):
    result = REGULAR_EXPRESSION_DIV.search(string)
    extract = string[result.start():result.end()]
    number = ''
    index = 0
    while len(number) < 12 and index < len(extract):
        if extract[index].isdigit():
            number += extract[index]
        index += 1
    if number[0] == '7':
        number = '8' + number[1:]
    return number


def clear_number(string):
    number = ''
    for i in string:
        if i.isdigit():
            number += i
    return number


def change_7_to_8(number):
    if number[0] == '7':
        number = '8' + number[1:]
    elif number[0] == "+":
        number = '8' + number[2:]
    return number


def parse(url, headers):
    session = requests.Session()

    try:
        request = session.get(url, headers=headers)
    except:
        print('error connecting to', url)
        return []

    if request.status_code == 200:
        time_start = time.time()
        soup = bs(request.content, 'lxml')
        links = soup.find_all('a', href=REGULAR_EXPRESSION_LINK)
        numbers = set()

        for link in links:
            number = link.get('href').split(':')[1]
            number = change_7_to_8(number)
            if number.isdigit() != True:
                number = clear_number(number)
            numbers.add(number)

        if len(numbers) == 0:
            divs = soup.find_all('div', attrs={'class': 'phones'})
            for div in divs:
                number = clear_number(div.text)
                while len(number) >= 11:
                    numbers.add(change_7_to_8(number[:11]))
                    number = number[11:]

        if len(numbers) == 0:
            divs = soup.find_all('div', text=REGULAR_EXPRESSION_DIV)
            for div in divs:
                number = div.text
                numbers.add(change_7_to_8(extract_number(number)))

        return [numbers, str(time.time() - time_start)]
    else:
        print('error connecting to', url)
        return []
