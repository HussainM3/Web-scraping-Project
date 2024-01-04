# Plan objects to be used for saving plans info
class Plan:
    def __init__(self, name, price, desc, features):
        self.name = name
        self.price = price
        self.desc = desc
        self.features = features

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nDescription: {self.desc}\nFeatures: {self.features}"

class RogersPlan(Plan):
    def __init__(self, name, priceDollars, priceCents, priceFreq, desc, features, perks):
        super().__init__(name, priceDollars + priceCents + priceFreq, desc, features)
        self.perks = perks

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nDescription: {self.desc}\nFeatures: {self.features}\nPerks: {self.perks}"

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

driver.get(rogersUrl) # for rogers phone plan deals

# name of deal: 
# price (per month): 
# short desc: 
# Features: 
# Perks: 

# Gather all deals (all have tile with same class name)
#Note: newer version of selenium so must specify getting elements By XPATH (Must also import 'By' and separate space in class name by dots)
deals = driver.find_elements(By.CLASS_NAME, 'col-12.col-sm-6.col-md-4.mb-24.mt-sm-0.mt-md-0.ng-star-inserted')

rogersPlans = []

# Loop to iterate through each deal
for deal in range(1, len(deals)+1):
    # wait to ensure everythin is loaded (otherwise will get StaleElementReferenceException)
    driver.implicitly_wait(10)
    
    # each element gotton using XPATH
    #XPATH always starts from closest block with id (in this case *[@id="converge"]). Since closest id was outside changing block, path needed to be edited
    name = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/p[2]').text
    driver.implicitly_wait(10)
    priceDollars = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[2]').text
    driver.implicitly_wait(10)
    priceCents = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[3]/span').text
    driver.implicitly_wait(10)
    priceFreq = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/ds-price/div/div/div[4]').text
    driver.implicitly_wait(10)
    desc = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/div[2]/dsa-price/div/p[2]').text
    driver.implicitly_wait(10)
    features = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[1]/p[2]').text
    driver.implicitly_wait(10)
    perks = deals[deal-1].find_element(By.XPATH, f'//*[@id="converge"]/dsa-layout/div/div/rci-ui-block-wrapper/div/div/rci-ui-block-tile-plans/div/div/div[{deal}]/dsa-vertical-tile/ds-tile/div/div/div[2]/ul/li[2]/p[2]').text
    # print(name + ": " + priceDollars + priceCents + priceFreq)

    # Create rogers plan object and add to list
    rogersPlans.append(RogersPlan(name, priceDollars, priceCents, priceFreq, desc, features, perks))

# Add all plans to text file
with open("PhonePlans/plans.txt", "w") as file:
    file.write("**************************************************\nRogers Plans:\n--------------------------------------------------\n")
    for plan in rogersPlans:
        file.write(str(plan) + "\n\n")
    file.write("**************************************************")
