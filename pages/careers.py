from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Careers:
    url = 'https://www.optimove.com/careers'
    offices_dropdown = (By.CSS_SELECTOR, '.selectric-hide-select>select')
    button_locator = (By.CSS_SELECTOR, '.selectric>.button')
    ukr_positions = (By.CSS_SELECTOR, 'div[data-location="UKR"] .job-card__title>a')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.url)

    def select_ukr_offices(self):

        action_chains = ActionChains(self.browser)
        action_chains.move_by_offset(200, 300).click().perform()

        self.click_on_button(self.button_locator)

        select_element = self.browser.find_element(*self.offices_dropdown)
        option_value = "UKR"
        for _ in range(10):
            select_element.send_keys(Keys.DOWN)  # Move down multiple times
            select_element.send_keys(Keys.ENTER)
            selected_option = select_element.get_attribute("value")
            if selected_option == option_value:
                break

    def click_on_button(self, button_location):
        btn_element = self.get_element_if_present(button_location)
        btn_element.click()

    def get_element_if_present(self, locator):
        try:
            element = WebDriverWait(self.browser, 2).until(
                EC.presence_of_element_located(locator))
        except:
            self.browser.refresh()
            try:
                element = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located(locator))
            except:
                raise Exception(
                    f"{locator} is not present on the page after reloading")
        return element

    def position_present_in_ukr(self,  title):
        elements = WebDriverWait(self.browser, 2).until(
            EC.presence_of_all_elements_located(self.ukr_positions))
        text_values = [element.text for element in elements]
        if title in text_values:
            return True
        else:
            print('Position is not found. Current opened positions:')
            print(text_values)
            return False
