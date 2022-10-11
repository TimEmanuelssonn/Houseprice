# Ändra länk

CSV_HEADER = {
    "Adress" : None,
    "Område" : None,
    "Region" : None,
    "Avstånd till T-centralen" : None,
    "Datum" : None,
    "Slutpris" : None,
    "Begärt pris" : None,
    "Bostadstyp" : None,
    "Upplåtelseform" : None,
    "Antal rum" : None,
    "Boarea" : None,
    "Balkong" : None,
    "Våning" : None,
    "Hiss" : None,
    "Byggår" : None,
    "Avgift/månad" : None,
    "Driftskostnad" : None,
    "Länk" : None
}

URLS = {
    #'Vällingby' : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925953&item_types%5B%5D=bostadsratt"
    #"Vasastan" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925970&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Östberga" : "https://www.hemnet.se/salda/bostader?item_types%5B%5D=bostadsratt&location_ids%5B%5D=473447&rooms_max=2&rooms_min=2",
    #"Södermalm" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=898472&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Kungsholmen" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925968&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Östermalm" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=473448&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Årsta" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=473440&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    "Bromma" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=898740&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Solna" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=18028&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Sundbyberg" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=18042&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Hammarbyhöjden-Skarpnäck" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925963&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Torsplan" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=475665&item_types%5B%5D=bostadsratt",
    #"Hammarby sjöstad" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925972&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Enskede" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925961&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Midsommarkransen" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=473396&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Gröndahl_Liljeholmen_Kajen" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=909928&location_ids%5B%5D=473385&location_ids%5B%5D=473346&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Norrmalm" : "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925969&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2",
    #"Nacka": "https://www.hemnet.se/salda/bostader?location_ids%5B%5D=473483&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2"

}

HEADERS = {
'Cookie': 'hn_exp_kpis=310; hn_exp_bstp=799; hn_exp_ese=26; hn_exp_spp=765; hn_exp_sss=614; hn_exp_ssr=640; hn_exp_nsp=719; __cfruid=709d4687ee26f8224371096f96e2d082c3853d5e-1661960849; __couid=eb30023a-4f3c-41a8-827a-c840eef38a5b; __codnp=; _gcl_au=1.1.565659984.1661960851; _gid=GA1.2.747562430.1661960851; _ga2=GA1.2.1619059294.1661960849; _hemnet_selling_price_result_settings_sorting=sale_date+desc; _hemnet_session_id=RFVJdVlSYWpOYUZyRWpGeTM5L1NITXB4Nkx6dTNwVG53SXpjNXFMWXRaL3loUzFOTDk5b1gvSHRkY0pNcVVualhPMVJVeTFScFFidEw5YW95ZTlwMXRhNFl6UTl0RXNtVFk0MzBMUnpLRTZtSVJSbTdEVFpnK2M1UXhUU3l5c0oxTUtkVm0xZ2tCZTlGakt6T1MrM0tyV1hvbTJGZGE2bE5DS0tEMytoTG1WY2pmWDJhK2hJM2xVbkRYa0FTZS9ULS1jUXp1bDhweTQ2dUtlR2FiSjEwMzNBPT0%3D--376cbd199e671e44d72d2dfba108028a033bd4e4; _ga_42YRRBRWVM=GS1.1.1661960849.1.1.1661961763.0.0.0; _ga=GA1.2.1619059294.1661960849; _hjSessionUser_420875=eyJpZCI6Ijk3MDA0OGU4LTZmYjItNTg0Mi1hNzNlLTkzOTIyZjdhYjI4NSIsImNyZWF0ZWQiOjE2NjE5NjEwMDg4OTYsImV4aXN0aW5nIjp0cnVlfQ==',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language' : 'en-US,en;q=0.9',
'Connection': 'keep-alive'
}

MAX_PAGES = 1
GOOGLEAPI = False
