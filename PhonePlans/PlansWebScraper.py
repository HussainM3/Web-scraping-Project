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
for deal in range(1, len(deals)+1):
    # each element gotton using XPATH
    #XPATH always starts from closest block with id (in this case *[@id="converge"]). Since closest id was outside changing block, path needed to be edited
    name = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/p[2]').text
    priceDollars = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[1]').text
    priceCents = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[2]').text
    priceFreq = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[3]').text
    desc = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/p[2]').text
    features = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[1]/p[2]').text
    perks = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[2]/p[2]').text
    # print(name + ": " + priceDollars + priceCents + priceFreq)

class Plan:
    def __init__(self, name, price, desc, features):
        self.name = name
        self.price = price
        self.desc = desc
        self.features = features

class RogersPlan(Plan):
    def __init__(self, name, priceDollars, priceCents, priceFreq, desc, features, perks):
        super().__init__(name, priceDollars + priceCents + priceFreq, desc, features)
        self.perks = perks
