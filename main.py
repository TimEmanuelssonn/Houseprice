from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
import requests
from config import *
from api import *
import json

api_key = APIKEY
googleapi = GOOGLEAPI

class Main:

    def __init__(self) -> None:
        self.links = []
        self.listings = []

    def extract_every_page(self, base_url):

        # range(1 - 51) == 1 - 50
        for page in range(1,MAX_PAGES+1):

            url = base_url
            url = url + f"&page=" + str(page)
            self.extract_all_link(url)

    def extract_all_link(self, url_page):

        try:

            response = requests.request("GET", url_page, headers=HEADERS)

            html = response.text
        
            soup = BeautifulSoup(html, "html.parser").find_all('a', {'class': 'sold-property-link js-sold-property-card-link'})
            
            for link in soup:
                self.links.append(link.get("href"))
        
        except Exception as e:
            print(e)
            print("no links at page " + url_page)

    def open_link(self):
        page_count = 0
        page = 0
        for i, link in enumerate(self.links):
            print(f"On link {i}")
            page_count += 1
            if (page_count == 50):
                #page +=1
                print("Done")
                #print(f"On page : {page}")
                page_count = 0
            
            self.scrape_link(link)

    def scrape_link(self, url_link):

        listings = {}
        #time.sleep(1)
        
        
        # Get html
        html = requests.request("GET", url_link, headers=HEADERS)
        soup = BeautifulSoup(html.text, "html.parser")

        # Url link
        listings['Länk'] = url_link

        # Street address
        street_address = list(soup.find('h1', {'class': 'hcl-heading hcl-heading--size1'}).get_text().split('\n'))[2].replace('-', ',').split(',')[0].strip()
        listings['Adress'] = street_address

        if googleapi:
            distance_to_central = self.calculate_distance_to_central_station(street_address)
            listings['Avstånd till T-centralen'] = distance_to_central

        # Location
        location = list(soup.find('p', {'class' : 'sold-property__metadata qa-sold-property-metadata'}).get_text().split('\n'))[6].strip().split(',')[0]
        listings['Område'] = location

        # Region
        region = list(soup.find('p', {'class' : 'sold-property__metadata qa-sold-property-metadata'}).get_text().split('\n'))[6].strip().split(',')[1].strip()
        listings['Region'] = region

        # Date
        date = soup.find('time')['datetime']
        listings['Datum'] = date

        # Price sold
        sold_price = "".join(soup.find('span', {'class' : 'sold-property__price-value'}).get_text().strip('kr').split())
        listings['Slutpris'] = sold_price
        
        property_key = soup.find_all('dt', {'class' : 'sold-property__attribute'})
        property_key_details = [i.text.strip() for i in property_key]

        property_value = soup.find_all('dd', {'class' : 'sold-property__attribute-value'})
        property_value_details = [i.text.strip() for i in property_value]

        for index, keys in enumerate(property_key_details):
            
            if (keys == "Begärt pris"):
                listings[keys] = "".join(property_value_details[index].strip('kr').split())

            elif (keys == "Bostadstyp"):
                listings[keys] = property_value_details[index]

            elif(keys == "Upplåtelseform"):
                listings[keys] = property_value_details[index]
                
            elif(keys == "Antal rum"):
                listings[keys] = property_value_details[index].strip('rum')

            elif(keys == "Boarea"):
                listings[keys] = property_value_details[index].strip('m²').replace(',', '.')

            elif(keys == "Balkong"):
                balle = property_value_details[index]
                if(balle == "Ja"):
                    listings[keys] = 1
                else:
                    listings[keys] = 0

            elif(keys == "Våning"):
                listings[keys] = self.calculate_floor(property_value_details[index].split(',')[0])
                hiss = property_value_details[index].split(',')[-1].strip()
                if (hiss == "hiss finns"):
                    listings["Hiss"] = 1 
                else:
                    listings["Hiss"] = 0
                    
            elif(keys == "Byggår"):
                listings[keys] = property_value_details[index].split('-')[0]

            elif(keys == "Avgift/månad"):
                listings[keys] = "".join(property_value_details[index].strip('kr/mån').split())

            elif(keys == "Driftskostnad"):
                listings[keys] = "".join(property_value_details[index].strip('kr/år').split())

        self.listings.append(dict(listings))

    def calculate_floor(self, floor):

        if(len(floor) > 1):
            tempfloor = floor.split('av')[0]
            tempfloor = int(tempfloor)

            if(tempfloor < 2):
                return 0
            else:
                return 1
        elif(int(floor) < 2):
            return 0
        else:
            return 1

    def calculate_distance_to_central_station(self, street_adress):
        origin = street_adress.replace(' ','+')

        URL = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}+Stockholm&destinations=T-Centralen+Stockholm&mode=transit&key={api_key}"
        response = requests.get(URL)
        json_data = json.loads(response.text)
        
        if json_data['status'] == 'REQUEST_DENIED':
            raise ValueError("Request to google maps API was denied. API key provided was not valid")
        
        #Returns distance to T-central stations in secounds with public transport. Devide with 60 for minutes.
        return json_data['rows'][0]['elements'][0]['duration']['value']

    def write_to_csv(self, name):
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d")
        csv_filepath = f"csv/{dt_string}-{name}.csv"
        keys = CSV_HEADER.keys()
        
        with open(csv_filepath, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.listings)

    def run(self):
        start = time.time()
        current_start = time.time()
        
        for key in URLS:
            print(f"Starting.. {key}")
            self.extract_every_page(URLS[key])
            self.open_link()
            self.write_to_csv(key)
            self.links = []
            self.listings = []
            print(f"Finish with {key} area!")
            stop = time.time()
            print(f"{key} took {stop - current_start} seconds")
            current_start = 0

        end = time.time()
        print("Total time " + str(end - start))

if __name__ == "__main__":

    hem = Main()
    hem.run()




