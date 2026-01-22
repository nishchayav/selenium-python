
"""Day8	Question 1 – Web Interaction & REST API Consumption						
Write a Python program that:			
1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)			
2. Sends custom headers with the request			
3. Parses the JSON response and extracts specific fields			
4. Serializes the extracted data and saves it into a JSON file			
5. Handles HTTP errors using proper exception handling



import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    # 1️⃣ Custom headers
    headers = {
        "User-Agent": "Python-Requests-Client",
        "Accept": "application/json"
    }

    try:
        # 2️⃣ Send GET request
        response = requests.get(url, headers=headers, timeout=5)

        # 3️⃣ Handle HTTP errors
        response.raise_for_status()

        # 4️⃣ Parse JSON response
        users = response.json()

        # 5️⃣ Extract specific fields
        extracted_data = []
        for user in users:
            extracted_data.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"]
            })

        # 6️⃣ Save extracted data to JSON file
        with open("users_data.json", "w") as file:
            json.dump(extracted_data, file, indent=4)

        print("Data successfully fetched and saved to users_data.json")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API")
    except requests.exceptions.Timeout:
        print("Error: Request timeout")


        """





'''	
Question 2 – HTML Parsing & Data Extraction
Parsing HTML (BeautifulSoup, lxml), Web automation basics
Write a Python program that:
1. Fetches an HTML webpage using the requests library
2. Parses the HTML using BeautifulSoup with the lxml parser
3. Extracts:Page title, All hyperlinks, Specific table or list data
4. Converts the extracted data into JSON format
5. Saves the output into a file for further automation or analysis'''




import requests
from bs4 import BeautifulSoup
import json


url ="https://www.w3schools.com/html/html_tables.asp"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

pagetitle=soup.title.string if soup.title else "No title"

print(pagetitle)

for link in soup.find_all("a"):
    href=link.get("href")
    print(href)
tabledata=[]
table=soup.find("table")
if table:
    rows=table.find_all("tr")
    for row in rows[1:]:
        columns=row.find_all("td")
        row_data=[col.text.strip() for col in columns]
        print(row_data)
        tabledata.append(row_data)
extracted_data={
    "page_title":pagetitle,
    "total_links":len(href),
    "links":href,
    "table_data":tabledata
}

with open("extracteddata.json",'w',encoding="utf-8") as file:
    json.dump(extracted_data,file,indent=4)