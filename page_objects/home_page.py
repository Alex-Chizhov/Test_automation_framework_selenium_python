# Our first Page Object.
# This class will represent the Home Page of our site and have all the web elements needed.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))
        self.icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        self.primary_menu = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, "primary-menu")))
        self.post_list = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))
        self.twitter_button = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Twitter')]")))
        self.linkedin_button = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'LinkedIn')]")))
        self.first_post = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//article[1]//h2/a")))

    @allure.step("Click Blog's first post")
    def click_first_post(self):
        self.first_post.click()

    @allure.step("Click about me link")
    def click_about_me_link(self):
        about_me_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://qaboy.com/about-me/']")))
        about_me_link.click()

    @allure.step("validate_title_is_present")
    def validate_title_is_present(self):
        assert self.title.is_displayed()

    @allure.step("validate_icon_is_present")
    def validate_icon_is_present(self):
        assert self.icon.is_displayed()

    @allure.step("validate_menu_options_are_present")
    def validate_menu_options_are_present(self):
        assert self.primary_menu.is_displayed()

    @allure.step("validate_posts_are_visible")
    def validate_posts_are_visible(self):
        assert len(self.post_list) > 0

    @allure.step("validate_social_media_links")
    def validate_social_media_links(self):
        assert self.twitter_button.is_displayed()
        assert self.linkedin_button.is_displayed()
