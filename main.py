from zillow_beast import ZillowBeast
from google_form import GoogleForm
APARTMENTS_URL = "https://www.apartments.com/westwood-los-angeles-ca/min-2-bedrooms-1-bathrooms-under-4000/"


zb = ZillowBeast(APARTMENTS_URL)
links = zb.get_links()
addresses = zb.get_addresses()
rents = zb.get_prices()

form = GoogleForm(links, addresses, rents)
