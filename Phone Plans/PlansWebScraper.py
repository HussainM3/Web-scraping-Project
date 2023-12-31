# Cant scrape websites that use Javascript for content loading (dynamic websites) with request and beautifulsoup
    # Wouldnt be able to get info
# For this reason use selenium

from selenium import webdriver

# Get url of page you want to scrape from
rogersUrl = "https://www.rogers.com/plans#mobile-plans"

# Use selenium driver to get the page (Dont have to use chrome)
driver = webdriver.Chrome()