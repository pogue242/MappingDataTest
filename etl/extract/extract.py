import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
limit = 1000
pageNum = 1
drinkingFountainsAPIURL = f"https://data.cityofnewyork.us/api/v3/views/qnv7-p7a2/query.json?page_number={pageNum}&page_size={limit}&app_token={API_TOKEN}"
treesCensusAPIURL = f"https://data.cityofnewyork.us/api/v3/views/uvpi-gqnh/query.json?page_number={pageNum}&page_size={limit}&app_token={API_TOKEN}"
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    NormalizedData = pd.json_normalize(data)
    return NormalizedData

def read_drinking_fountains_data():
    data = fetch_data(drinkingFountainsAPIURL)
    dataFrame = pd.DataFrame(data)
    return dataFrame

def read_tree_census_data():
    data = fetch_data(treesCensusAPIURL)
    dataFrame = pd.DataFrame(data)
    return dataFrame
