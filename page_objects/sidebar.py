# right sidebar repeats itself on all pages.
# This is a good candidate for a Page Object so we can isolate the testing of that section.
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideBar:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "search-field")))
        self.search_submit = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "search-submit")))
        self.user_comment = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[@class='recentcomments'][1]/a")))
        self.category_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, "//section[@class='widget widget_categories']//li[1]/a")))

    @allure.step("Search for an Article")
    def search_for_article(self, article_title):
        self.search_bar.send_keys(article_title)
        self.search_submit.click()

    @allure.step("Click user comment")
    def click_user_comment(self):
        self.user_comment.click()

    @allure.step("Click category")
    def click_category(self):
        self.category_link.click()