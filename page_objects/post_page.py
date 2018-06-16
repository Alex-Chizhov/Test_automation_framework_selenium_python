import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class PostPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.post_image = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='post-thumbnail-wrap']")))
        self.published_date = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".entry-date.published")))
        self.share_buttons_container = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='the_champ_sharing_container the_champ_horizontal_sharing']")))
        self.comment_form = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//form[@id='commentform']")))
        self.article_title_on_page = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='entry-title']")))

    @allure.step("Validate post image")
    def validate_post_image(self):
        assert self.post_image.is_displayed()

    @allure.step("Validate post published date")
    def validate_published_date(self):
        assert self.published_date.is_displayed()

    @allure.step("Validate post share buttons")
    def validate_share_buttons(self):
        assert self.share_buttons_container.is_displayed()

    @allure.step("Validate post Comment section")
    def validate_comment_section(self):
        assert self.comment_form.is_displayed()

    @allure.step("Validate article title")
    def validate_article_title(self, article_title):
        real_title = self.article_title_on_page.text
        expected_title = article_title
        assert real_title == expected_title
