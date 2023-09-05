from playwright.sync_api import sync_playwright
from parsel import Selector
from utils.geocode import get_brewery_coordinates


class Brewery:
    def __init__(self, brewery):
        self.name = brewery['name']
        self.url = brewery['url']  # url for brewery details
        self.type = brewery['type']
        self.city = brewery['city']
        self.country = brewery['country']

    def get_brewery_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            page.wait_for_timeout(3000)
            return page.content()

    @staticmethod
    def get_brewery_details(page):
        selector = Selector(text=page)
        address_xpath = '//*[@id="root"]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[3]/a/div/text()'
        website_xpath = '//*[@id="root"]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[5]/a/@href'
        telephone_xpath = '//*[@id="root"]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[4]/a/div/text()'
        address = selector.xpath(address_xpath).get()
        website = selector.xpath(website_xpath).get()
        telephone = selector.xpath(telephone_xpath).get()
        return {
            'address': address,
            'website': website,
            'telephone': telephone
        }

    def format_data(self, brewery_details):
        address = ','.join(brewery_details['address'].split(',')[0: -4])
        postcode = brewery_details['address'].split(',')[-2].strip()
        city = self.city.split(',')[0]
        county = brewery_details['address'].split(',')[-3].strip()
        coordinates = get_brewery_coordinates(address, postcode, self.country)

        return {
            'name': self.name,
            'brewery_type': self.type.lower(),
            'address 1': address,
            'address 2': None,
            'address 3': None,
            'city': city,
            'state_province': county,
            'postal_code': postcode,
            'country': self.country,
            'longitude': coordinates[0] if coordinates else None,
            'latitude': coordinates[1] if coordinates else None,
            'phone': brewery_details['telephone'],
            'website_url': brewery_details['website'],
            'state': county,
            'street': address
        }

