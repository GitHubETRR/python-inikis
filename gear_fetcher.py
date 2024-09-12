import requests
import json
import sys

catalog_params = {
    "Category": 11,
    "Subcategory": 5,
    "Limit": 30,
    "Cursor": "",
}
catalogURL = "https://catalog.roblox.com/v1/search/items/details?"

items = []

page = 0

def exit_program():
    input()
    sys.exit()

def catalog_query():
    print("quering")
    response = requests.get(catalogURL, catalog_params)
    print(response)
    if response:
        return response.json()
    else:
        print("Could not fetch a request from the URL. Do you have access to the website?")
        exit_program()

print("ROBLOX Gear items fetcher\nStarting...")

# begin requests
while True:
    data = catalog_query()
    
    exit_program()

    if "nextPageCursor" not in data:
        if page == 0: 
            print("API limit reached because of a previous session. Please wait a minute and restart this program again.")
            exit_program()

        # the API reached a limit or smth.
        # we re-start using the last nextPageCursor
        # and we re-query until we receive data
        print("API limit reached. Re-quering until limit ban is revoked. This should take no more than a minute.")
        attempts = 0
        while "nextPageCursor" not in data:
            if attempts > 120: 
                print("Re-query attempt limit reached. Aborting request operation early.")
                break
            attempts+=1

            attempted_data = catalog_query()
            if "nextPageCursor" in attempted_data: 
                data = attempted_data 
                break

    page+=1
    print("Fetching page", page)
    
    for item in data["data"]:
         newItem = (item["id"], item["name"])
         items.append(newItem)

    if data["nextPageCursor"] is None: break # last page
    
    catalog_params["Cursor"] = data["nextPageCursor"]

print("Requests finished. Compiling data into JSON")

txt = open("catalog_items.json", "w")
txt.write(json.dumps(items))
txt.close()

exit_program()
