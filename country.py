import requests
from bs4 import BeautifulSoup
from settings import headers, base_url


class Country:
    def __init__(self, country):
        self.country_name = country['name']
        self.country_code = country['code']

    def get_country_page(self):
        target_href = f'/breweries/{self.country_name}/0/{self.country_code}/'
        html_content = requests.get(base_url + target_href, headers=headers).content
        return BeautifulSoup(html_content, 'html.parser')

    @staticmethod
    def get_breweries(content, state):
        results = []
        table = content.find('div', id=state).find('table')
        rows = table.findAll('tr')
        try:
            for row in rows[1:]:
                content = row.find_all('td')
                a_tags = content[0].find_all('a')
                data = {
                    'name': a_tags[0].text.strip(),
                    'url': base_url + content[0].find('a')['href'],
                    'type': content[1].text.strip(),
                    'city': a_tags[1].text.strip() if state == 'active' else content[0].find('span').text.strip(),
                    'country': 'United Kingdom'
                }
                results.append(data)
        except IndexError:
            pass
        return results
