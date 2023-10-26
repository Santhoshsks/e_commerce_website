import http.client
import json
import matplotlib.pyplot as plt
import numpy as np
import json

""" conn = http.client.HTTPSConnection("axesso-walmart-data-service.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': "2462163276msh2728e3d299cf15ap15ef57jsn4803740f328c",
    'X-RapidAPI-Host': "axesso-walmart-data-service.p.rapidapi.com"
}
conn.request("GET", "/wlm/walmart-search-by-keyword?keyword=Lego%20Star%20Wars&page=1&sortBy=best_match", headers=headers)
res = conn.getresponse()
data = res.read()

# Parse the JSON response
product_data = json.loads(data.decode("utf-8"))


# Open the JSON file for writing
with open("lego_star_wars_product_data.json", "w") as f:
    # Write the product data to the JSON file
    json.dump(product_data, f)

# Get the product prices and ratings """

# Open the JSON file for reading
with open("lego_star_wars_product_data.json", "r") as f:
    # Load the product data from the JSON file
    product_data = json.load(f)

# Extract the product price and rating data from the JSON data
product_prices = []
product_ratings = []
for item in product_data["item"]["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"]:
    # Check if the item has the required keys
    if all(key in item for key in ["price", "rating", "averageRating"]):
        product_prices.append(float(item["price"]))
        product_ratings.append(float(item["rating"]["averageRating"]))

# Sort the product prices and ratings by price
sorted_product_prices = np.sort(product_prices)
sorted_product_ratings = np.sort(product_ratings)

# Plot the relationship between product price and rating
plt.plot(sorted_product_prices, sorted_product_ratings)

# Add labels and title
plt.xlabel("Product Price")
plt.ylabel("Product Rating")
plt.title("Relationship between Product Price and Rating for LEGO Star Wars Products")

# Show the plot
plt.show()