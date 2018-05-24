# This file will be our Test Suite and will store all the test cases for our QABoy site.
import unittest
from webdriver import Driver
from values import strings
from page_objects.home_page import HomePage

class TestQABoy(unittest.TestCase):

    def setUp(self):
        '''setUp method will run before - each of our test cases
        (set up driver, launch site and other)'''
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_page = HomePage(self.driver)
        home_page.validate_title_is_present()
        home_page.validate_icon_is_present()
        home_page.validate_menu_options_are_present()
        home_page.validate_posts_are_visible()
        home_page.validate_social_media_links()

    def tearDown(self):
        '''tearDown method will run after - each of our test cases
        (clean up anything we did with our test case and quit the web driver)'''
        # Remember to always use “quit” instead of “close”.
        # If we used close, that would close the site but the instance of the web driver would remain alive.
        self.driver.instance.quit()


# The last 2 lines in our Class are there to let ?pytest know that this file contains tests.
if __name__ == '__main__':
    unittest.main()