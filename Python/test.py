import requests
import pandas as pd
import json

# --- Configuration ---
# Using the Coca-Cola barcode from the PDF you provided
barcode = "5449000054227" 
output_filename = "api_columns_list.xlsx"

# OpenFoodFacts API endpoint
url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

print(f"Fetching data for barcode: {barcode}...")

try:
    # --- 1. Fetch data from the API ---
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)

    # --- 2. Load the JSON response ---
    data = response.json()

    # The main product data is inside the "product" key
    if "product" in data:
        product_data = data["product"]

        # --- 3. Get all the top-level keys (column names) ---
        column_names = list(product_data.keys())
        print(f"Found {len(column_names)} columns/fields in the API response.")

        # --- 4. Create a Pandas DataFrame ---
        # A DataFrame is like a table, perfect for exporting to Excel
        df = pd.DataFrame(column_names, columns=["Available API Columns"])

        # --- 5. Save the DataFrame to an Excel file ---
        # The index=False part prevents pandas from writing row numbers into the Excel file
        df.to_excel(output_filename, index=False)

        print(f"✅ Success! All column names have been saved to '{output_filename}'")

    else:
        print("Error: 'product' key not found in the API response.")
        print("Full response:", json.dumps(data, indent=2))

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")