import re

from bs4 import BeautifulSoup
import requests

TEST_ENABLED = False

URL = 'http://matfyzak.cz/rzrv/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
PARSER_REGEX = r'volných (\d+) \(\+(\d+) u prodejců\)'

NIMROD_URL = 'https://www.nimrod-messenger.io/api/v1/message'
NIMROD_API_KEYS = ['71c906ad-8e09-4a7e-aca9-7983cb2eabfe', '8fa62c01-1f57-4afe-a584-4e637cc6d910']
RESULT_MESSAGE = 'POZOR Damiane!!!\nJe volnych {} listku a {} u prodejcu!!!\n{}\nMAKEJ...\nTed dluzis pivo ty mi. 🍻'


response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, features="html.parser")
text = str(soup.select('table.table-striped.table-hover tbody tr:nth-of-type(2) td')[2].text).strip()

result = re.findall(PARSER_REGEX, text)[0]
available_tickets, seller_tickets = int(result[0]), int(result[1])

if available_tickets or seller_tickets or TEST_ENABLED:
    for key in NIMROD_API_KEYS:
        requests.post(
            NIMROD_URL,
            data={
                'api_key': key,
                'message': RESULT_MESSAGE.format(available_tickets, seller_tickets, URL)
            }
        )
