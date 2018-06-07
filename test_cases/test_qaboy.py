# This file will be our Test Suite and will store all the test cases for our QABoy site.
import unittest
from webdriver import Driver
from values import strings
from page_objects.home_page import HomePage
from page_objects.about_page import AboutPage
from page_objects.post_page import PostPage
from page_objects.base_page import BasePage


class TestQABoy(unittest.TestCase):

    def setUp(self):
        '''setUp method will run before - each of our test cases
        (set up driver, launch site and other)'''
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_page_components(self):
        home_page = HomePage(self.driver)
        home_page.validate_title_is_present()
        home_page.validate_icon_is_present()
        home_page.validate_menu_options_are_present()
        home_page.validate_posts_are_visible()
        home_page.validate_social_media_links()

    def test_about_page_components(self):
        home_page = HomePage(self.driver)
        home_page.click_about_me_link()

        about_page = AboutPage(self.driver)
        about_page.validate_title_is_present()
        about_page.validate_icon_is_present()
        about_page.validate_menu_options_are_present()
        about_page.validate_social_media_links()
        about_page.validate_about_me_header()
        about_page.validate_about_me_post()

    def test_post_page_components(self):
        home_page = HomePage(self.driver)
        home_page.click_first_post()

        post_page = PostPage(self.driver)
        post_page.validate_title_is_present()
        post_page.validate_icon_is_present()
        post_page.validate_menu_options_are_present()
        post_page.validate_social_media_links()
        post_page.validate_post_image()
        post_page.validate_published_date()
        post_page.validate_share_buttons()
        post_page.validate_comment_section()

    def tearDown(self):
        '''tearDown method will run after - each of our test cases
        (clean up anything we did with our test case and quit the web driver)'''
        # Remember to always use “quit” instead of “close”.
        # If we used close, that would close the site but the instance of the web driver would remain alive.
        self.driver.instance.quit()


# The last 2 lines in our Class are there to let pytest know that this file contains tests.
if __name__ == '__main__':
    unittest.main()