from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # this is another way to create a page object element
    # self.country = "country"

    country = (By.ID, "country")
    country_link_text = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_btn = (By.CSS_SELECTOR, "[type='submit']")
    alert_success = (By.CSS_SELECTOR, "[class*='alert-success']")

    def enter_country(self):
        self.driver.find_element(*ConfirmPage.country).send_keys("ind")

    def click_country(self):
        self.driver.find_element(*ConfirmPage.country_link_text).click()

    def click_checkbox(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def click_submit_btn(self):
        self.driver.find_element(*ConfirmPage.submit_btn).click()

    def get_alert_text(self):
        text = self.driver.find_element(*ConfirmPage.alert_success).text
        return text

# def enter_country(self):
#    self.driver.find_element_by_id(self.country).send_keys("ind")
