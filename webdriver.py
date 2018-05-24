from selenium import webdriver

class Driver:
    ''' I like to have a custom navigate method instead of the default “get(URL)” from the web driver
    because this allows me to add some validations that come really handy when debugging.
    In this case, I validate that the URL is a string before trying to navigate.'''

    def __init__(self):
        self.instance = webdriver.Chrome()
        self.instance.maximize_window()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")