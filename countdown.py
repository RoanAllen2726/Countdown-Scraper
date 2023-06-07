from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
import csv
import re
import lxml
import datetime
import pandas as pd


class DataGetter:
    def generate():
        # Create dictionaries of keywords for each category
        meat_poultry = ['beef', 'pork', 'chicken', 'turkey', 'lamb', 'sausage', 'patties', 'steak']
        fish_seafood = ['fish', 'salmon', 'shrimp', 'crab', 'lobster', 'prawn', 'mussels', 'fillet']
        fridge_deli = ['cheese', 'yogurt', 'milk', 'cream', 'butter', 'egg', 'ham', 'bacon', 'salami',
                       'olivani', 'hummus', 'dip', 'prosciutto', 'dairy', 'yoghurt']
        bakery = ['bread', 'bagel', 'pastry', 'croissant', 'muffin', 'buns', 'bakery']
        frozen = ['frozen','ice cream', 'pizza', 'frozen vegetables', 'frozen fruits', 'vegetables', 'ice block']
        pantry = ['cereal', 'pasta', 'rice', 'beans', 'sauces', 'spices', 'chips', 'spread', 'cereal',
                  'sauce', 'chocolate', 'biscuits', 'crackers', 'noodles', 'coffee', 'espresso',
                  'robert harris', 'oats', 'dressing']
        beer_wine = ['beer', 'wine', 'spirits', 'whiskey', 'vodka', 'rose', 'pinot', 'sauvignon',
                     'cider', 'brut', 'shiraz', 'chardonnay', 'merlot', '19 crimes', 'riesling', 'moscato']
        drinks = ['soda', 'kombucha', 'juice', 'water', 'tea', 'coffee', 'drink', 'coke', 'fanta', 'pepsi', 'sprite']
        health_body = ['vitamins', 'supplements', 'shampoo', 'soap', 'lotion', 'tissues', 'toothpaste',
                       'conditioner', 'body wash', 'mouthwash', 'hand wash', 'deodorant' 'antiperspirant', 'aerosol',
                       'hair', 'vitamin', 'tablets', 'neutrogena', 'glow lab', 'rimmel', 'shower gel']
        household = ['cleaning supplies', 'laundry detergent', 'paper towels', 'batteries', 'dishwash',
                     'laundry', 'battery', 'wipes']
        baby_child = ['diapers', 'baby food', 'toys']
        pet = ['dog food', 'cat food', 'pet toys']

        # generating todays date and using it as the filename
        filename1 = "data/" + datetime.datetime.now().strftime("%d_%m_%Y") + ".csv"

        # the following options are only for setup purposes
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=chrome_options)

        # creating the csv file to write to
        with open(filename1, mode="w", newline="", encoding="UTF-8") as csvfile:
            fieldnames = ['item_name', 'full_price', 'new_price', 'discount', 'amount_saved', 'category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            x = 2
            y = 100

            while x <= y:
                # generating countdown link with changing page number
                URL = ("https://www.countdown.co.nz/shop/specials?page=" + str(x).strip() + "&inStockProductsOnly=true&size=120")
                driver.get(URL)
                time.sleep(3)  # any number > 3 should work fine
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')

                # getting max page number and setting it as new limit (y)
                while y == 100:
                    y = soup.find('search-footer')
                    y = y.findAll('li', class_="ng-star-inserted")
                    y = int(y[-1].get_text())
                # getting a list of all the items on the page and extracting the data
                items = soup.findAll('cdx-card', class_="card ng-star-inserted")
                try:
                    for item in items:
                        # collecting the data
                        title = item.find('h3').get_text()
                        fullprice = item.find('span', class_="price price--was ng-star-inserted").get_text()
                        discount = item.find('span', class_="price price--save ng-star-inserted").get_text()
                        new_price = item.find('h3', class_="heading--2 presentPrice price--special ng-star-inserted").get_text()
                        cost_index = fullprice.index("$")
                        disc_index = discount.index("$")
                        category = 'Unknown'

                        # calculating the percentage which is discounted
                        amount_saved = round(float(discount[disc_index+1:]) / float(fullprice[cost_index+1:]) * 100, 2)

                        # Categorize items based on keywords
                        for keyword in meat_poultry:
                            if keyword in title.lower():
                                category = 'Meat & Poultry'
                                break
                        for keyword in fish_seafood:
                            if keyword in title.lower():
                                category = 'Fish & Seafood'
                                break
                        for keyword in fridge_deli:
                            if keyword in title.lower():
                                category = 'Fridge & Deli'
                                break
                        for keyword in bakery:
                            if keyword in title.lower():
                                category = 'Bakery'
                                break
                        for keyword in frozen:
                            if keyword in title.lower():
                                category = 'Frozen'
                                break
                        for keyword in pantry:
                            if keyword in title.lower():
                                category = 'Pantry'
                                break
                        for keyword in beer_wine:
                            if keyword in title.lower():
                                category = 'Beer & Wine'
                                break
                        for keyword in drinks:
                            if keyword in title.lower():
                                category = 'Drinks'
                                break
                        for keyword in health_body:
                            if keyword in title.lower():
                                category = 'Health & Body'
                                break
                        for keyword in household:
                            if keyword in title.lower():
                                category = 'Household'
                                break
                        for keyword in baby_child:
                            if keyword in title.lower():
                                category = 'Baby & Child'
                                break
                        for keyword in pet:
                            if keyword in title.lower():
                                category = 'Pet'
                                break
                        # adding the item to the csv file in the format of a dictionary
                        writer.writerow({'item_name': title.strip(), 'full_price': fullprice, 'new_price': new_price, 'discount': discount, 'amount_saved': amount_saved, 'category': category})
                except:
                    pass
                # increment the page number
                x += 1

        # sort and save the data by the amount saved
        csvData = pd.read_csv(filename1)
        sorteddata = csvData.sort_values(by=["amount_saved"], ascending=False)
        sorteddata.to_csv(filename1, index=False, encoding="UTF-8")

        return filename1


print(DataGetter.generate())