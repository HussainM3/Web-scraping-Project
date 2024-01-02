# Video reference: https://www.youtube.com/watch?v=lTypMlVBFM4&t=111s
# Cant scrape websites that use Javascript for content loading (dynamic websites) with request and beautifulsoup
    # Wouldnt be able to get info
# For this reason use selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

# Get url of page you want to scrape from
rogersUrl = "https://www.rogers.com/plans#mobile-plans" #NOTE: use helium for getting full deal details

# Use selenium driver to access the page (Dont have to use chrome)
driver = webdriver.Chrome()

# run website
driver.get(rogersUrl)



# name of deal: 
# price (per month): 
# short desc: 
# Features: 
# Perks: 

# Gather all deals (all have tile with same class name)
#Note: newer version of selenium so must specify getting elements By XPATH (Must also import 'By' and separate space in class name by dots)
deals = driver.find_elements(By.CLASS_NAME, 'col-12.col-sm-6.col-md-4.mb-24.mt-sm-0.mt-md-0.ng-star-inserted')

# Loop to iterate through each deal
for deal in deals:
    # each element gotton using XPATH
    name = deal.find_element(By.XPATH, '//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[1]/dsa-vertical-tile/ds-tile/div/div/div[2]/p[2]').text
    price = deal.find_element(By.XPATH, '//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[1]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div').text
    desc = deal.find_element(By.XPATH, '//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[1]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/p[2]').text
    features = deal.find_element(By.XPATH, '//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[1]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[1]/p[2]').text
    perks = deal.find_element(By.XPATH, '//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[1]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[2]/p[2]').text
    print(name, ": ", price)
    