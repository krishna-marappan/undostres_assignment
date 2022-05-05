from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverSetup():

    def website_launch(websiteurl):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(websiteurl)
        return driver
