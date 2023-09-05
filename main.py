import os
import json
from country import Country
from brewery import Brewery
from settings import countries, active_breweries, inactive_breweries, active_breweries_details, inactive_breweries_details


def write_to_file(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)


def collect_initial_data():
    print('Collecting initial data...')
    active_data = []
    inactive_data = []

    for country in countries:
        print(f'Collecting data for {country["name"]}...')
        country = Country(country)
        country_page = country.get_country_page()
        active_data.extend(country.get_breweries(country_page, 'active'))
        inactive_data.extend(country.get_breweries(country_page, 'closed'))

    write_to_file(active_data, active_breweries)
    write_to_file(inactive_data, inactive_breweries)
    print('Data collection complete')


def scrape_brewery_data():
    print("Scraping brewery data...")

    with open(active_breweries, 'r') as f:
        data = json.load(f)

    if os.path.exists(active_breweries_details):
        with open(active_breweries_details, 'r') as f:
            brewery_details_data = json.load(f)
    else:
        brewery_details_data = []

    existing_brewery_names = set(brewery['name'] for brewery in brewery_details_data)

    for row in data:
        brewery_name = row['name']

        if brewery_name in existing_brewery_names:
            print(f"Skipping {brewery_name} as it already exists in file.")
            continue

        brewery = Brewery(row)
        brewery_page = brewery.get_brewery_page()
        brewery_details = brewery.get_brewery_details(brewery_page)

        formatted_data = brewery.format_data(brewery_details)
        print(formatted_data)

        brewery_details_data.append(formatted_data)
        write_to_file(brewery_details_data, active_breweries_details)


def main():
    cls = 'cls' if os.name == 'nt' else 'clear'
    os.system(cls)

    while True:
        print("""
UK Brewery Scraper (ratebeer.com)
---------------------------------

1. Collect initial brewery data
2. Scrape brewery data
3. Exit
""")

        ans = input("Please choose an option: ")
        if ans == "1":
            collect_initial_data()
        if ans == "2":
            scrape_brewery_data()
        if ans == "3":
            return False


if __name__ == '__main__':
    main()
