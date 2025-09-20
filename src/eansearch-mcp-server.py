import os
import re
from eansearch import EANSearch
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
app = FastMCP("eansearch")
ean_search_api_token = os.environ['EAN_SEARCH_API_TOKEN']

eansearch = EANSearch(ean_search_api_token)


@app.tool()
async def lookup_product(barcode: str) -> str:
    """Lookup the product for an EAN, GTIN, ISBN or UPC barcode.

    Args:
        barcode: the barcode (EAN, GTIN, ISBN or UPC)
    """
    if not ean_search_api_token:
        return "You need to set put your API token into the environment variable EAN_SEARCH_API_TOKEN. Get your API token from https://www.ean-search.org/ean-database-api.html"
    barcode = re.sub('[^0-9Xx]', '', barcode)
    if len(barcode) == 10:
        data = eansearch.isbnLookup(barcode)
        barcode = f"ISBN {barcode}" # for output below
    else:
        data = eansearch.barcodeLookup(barcode)
    if not data:
        return "No product found."
    return barcode + " is product " + data

@app.tool()
async def find_products(keywords: str) -> str:
    """Find products matching all the keywords with their EAN barcode.

    Args:
        keywords: keywords to search for
    """
    if not ean_search_api_token:
        return "You need to set put your API token into the environment variable EAN_SEARCH_API_TOKEN. Get your API token from https://www.ean-search.org/ean-database-api.html"
    productlist = eansearch.productSearch(keywords)

    if not productlist:
        return "No products found."
    
    result = ''
    for p in productlist:
        if result:
            result += ", "
        result += 'EAN ' + p["ean"] + " is " + p["name"]
        if (p['categoryName'] != 'Unknown'):
            result += ' from the category ' + p['categoryName']
    return result

if __name__ == "__main__":
    # Initialize and run the server
    app.run(transport='stdio')
