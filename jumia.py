import pandas as pd
import requests
from bs4 import BeautifulSoup

jumia = requests.get("https://www.jumia.co.ke/mlp-pay-day/")
#print(jumia.text)
src = jumia.content
soup = BeautifulSoup(src, 'lxml')
#product names
item_names = []
item_prices = []
item_ratings = []
item_discounts = []
all_products_by_name = soup.findAll('h3', class_='name')
#while shopping is True:
for product in all_products_by_name:
    product_names = soup.findAll('h3', class_='name')
    for element in product_names:
        product_name = element.get_text(strip=True)
        item_names.append(product_name)


    #product price
    product_prices = soup.findAll('div', class_='prc')
    for element in product_prices:
        product_price = element.get_text(strip=True)

        item_prices.append(product_price)

    #product rating
    product_ratings = soup.findAll('div', class_="rev")
    for element in product_ratings:
        product_rating = element.get_text(strip=True)
        item_ratings.append(product_rating)



    #product discount
    product_discounts = soup.findAll('div', class_="bdg _dsct _sm")
    for element in product_discounts:
        product_discount = element.get_text(strip=True)
        #
        item_discounts.append(product_discount)

min_length = min(len(item_names), len(item_prices), len(item_discounts), len(item_ratings))
    #prints the products details
for count in range(min_length):
#while count < (len(all_products_by_name) -1):
    print(f"the product is: {item_names[count]} it costs:{item_prices[count]} discounted at:{item_discounts[count]} rating is:{item_ratings[count]}")

    #count += 1
#collects all divs with the name,price,rating and discount
#src = jumia.content
#soup = BeautifulSoup(src, 'lxml')
#product = []
#divs = soup.findAll('div', class_='info')
#for info in divs:
   # product.append(info.get_text(#))
    #print(info.get_text())

data_2_csv = pd.DataFrame({'name': item_names[:min_length],
                           'price': item_prices[:min_length],
                           'Discount': item_discounts[:min_length],
                           'Rating': item_ratings[:min_length]
                           })
data_2_csv.to_csv("jumia.csv", index=False)
print(data_2_csv)





