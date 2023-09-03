import time
import secrets
from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleForm:
    def __init__(self, links: list[str], addresses: list[str], rents: list[str]):
        self.links, self.addresses, self.rents = links, addresses, rents

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(secrets.FORM_URL)
        self.driver.maximize_window()

        time.sleep(1.5)
        self.submit_form()

    def submit_form(self):
        for i in range(len(self.links)):
            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/'
                                                                     'div/div[2]/div/div[1]/div/div[1]/input')
            rent_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/'
                                                                  'div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/'
                                                                  'div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]'
                                                                     '/div[1]/div/span/span')

            address_input.send_keys(self.addresses[i])
            rent_input.send_keys(self.rents[i])
            link_input.send_keys(self.links[i])
            submit_button.click()

            time.sleep(1)

            submit_another = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_another.click()
            time.sleep(1)
