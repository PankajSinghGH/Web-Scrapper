import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Ensure dynamic variable is passed
if len(sys.argv) < 2:
    print("Error: URL argument missing.")
    sys.exit(1)

dynamic_variable = sys.argv[1]
url = dynamic_variable

data = {'Product Name': [], 'Price': []}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses
except requests.RequestException as e:
    print(f"HTTP Request failed: {e}")
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

divProduct1 = soup.select("div.KzDlHZ")
divPrice1 = soup.select("div.Nx9bqj._4b5DiR")

for product, price in zip(divProduct1, divPrice1):
    data["Product Name"].append(product.text)
    data["Price"].append(price.text)

divProduct2 = soup.select("div.syl9yP")
divPrice2 = soup.select("div.Nx9bqj")
for product, price in zip(divProduct2, divPrice2):
    data["Product Name"].append(product.text)
    data["Price"].append(price.text)

new_df = pd.DataFrame.from_dict(data)

# Check if the Excel file exists
file_path = "F:\pythonProject\Scraped.xlsx"

if os.path.exists(file_path):
    # Read the existing data
    existing_df = pd.read_excel(file_path)
    # Append the new data
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    # If the file does not exist, use the new data
    combined_df = new_df

# Save the combined data back to the Excel file
combined_df.to_excel(file_path, index=False)

print(f"Data appended and saved to {file_path}")
