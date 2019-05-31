from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def getData(url, second=5):
    # Specify the url

    # The path to where you have your chrome webdriver stored:
    webdriver_path = 'E:\PyCharm\chromedriver_win32/chromedriver.exe'

    # Add arguments telling Selenium to not actually open a window
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--windows-size=1920x1080')

    # Fire up the headless browser
    browser = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

    # Load Webpage
    browser.get(url)

    # It can be a good idea to wait for a few seconds before trying to parse
    # To ensure that the page has loaded completely.
    time.sleep(second)

    # Parse HTML, close browser
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()

    return soup