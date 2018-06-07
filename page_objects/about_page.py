from page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class AboutPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.about_me_header = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'About Me')]")))
        self.about_me_post = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "entry-content")))

    @allure.step("Validate_about_me_header")
    def validate_about_me_header(self):
        assert self.about_me_header.is_displayed()

    @allure.step("Validate about me post")
    def validate_about_me_post(self):
        assert self.about_me_post.is_displayed()