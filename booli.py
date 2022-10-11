from bs4 import BeautifulSoup
import time
import requests

url = "https://www.booli.se/annons/4540360"
MAX_PAGES = 1

class Booli:

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
        
        # Get html
        #headers=HEADERS
        html = requests.request("GET", url_link)
        soup = BeautifulSoup(html.text, "html.parser")

        
        # Url link
        listings['Länk'] = url_link

        # Street address
        street_address = soup.find('h1', {'class': 'lzFZY _10w08'}).get_text()
        print(street_address)
        listings['Adress'] = street_address

        #BRF name
        #Eftersom h3an jag vill få fram har samma class som den översta så kommer jag inte åt den undre.
        brf_name = list(soup.find('div', {'class': '_36W0F mz1O4'}).get_text().split('\n'))[0]
        print(brf_name)

        '''
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
        '''
        self.listings.append(dict(listings))
        

    def run(self):
        self.scrape_link(url)
        print(self.listings)

boo = Booli()
boo.run()
