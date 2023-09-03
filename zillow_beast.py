import requests
from bs4 import BeautifulSoup


class ZillowBeast:
    def __init__(self, url):
        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/116.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5"
        }
        self.url = url
        response = requests.get(self.url, headers=self.HEADERS)
        content = response.text
        self.soup = BeautifulSoup(content, "html.parser")

        self.links, self.prices, self.addresses = [], [], []
        self.mortar_wrappers: list

    def get_links(self) -> list[str]:
        placardContainer = self.soup.find("div", {"id": "placardContainer", "class": "placardContainer"})
        ul_element = placardContainer.find("ul")
        self.mortar_wrappers = ul_element.find_all("li", class_="mortar-wrapper")

        for li_element in self.mortar_wrappers:
            self.links.append(li_element.find('a').get("href"))

        return self.links

    def get_prices(self) -> list[str]:
        for link in self.links:
            mini_response = requests.get(link, headers=self.HEADERS)
            mini_content = mini_response.text
            mini_soup = BeautifulSoup(mini_content, "html.parser")
            rent = mini_soup.select_one(".rentInfoDetail").get_text(strip=True)
            self.prices.append(rent)

        return self.prices

    def get_addresses(self) -> list[str]:
        self.addresses = [li.select_one(".property-address").get_text(strip=True) for li in self.mortar_wrappers]
        return self.addresses
